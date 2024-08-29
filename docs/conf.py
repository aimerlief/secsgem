# -*- coding: utf-8 -*-
#
# secsgem documentation build configuration file, created by
# sphinx-quickstart on Tue Apr 28 17:32:23 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import os.path
import pathlib

html_theme = 'sphinx_rtd_theme'

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "extensions")))

config_path = pathlib.Path(__file__).parent.resolve()

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'myst_parser',
    'py_exec',
    'sphinx_autodoc_typehints',
    'sphinxcontrib.plantuml'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'secsgem'
copyright = u'2015-2024, Benjamin Parzella'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0'
# The full version, including alpha/beta/rc tags.
release = '0.2.0-rc.1'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

autodoc_default_flags = ["members", "undoc-members", "show-inheritance", "inherited-members"]
autodoc_member_order = "bysource"

plantuml_path = config_path / "bin" / "plantuml.jar"
plantuml = f"java -jar {plantuml_path}"

myst_heading_anchors = 3
# -- Options for HTML output ----------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'secsgemdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'secsgem.tex', u'secsgem Documentation',
   u'Benjamin Parzella', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'secsgem', u'secsgem Documentation',
     [u'Benjamin Parzella'], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'secsgem', u'secsgem Documentation',
   u'Benjamin Parzella', 'secsgem', 'One line description of project.',
   'Miscellaneous'),
]
