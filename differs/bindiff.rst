Bindiff
=======

`BinDiff <https://www.zynamics.com/bindiff.html>`_ is the oldest and most widely used differ in the reverse engineering community. First conceived at Zynamics, it was then sold to Google. This differ is based on properties of CallGraph to establish matches between functions of two binaries. For more details about BinDiff heuristics, have a look at `one the first paper<https://static.googleusercontent.com/media/www.zynamics.com/en//downloads/bindiffsstic05-1.pdf>`_ about it 

------------

.. include:: ../python-bindiff/README.md
   :parser: myst_parser.sphinx_

------------

API
---

BinDiff
~~~~~~~

.. autoclass:: bindiff.BinDiff
    :members:
    :undoc-members:
    :exclude-members:

BinDiff File
~~~~~~~~~~~~

.. automodule:: bindiff.file
    :members:
    :undoc-members:
    :exclude-members:

Types
~~~~~

.. automodule:: bindiff.types
    :members:
    :show-inheritance:
    :undoc-members:
    :exclude-members:
