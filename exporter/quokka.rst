Quokka
======


..  figure:: ../quokka/docs/img/logo.png
    :align: center
    :width: 30%



`Quokka <https://github.com/quarkslab/quokka>`_ is a binary exporter developed by Quarkslab. It serves the same
purpose than BinExport but it exports more data like data references that Binexport does not. The goal is to approach
the disassembler functionalities in terms of available information.

It has also been designed with space efficiency in mind. The goal is to have a minimal overhead in comparison to other
exports or disassembler databases (e.g: .i64) so that they can be kept along with the binary. Everything that can be
retrieve from the static executable file will be (strings, data, etc). Also Quokka leverages the variable integer length
encoding of protobuf to reduce their size as much as possible.

A thorough comparison of time, and space differences between Quokka and other exporters have been done in
`this blogpost <https://blog.quarkslab.com/an-experimental-study-of-different-binary-exporters.html>`_.


.. note::

    Quokka's homepage and **documentation** is hosted at:  `https://quarkslab.github.io/quokka/ <https://quarkslab.github.io/quokka/>`_



.. include:: ../quokka/docs/README.md
   :parser: myst_parser.sphinx_
