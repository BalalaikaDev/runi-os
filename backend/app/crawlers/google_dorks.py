"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.google_dorks import ...` imports keep working unchanged.
"""
from osintkit.sources.google_dorks import (run_dork)

__all__ = ["run_dork"]
