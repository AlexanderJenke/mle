"""
This setup file makes the package available to other projects
"""

import os

import sys

if __name__ == '__main__':
    """
    Creates a softlink to this package in the latest python site-package path.
    """
    os.system(f"ln -sf -t {sys.path[-1]} $(pwd)")
