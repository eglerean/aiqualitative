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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'AI for Qualitative Data Analysis'
copyright = '2024, Enrico Glerean. Book is distributed under CC-BY-SA license.'
author = 'Enrico Glerean'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser',
	'sphinx_tabs.tabs',
	'sphinxcontrib.mermaid'
]


myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "linkify",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_inline",
    "attrs_block"
]

#myst_enable_extensions = [
#    "dollarmath",
#    "amsmath",
#    "deflist",
    # "html_admonition",
    # "html_image",
#    "colon_fence",
    # "smartquotes",
    # "replacements",
    # "linkify",
    # "substitution",
#]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/tweaks.css']

html_theme_options = {
    "repository_url": "https://github.com/eglerean/aiqualitative/",
    "path_to_docs": "doc/",
    # "use_repository_button": True,
    "use_edit_page_button": True,
    "use_source_button": True,
    "use_issues_button": True,
    # "use_repository_button": True,
    "use_download_button": True,
    "use_sidenotes": True,
    "show_toc_level": 2,
    "announcement": (
        "⚠️Work in progress! Help me!⚠️"
    ),
    #"logo": {
    #    "image_dark": "_static/logo-wide-dark.svg",
    #    # "text": html_title,  # Uncomment to try text with logo
    #},
}

html_logo = "img/AIforqual.png"
html_title = "AI for Qualitatie Data Analysis"

