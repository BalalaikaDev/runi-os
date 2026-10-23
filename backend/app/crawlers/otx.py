"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.otx import ...` imports keep working unchanged.
"""
from osintkit.sources.otx import (enrich_otx)

__all__ = ["enrich_otx"]
