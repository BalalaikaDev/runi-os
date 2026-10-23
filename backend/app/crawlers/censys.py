"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.censys import ...` imports keep working unchanged.
"""
from osintkit.sources.censys import (search_hosts,get_host)

__all__ = ["search_hosts", "get_host"]
