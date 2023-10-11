Diaphora
========

`Diaphora <https://github.com/joxeankoret/diaphora/>`_ is an open-source binary diffing tool deeply integrated into IDA
Pro. A new version, the `3.1 <https://github.com/joxeankoret/diaphora/releases/tag/3.1>`_, has recently been released in 2023. It offers a variety of features that are used to
compute the diff between two binaries, some of which are common to BinDiff and QBinDiff.

Diaphora uses a custom SQLite database to export the relevant informations it needs. As it is very specific to
this software, it has not been referenced in exporter section;

Contrary to other differs, Diaphora uses a sequential process to output matches : a set of rules are defined to
establish the matches. These rules are executed from the most reliable query to the less reliable one. Thus it
iteratively refine the match by applying these rules.

More details and thorough documentation can be found on Diaphora's `website <http://diaphora.re>`_
and the associated `Github <https://github.com/joxeankoret/diaphora/>`_ repository.
