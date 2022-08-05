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

project = 'Strøm'
copyright = '2022, Lyd by Dissing ApS'
author = 'Tue S. Dissing'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'rst2pdf.pdfbuilder',
    'sphinx_charts.charts',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'sphinx-favicon',
    'sphinxcontrib.youtube',
    'sphinx_panels',
    'myst_parser',
    'sphinxemoji.sphinxemoji',
    'sphinx_last_updated_by_git',
    'sphinx_github_changelog',
]

sphinxemoji_style = 'twemoji'
source_suffix = ['.rst', '.md']

# Display todos by setting to True
todo_include_todos = True

# Make sure the target is unique
autosectionlabel_prefix_document = True

# Adding support for generating PDF documents
pdf_documents = [('index', u'rst2pdf', u'Sample rst2pdf doc', u'Lyd by Dissing'),]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []





## Toolbox options
#github_username = 'LydByDissing'
#github_repository = 'stroem'

# Provide a GitHub API token:
# Pass the SPHINX_GITHUB_CHANGELOG_TOKEN environment variable to your build
# OR
sphinx_github_changelog_token = "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"



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Adding logo
html_logo = "_static/logo.svg"
html_theme_options = {
    'logo_only': False,
    'display_version': True,
}

favicons = [
    {
        "rel": "icon",
        "static-file": "favicon.ico",  # => use `_static/icon.svg`
        "type": "image/x-icon",
    },
    {
        "rel": "icon",
        "sizes": "16x16",
        "href": "/_static/favicon-16x16.png",
        "type": "image/png",
    },
    {
        "rel": "icon",
        "sizes": "32x32",
        "href": "/_static/favicon-32x32.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "/_static/apple-touch-icon.png",
        "type": "image/png",
    },
    {
        "rel": "android-chrome-192x192",
        "sizes": "180x180",
        "href": "/_static/android-chrome-192x192.png",
        "type": "image/png",
    },
    {
        "rel": "android-chrome-512x512",
        "sizes": "180x180",
        "href": "/_static/android-chrome-512x512.png",
        "type": "image/png",
    }
]
