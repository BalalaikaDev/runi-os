"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.maritime import ...` imports keep working unchanged.
"""
from osintkit.sources.maritime import (track_vessel)

__all__ = ["track_vessel"]
