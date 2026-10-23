"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.whois_history import ...` imports keep working unchanged.
"""
from osintkit.sources.whois_history import (get_whois_history)

__all__ = ["get_whois_history"]
