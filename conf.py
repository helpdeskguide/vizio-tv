# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Set Up Your VIZIO TV'
copyright = '2025, VIZIO'
author = 'VIZIO'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Extensions
extensions = []

# Templates path
templates_path = ['_templates']

# List of patterns to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "Set Up Your VIZIO TV at vizio.com/setup – Step-by-Step Guide"

# Optional short title (e.g., for nav bar)
html_short_title = "VIZIO Setup Guide"

# Favicon (place favicon.ico in the root or _static folder if available)
html_favicon = 'favicon.ico'

# Choose a theme (uncomment and install if desired)
# html_theme = 'sphinx_rtd_theme'
html_theme = 'alabaster'  # Default theme; change as needed

# Hide "View page source" from HTML output
html_show_sourcelink = False

# Allow raw HTML in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
    'description': 'Step-by-step instructions to activate your VIZIO Smart TV at vizio.com/setup',
}

# Paths to static files like stylesheets or images
# Uncomment if you have static assets like logo or favicon
# html_static_path = ['_static']
