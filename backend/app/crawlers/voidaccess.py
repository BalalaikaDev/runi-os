"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.voidaccess import ...` imports keep working unchanged.
"""
from osintkit.sources.voidaccess import (crawl_voidaccess)

__all__ = ["crawl_voidaccess"]
