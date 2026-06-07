"""Utility functions for common list and collection operations."""


def flatten(nested):
    """Return a single flat list from an arbitrarily nested iterable."""
    # TODO: implement recursive flattening that handles any nesting depth
    raise NotImplementedError


def chunk(lst, size):
    """Split lst into successive sublists of length size (last chunk may be smaller)."""
    # TODO: implement chunking; raise ValueError if size < 1
    raise NotImplementedError


def unique_ordered(lst):
    """Return a new list with duplicates removed while preserving insertion order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def frequencies(lst):
    """Return a dict mapping each element to its occurrence count in lst."""
    # TODO: implement element frequency counting
    raise NotImplementedError
