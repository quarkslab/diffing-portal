Bindiff
=======

`BinDiff <https://www.zynamics.com/bindiff.html>`_ is one of the oldest and most
widely used differ in the reverse engineering community. First developed at Zynamics,
it was then acquired by Google. This differ is based on properties of CallGraph to
establish matches between functions of two binaries. For more details about BinDiff
heuristics, have a look at `one the first paper <https://static.googleusercontent.com/media/www.zynamics.com/en//downloads/bindiffsstic05-1.pdf>`_
or the `documentation <https://www.zynamics.com/bindiff/manual/index.html>`_.


**Limitations**:
Bindiff has primarily been designed to be used using the main Java GUI application. A diff can be triggered
using using command line, but no API has been implemented to trigger a diff programatically. Similarly,
no API enables manipulating the diff result itself.

As such, `python-bindiff <https://github.com/quarkslab/python-bindiff>`_ has been developed to provide a
Python API enabling triggering a diff and manipulating its content.

------------

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
