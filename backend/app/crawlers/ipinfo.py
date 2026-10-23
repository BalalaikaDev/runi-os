"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.ipinfo import ...` imports keep working unchanged.
"""
from osintkit.sources.ipinfo import (enrich_ip_ipinfo)

__all__ = ["enrich_ip_ipinfo"]
