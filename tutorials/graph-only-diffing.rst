Diffing Graphs only
===================

QBinDiff is able to perform graph matching, whether this graph is a Control Flow Graph (CFG),
a Call Graph (CG), or something completely unrelated.
We demonstrated this in our `introductory blog post <https://blog.quarkslab.com/qbindiff-a-modular-diffing-toolkit.html>`_
with the protein-protein interaction (PPI) networks of different species in bioinformatics.

In this tutorial, we will focus our attention on the CFG of EVM smart contracts.

Motivation
----------

The Ethereum Virtual Machine (EVM) is a RISC stack-based architecture.
It is used by Ethereum and other compatible chains to execute smart contracts,
the core programs of decentralized applications on these platforms.

In addition to the lack of native support from tools such as QBinDiff, BinExport, and Quokka,
the EVM bytecode lacks an explicit structure to identify functions:
all the control flow is performed with only conditional and unconditional jumps (``JUMPI``, ``JUMP``),
that read the destination address on the stack.
This design leads to particular patterns in the bytecode, for example:

* the start of the bytecode contains a dispatcher, acting like a giant switch statement,
  that is responsible for jumping into the called external/public function;
* to call internal functions and other forms of duplicated code,
  the caller pushes a return address onto the stack before executing a jump instruction.

However, several tools let you recover the CFG of the smart contract
(some even detect functions with varying degrees of success).
From this information alone, this tutorial will guide you with diffing an example smart contract.

How to diff
-----------

In this tutorial, we will diff two versions of an example smart contract.
One allows its user's balance to go negative but not the other.

+---------------------------------------+----------------------------------+
| ``vulnerable.sol``                    | ``fixed.sol``                    |
+=======================================+==================================+
|.. literalinclude:: res/vulnerable.sol |.. literalinclude:: res/fixed.sol |
+---------------------------------------+----------------------------------+
|.. literalinclude:: res/vulnerable.evm |.. literalinclude:: res/fixed.evm |
+---------------------------------------+----------------------------------+

To this end, we will use QBinDiff's ``DiGraphDiffer`` to compare their CFG.

Generate the graphs
^^^^^^^^^^^^^^^^^^^

The first step is to recover the CFG from the bytecode of the smart contracts.
While not trivial, this has been solved by several tools already.
We recommend `EtherSolve <https://github.com/SeUniVr/EtherSolve/>`_ (java)
or `vandal <https://github.com/usyd-blockchain/vandal/>`_ (python).

.. code-block:: sh

  java -jar EtherSolve.jar -r -j vulnerable.evm

The command above generates a file named ``Analysis_<datetime>.json``.
In this file, the CFG can be found under the ``runtimeCfg`` field.
Note that edges are stored under ``runtimeCfg.successors`` (and sometimes have duplicate entries).

QBinDiff's differ expects ``networkx.DiGraph`` as inputs, so we will need to adapt the data a little bit:

.. code-block:: python

  def process_ethersolve(analysis: dict[str, Any]) -> networkx.DiGraph:
      # Filter the desired attributes and set the node ID as the basic block's offset
      nodes = [
          {
              "id": n["offset"],
              "length": n["length"],
              "type": n["type"],
              "stack_balance": n["stackBalance"],
              "bytecode": n["bytecodeHex"],
              "opcodes": n["parsedOpcodes"],
          } for n in analysis["runtimeCfg"]["nodes"]
      ]

      # Generate an edge for each successor of each node
      links = [
          [{"source": e["from"], "target": t} for t in e["to"]]
          for e in analysis["runtimeCfg"]["successors"]
      ]
      # Flatten the list
      links = [item for sublist in links for item in sublist]

      # Create the networkx.DiGraph
      nx_node_link = {"directed": True, "multigraph": False, "nodes": nodes, "links": links}
      return networkx.node_link_graph(nx_node_link)
 

(optional) Write heuristics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When matching nodes, we can help the differ by setting an initial similarity score between each pair of nodes.
These scores are gathered in the similarity matrix, initialized to all 1,
meaning every node is initially believed to be similar to all nodes.

If you have access to some heuristic for similarity between nodes,
you can add a prepass that will be executed before matching nodes to alter the similarity matrix.

