"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.geocode import ...` imports keep working unchanged.
"""
from osintkit.sources.geocode import (geocode,reverse_geocode)

__all__ = ["geocode", "reverse_geocode"]
