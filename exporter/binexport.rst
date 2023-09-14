Binexport
=========


`BinExport <https://github.com/google/binexport>`_ is an utility hosted on Google's github to export the disassembly
obtained from IDA Pro, Binary Ninja and Ghidra into external file. The file is defined in `Protobuf <TODO>`_. It is
particularly used by `BinDiff <https://www.zynamics.com/bindiff.html>`_ as input for its diffing.

For more details: `Project homepage <TODO>`_

**Limitations**:
Besides, working like a charm, BinExport is essentially lacking the two following features:

* regardless of the disassembler (IDA, Ghidra ..), binexport has to be launched manually through GUI or via a shell
  command if the disassembler support headless mode. There are no programmatic bindings to trigger an export.
* Exported data are very useful, but has binexport was defined as an internal format, there are no API to manipulate
  exported data.

As such, `python-binexport <https://github.com/quarkslab/python-binexport>`_ has been developed to fulfill
these two weaknesses.


.. include:: ../python-binexport/README.md
   :parser: myst_parser.sphinx_


API
---

Program
~~~~~~~

.. autoclass:: binexport.program.ProgramBinExport
    :members:
    :undoc-members:
    :exclude-members:
    :show-inheritance:

Function
~~~~~~~~

.. autoclass:: binexport.function.FunctionBinExport
    :members:
    :undoc-members:
    :exclude-members:

Basic Block
~~~~~~~~~~~

.. autoclass:: binexport.function.BasicBlockBinExport
    :members:
    :undoc-members:
    :exclude-members:
    :show-inheritance:

Instruction
~~~~~~~~~~~

.. autoclass:: binexport.instruction.InstructionBinExport
    :members:
    :undoc-members:
    :exclude-members:

Operand
~~~~~~~

.. autoclass:: binexport.operand.OperandBinExport
    :members:
    :undoc-members:
    :exclude-members:

Expression
~~~~~~~~~~

.. autoclass:: binexport.expression.ExpressionBinExport
    :members:
    :undoc-members:
    :exclude-members:

Types
~~~~~

.. automodule:: binexport.types
    :members:
    :undoc-members:
    :exclude-members:
