Bindiff
=======

<<<<<<< HEAD
`BinDiff <https://www.zynamics.com/bindiff.html>`_ is one of the oldest and most
widely used differ in the reverse engineering community. First conceived at Zynamics,
it was then acquired by Google. This differ is based on properties of CallGraph to
establish matches between functions of two binaries. For more details about BinDiff
heuristics, have a look at `one the first paper <https://static.googleusercontent.com/media/www.zynamics.com/en//downloads/bindiffsstic05-1.pdf>`_
or the `documentation <https://www.zynamics.com/bindiff/manual/index.html>`_.

.. include:: ../python-bindiff/README.md
   :parser: myst_parser.sphinx_

------------

API
---

BinDiff
^^^^^^^

.. autoclass:: bindiff.BinDiff
    :members:
    :undoc-members:
    :exclude-members:

BinDiff File
^^^^^^^^^^^^

.. autoclass:: bindiff.file.BindiffFile
    :members:
    :undoc-members:
    :exclude-members:

Types
^^^^^

.. autoclass:: bindiff.file.File
    :members:
    :undoc-members:
    :exclude-members:

.. autoclass:: bindiff.file.FunctionMatch
    :members:
    :undoc-members:
    :exclude-members:

.. autoclass:: bindiff.file.BasicBlockMatch
    :members:
    :undoc-members:
    :exclude-members:


.. automodule:: bindiff.types
    :members:
    :show-inheritance:
    :undoc-members:
    :exclude-members:
