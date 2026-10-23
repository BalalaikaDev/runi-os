"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.adverse_media import ...` imports keep working unchanged.
"""
from osintkit.sources.adverse_media import (search_adverse_media)

__all__ = ["search_adverse_media"]
