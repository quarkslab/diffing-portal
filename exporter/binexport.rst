Binexport
=========


`BinExport <https://github.com/google/binexport>`_ is a tool provided by Google that helps to export binary
dissassemblies from IDA Pro as an example. It is used in particular by the differ
`BinDiff <https://www.zynamics.com/bindiff.html>`_ or by QBinDiff. 

BinExport, whether it is the IDA, BinaryNinja or Ghidra version, mainly relies on the GUI : it requires to manually
launch the tools, then go the setting and export the binary into a BinExport file.


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

Function
~~~~~~~~

.. autoclass:: binexport.function.FunctionBinExport
    :members:
    :undoc-members:
    :exclude-members:

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
