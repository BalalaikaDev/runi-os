"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.wigle import ...` imports keep working unchanged.
"""
from osintkit.sources.wigle import (enrich_wifi_wigle)

__all__ = ["enrich_wifi_wigle"]
