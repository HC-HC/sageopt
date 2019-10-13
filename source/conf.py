# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import inspect

sys.path.insert(0, os.path.abspath('~/documents/research/software/sageopt'))


# -- Project information -----------------------------------------------------

project = 'sageopt'
copyright = '2019, Riley J. Murray'
author = 'Riley J. Murray'

# The full version, including alpha/beta/rc tags
release = '0.4.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
    # 'sphinx.ext.imgmath'
]


def autodoc_skip_member(app, what, name, obj, skip, options):
    exclusions = ('__weakref__',  # special-members
                  '__doc__', '__module__', '__dict__',  # undoc-members
                  )
    if inspect.ismethod(obj) or inspect.isfunction(obj):
        func_name = obj.__qualname__
        # exclusions for Variable objects
        if func_name in {'Variable.is_constant', 'Variable.is_affine'}:
            return True
        if func_name in {'Expression.as_expr'}:
            return True

    exclude = name in exclusions
    return skip or exclude


def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)


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
html_theme = 'alabaster'

# https://alabaster.readthedocs.io/en/latest/customization.html#theme-options
html_theme_options = {
    'github_user': 'rileyjmurray',
    'github_repo': 'sageopt',
    'body_text_align': 'justify',
    'fixed_sidebar': 'true',
    'page_width': '1000px'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']