# Sphinx documentation starter
# See docs/11-15.md for setup details
project = 'MyProject'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))
