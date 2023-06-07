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
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('idascript'))
sys.path.insert(0, os.path.abspath('python-binexport'))
sys.path.insert(0, os.path.abspath('python-bindiff'))

# -- Project information -----------------------------------------------------

project = 'Diffing Portal'
copyright = ''
author = 'Quarkslab'

# The full version, including alpha/beta/rc tags
release = '0.2'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'  # also monokai, friendly, colorful


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.imgmath',
    'sphinxcontrib.bibtex'
    "enum_tools.autoenum",
    'sphinx_fontawesome',
    "nbsphinx"
]

bibtex_bibfiles = ['refs.bib']

myst_enable_extensions = ["colon_fence", "dollarmath"]

autosummary_generate = True
autoclass_content = "class"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["idascript/idascript/*"]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# ~ autodoc_type_aliases = {
    # ~ 'Graph': 'qbindiff.abstract.GenericGraph',
    # ~ 'qbindiff.types.Graph': 'qbindiff.abstract.GenericGraph',
    # ~ 'qbindiff.Graph': 'qbindiff.abstract.GenericGraph',
# ~ }


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material' #'sphinx_rtd_theme', "sphinx_book_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'style.css',
]

html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]  # Somehow make appearing sidebar
}


# Set link name generated in the top bar.
html_title = 'Diffing Portal'

# Material theme options (see theme.conf for more information)
html_theme_options = {
    "base_url": "https://quarkslab.gitlab.io/diffing-portal",
    "repo_url": "",  # At the top right (with badges)
    "repo_name": "Diffing Portal",
    "google_analytics_account": "UA-XXXXX",
    "html_minify": False,
    "html_prettify": True,
    "css_minify": True,
    "logo_icon": "&#xe869",
    "repo_type": "github",
    "globaltoc_depth": 3,
    "color_primary": "#4051b5",
    "color_accent": "#d8f32a",#"#566df3",
    "touch_icon": "logo2.png",
    "theme_color": "#4051b5",
    "master_doc": False,
    # "nav_links": [
    #     {"href": "index", "internal": True, "title": "QBindiff++"},
    #     {
    #         "href": "https://squidfunk.github.io/mkdocs-material/",
    #         "internal": False,
    #         "title": "QBindiff--",
    #     },
    # ],

    # Text written betwen top bar and nav bar
    # "heroes": {
    #     "index": "A responsive Material Design theme for Sphinx sites.",
    #     "customization": "Configuration options to personalize your site.",
    # },

    # Versions infos
    # "version_dropdown": False,  # Version dropdown at the top right
    # "version_json": "_static/versions.json",
    # "version_info": {
    #     "Release": "https://bashtage.github.io/sphinx-material/",
    #     "Development": "https://bashtage.github.io/sphinx-material/devel/",
    #     "Release (rel)": "/sphinx-material/",
    #     "Development (rel)": "/sphinx-material/devel/",
    # },

    "table_classes": ["plain"],
}
