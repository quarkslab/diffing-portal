==============
Diffing Portal
==============

Introduction
------------

This portal aims to provide user-friendly resources on binary diffing. Binary diffing is a central topic in reverse-engineering but contents tend to be widespread among different tools, websites, frameworks. This portal tries to centralize the most well-known diffing tools that are used in industry with easy-to-use python packages. 

Binary diffing is usually performed between two binaries, one primary and one secondary, but diffing these binaries and evaluating the diff result is usually a complicated task. The goal of this portal is to automate as much as possible the diffing, in order to make the work of reverse-engineers easier. 

In this website, you could find in particular : 

- binary exporters : to diff two binaries, using directly executables is not feasible. It requires to use some exporters, that will translate the binary to some kind of protobuf format file. This file will then be used for diffing. We support BinExport and Quokka. 

- differs : there is a wide range of differs, some of them being widely used in industry, others that come from an academic background. We support the two most famous industrial differs, BinDiff and Diaphora. Plus, we opensource the Quarkslab differ, QBinDiff. 

- tutorials : binary diffing could be tought for beginners (and even for reverse-engineers). We provide different tutorials to show how to use the tools of this portal, as well as realistic user-cases.

- additional resources : binary diffing is essential in reverse-engineering and a lot of tools, resources, academic publications are available online. We try to maintain a state-of-the-art list of academic publications and ressources and this subject. 


.. toctree::
    :caption: Exporters
    :maxdepth: 2
    :hidden:

    exporter/binexport
    exporter/quokka

Qbindiff
--------

.. toctree::
    :caption: Qbindiff
    :maxdepth: 2
    :hidden:

    qbindiff/doc/source/installation
    qbindiff/doc/source/documentation
    qbindiff/doc/source/api/qbindiff
    qbindiff/doc/source/publication



.. toctree::
    :caption: Third-party differs
    :maxdepth: 2
    :hidden:

    other_differ/bindiff
    other_differ/diaphora



Tutorials
---------

.. toctree::
    :caption: Tutorials
    :maxdepth: 2

    tutorials/basic-diffing.rst
    tutorials/using-passes.rst
    tutorials/diffing-obfuscated-binaries.rst


.. toctree::
    :caption: Tools
    :maxdepth: 2
    :hidden:

    idascript/README



.. toctree::
    :caption: Resources
    :maxdepth: 2
    :hidden:

    resources/academia
