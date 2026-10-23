"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.wikidata import ...` imports keep working unchanged.
"""
from osintkit.sources.wikidata import (lookup_wikidata)

__all__ = ["lookup_wikidata"]
