"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.hunter import ...` imports keep working unchanged.
"""
from osintkit.sources.hunter import (hunt_domain_emails)

__all__ = ["hunt_domain_emails"]