For example, we have access to the stack balance of each basic block.
This value indicates how many words the basic block pushes or pops from the stack.
Intuitively, similar blocks should have the same stack balance.

You can find more information `here <../qbindiff/doc/source/api/differ.html#qbindiff.Differ.register_prepass>`_
on how to create a prepass.

In this example, we first arrange nodes by stack balance in each graph,
then reduce the similarity of nodes that do not share the same stack balance.

Note that the nodes' IDs are their offset, and do not correspond to the row or column in the similarity matrix.
The correspondance is given by the ``primary_n2i`` and ``secondary_n2i`` mappings.

.. code-block:: python

  def prepass_stack_balance(
      sim_matrix: SimMatrix,
      primary: qbindiff.GenericGraph,
      secondary: qbindiff.GenericGraph,
      primary_n2i: dict[int, int],
      secondary_n2i: dict[int, int],
      **kwargs,
  ) -> None:
      # Arrange nodes indices by stack balance

      ## Primary node indices by stack balance
      primary_index: dict[int, list[int]] = {}
      ## Secondary node indices by stack balance
      secondary_index: dict[int, list[int]] = {}
  
      ## Populate primary_index and secondary_index
      for graph, n2i, index in (
          (primary, primary_n2i, primary_index),
          (secondary, secondary_n2i, secondary_index),
      ):
          for node_id in graph.nodes():
              node = graph.nodes[node_id]
              balance = node["stack_balance"]
              if balance not in index:
                  index[balance] = []
              index[balance].append(n2i[node_id])
  
      # Reduce the similarity of nodes that do not share the same stack balance by 60%
      for primary_balance, primary_indices in primary_index.items():
          for secondary_balance, secondary_indices in secondary_index.items():
              if primary_balance == secondary_balance:
                  continue
              for i in primary_indices:
                  sim_matrix[i, secondary_indices] *= 0.4

Perform the match
^^^^^^^^^^^^^^^^^

Once you have the CFG in a ``networkx.DiGraph`` object,
and have optionally written some prepasses, performing the mapping is simple:

.. code-block:: python

  differ = qbindiff.DiGraphDiffer(
      primary_cfg,
      secondary_cfg,
      sparsity_ratio=0,
      tradeoff=0.5,
      epsilon=0.1,
  )
  differ.register_prepass(prepass_stack_balance)  # optional
  mapping = differ.compute_matching()

You can experiment with the tradeoff and epsilon values,
depending on the nature of the diffing performed.
As general guidelines:

* ``tradeoff`` gives more weight to the topology when close to 0,
  and more weight to the similarity when close to 1.
  It should be set strictly between 0 and 1.
  The better your heuristics, the higher its value.
* ``epsilon`` controls the convergence speed.
  It should not be set to 0, and be as close to 1 as you can afford to wait.
  For this simple example, a conservative low value is not an issue.
* you should adjust how much your prepasses affect the similarity matrix,
  depending on the quality of your heuristics.

For this example, we performed an exhaustive search of these parameters,
when compared to a ground truth matching.
In these maps, ``epsilon`` and ``tradeoff`` correspond to the above parameters,
while ``stack balance weight`` controls how much the stack balance prepass impacts the similarity matrix.

+-------------------------------------------------+--------------------------------------------------+-------------------------------------+
| .. image:: res/stack-balance-weight-epsilon.png | .. image:: res/stack-balance-weight-tradeoff.png | .. image:: res/tradeoff-epsilon.png |
+-------------------------------------------------+--------------------------------------------------+-------------------------------------+

Process the result
^^^^^^^^^^^^^^^^^^

Now that you have a mapping between nodes of the primary and secondary graphs,
you can process it however you like, for example to compute similarity score.

Here we show a visualization of the resulting diff, revealing interesting aspects of the modification:

+------------------------------------+-----------------------------+------------------------------------+
| From signed to unsigned operations | CFG rewiring                | Dispatcher update                  |
+====================================+=============================+====================================+
| .. image:: res/diff-signedness.png | .. image:: res/diff-cfg.png | .. image:: res/diff-dispatcher.png |
+------------------------------------+-----------------------------+------------------------------------+
