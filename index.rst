==============
Diffing Portal
==============

This documentation aims to provide various resources on binary diffing which is handy for reverse-engineering.
Tools and associated publications related to diffing are slightly scattered online thus the goal is to
reference them here by centralizing information.

Diffing
-------

Binary diffing is usually performed between two binaries, usually referred as primary and secondary.
Diffing requires comparing the two programs using common artifacts. At binary-level, disassemblers usually
lift the program into functions that encode the different functionalities provided by the program.
This lifting requires identifying accurately functions content, their bounds etc. It is usually the
last refinement steps of the disassembly before decompilation. As such, diffing is usually performed
at function level. Diffing aims at computing an assignment between functions from primary to secondary.
The assignment is usually 1-to-1 but by means of optimization or obfuscation functions can be inlined
or splitted. As such some utilities tries computing an M-to-N mapping between functions [TODO: REFS].


Overview
--------

Most differs rely on existing disassembler like IDA Pro or Ghidra for disassembly as they work on a
disassembled representation of the program. However they usually relies on an an intermediate format
allowing to perform the diff outside of the disassembler context. The software generating this file
is usually implemented as a disassembler plugin and is called exporter. The Figure below shows the
relationships between some disassemblers, exporters and differs.

.. raw:: html

    <figure class="align-center">

.. raw:: html
   :file: _static/overview_diff_tools2.svg

.. raw:: html

    </figure>

As shown on the figure the base layer are disassemblers from which differs tries to be independents from.
The second layer are exporters which provides an interface to disassembler by serializing the disassembly
in a format specific file which is later read by the differ to perform the diff. The figure shows various
tools and modules discussed on this portal, especially python-bindiff, python-binexport, qbindiff, and quokka.


.. toctree::
    :caption: Exporters
    :maxdepth: 2
    :hidden:

    exporter/binexport
    exporter/quokka

.. toctree::
    :caption: Qbindiff
    :maxdepth: 3
    :hidden:

    qbindiff/doc/source/intro
    qbindiff/doc/source/install
    qbindiff/doc/source/how
    qbindiff/doc/source/api/qbindiff


.. toctree::
    :caption: Third-party differs
    :maxdepth: 2
    :hidden:

    differs/bindiff
    differs/diaphora


.. toctree::
    :caption: Tutorials
    :maxdepth: 2
    :hidden:

    tutorials/tutorials


.. toctree::
    :caption: Tools
    :maxdepth: 2
    :hidden:

    tools/idascript

.. toctree::
    :caption: Resources
    :maxdepth: 2
    :hidden:

    resources/academia
    resources/industry

How to Contribute ?
-------------------

This page aims at aggregating various ressources related to diffing.
Thus, pull requests to contribute are warmly welcomed to add new utility
link or other resources.
