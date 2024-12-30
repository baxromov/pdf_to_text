# -- Project information -----------------------------------------------------

project = 'pdf-text-extractor'
author = 'Shahzod'


# Get the version from _version.py
def get_version(version_file="_version.py"):
    version = {}
    with open(version_file) as f:
        exec(f.read(), version)
    return version['__version__']

version = get_version()
release = version

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',  # For automatic documentation generation from docstrings
    'sphinx.ext.napoleon',  # Support for Google and NumPy style docstrings
    'sphinx.ext.viewcode',  # Add links to the source code in the documentation
    'sphinx.ext.todo',  # Support for TODOs in the documentation
]

# Templates path
templates_path = ['_templates']

# Source file suffixes
source_suffix = '.rst'  # You can use `.md` if you're writing Markdown files

# Master document (default is 'index')
master_doc = 'index'

# Exclude patterns (e.g., files or directories to ignore)
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'  # Or use other themes like 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for LaTeX output -------------------------------------------------
latex_documents = [
    ('index', 'pdf-text-extractor.tex', 'pdf-text-extractor Documentation', 'Shahzod', 'manual'),
]

# -- Autodoc configuration ---------------------------------------------------
autodoc_default_flags = ['members', 'undoc-members', 'private-members', 'show-inheritance']
autodoc_member_order = 'bysource'

# Napoleon settings for Google/NumPy style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
