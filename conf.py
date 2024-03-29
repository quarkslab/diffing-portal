# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# -- Project information -----------------------------------------------------

project = "Diffing Portal"
copyright = "2023 Quarkslab"
author = "Quarkslab"

# The full version, including alpha/beta/rc tags
release = "0.2"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = "en"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "default"  # also monokai, friendly, colorful


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.imgmath",
    "sphinxcontrib.bibtex",
    "enum_tools.autoenum",
    "sphinx_fontawesome",
    "nbsphinx",
]

bibtex_bibfiles = ["refs.bib"]

myst_enable_extensions = ["colon_fence", "dollarmath"]

autosummary_generate = True
autoclass_content = "both"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

source_suffix = [".rst"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "qbindiff/doc/source/basicex.rst",
    "qbindiff/doc/source/documentation.rst",
    "qbindiff/doc/source/index.rst",
    "qbindiff/doc/source/tutorial.rst",
]

include_patterns = [
    "index.rst",
    "exporter/*",
    "differs/*",
    "tutorials/*",
    "resources/*",
    "tools/*",
    "qbindiff/doc/source/**",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "networkx": ("https://networkx.org/documentation/stable/", None),
    "quokka": ("https://quarkslab.github.io/quokka/", None),
}

autodoc_typehints_format = "short"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "insipid"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ["style.css", "https://netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

html_show_sourcelink = True

# Set link name generated in the top bar.
html_title = "Diffing Portal"
