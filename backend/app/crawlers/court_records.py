"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.court_records import ...` imports keep working unchanged.
"""
from osintkit.sources.court_records import (search_court_records)

__all__ = ["search_court_records"]
