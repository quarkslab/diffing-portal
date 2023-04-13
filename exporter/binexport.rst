Binexport
=========

Introduction
------------

`BinExport <https://github.com/google/binexport>`_ is a tool provided by Google that helps to export binary dissassemblies from IDA Pro as an example. It is used in particular by the differ `BinDiff <https://www.zynamics.com/bindiff.html>`_ or by QBinDiff. 

BinExport, whether it is the IDA, BinaryNinja or Ghidra version, mainly relies on the GUI : it requires to manually launch the tools, then go the setting and export the binary into a BinExport file. This process is not well suited for automated binary export. 

python-binexport
----------------
Because using BinExport tends to be difficult for an automated task, we provide python-binexport, a python module aiming to give a friendly interface to create, load and manipulate binexport files.


Installation
~~~~~~~~~~~~

BinExport has to be installed first, as python-binexport entirely relies on it. The project is available ` here <https://github.com/google/binexport>`_

.. note::
   python-binexport requires at least IDA Pro 7.2 (as it calls the `BinExportBinary` IDC function).

It is recommanded to install all the diffing tools in the same virtual env. To install python-binexport :

..  code-block:: bash
    python3 -m venv venv
    source venv/bin/activate
    pip install python-binexport
    
Optionally, python-binexport may require `idascript <https://github.com/quarkslab/idascript>`_ to directly generate the binexport files. See the setup.py file for more detail about installation.

Usage
~~~~~

python-binexport is particularly convenient to use and manipulate BinExport files. For example, the following python snippet iterates on every function of the program, every basic blocks, instructions, operands and expression. 

..  code-block:: python
    from binexport import ProgramBinExport

    p = ProgramBinExport("myprogram.BinExport") # Load the binexport file
    for fun_addr, fun in p.items(): # Fun_addr is the function address in the binary, fun is the object
        for bb_addr, bb in fun.items(): # The same holds for bb_addr and bb
            for inst_addr, inst in bb.items(): # Same as before
                for operand in inst.operands:
                    for exp in operand.expressions:
                        pass  # Do whatever at such deep level

API
---

.. toctree::
    :caption: API
    :maxdepth: 2
    :hidden:

    python-binexport/doc/api
