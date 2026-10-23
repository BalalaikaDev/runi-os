"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.reddit import ...` imports keep working unchanged.
"""
from osintkit.sources.reddit import (reddit_search,reddit_user)

__all__ = ["reddit_search", "reddit_user"]
