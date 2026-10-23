"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.torbot import ...` imports keep working unchanged.
"""
from osintkit.sources.torbot import (crawl_onion_torbot)

__all__ = ["crawl_onion_torbot"]
