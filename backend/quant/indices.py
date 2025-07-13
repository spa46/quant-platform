# indices.py
"""
This module provides access to the global stock indices configuration.
"""
from .global_indices import index_global

def get_global_indices():
    """Return the list of global stock indices."""
    return index_global
