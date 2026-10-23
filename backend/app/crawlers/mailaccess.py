"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.mailaccess import ...` imports keep working unchanged.
"""
from osintkit.sources.mailaccess import (enrich_email_mailaccess)

__all__ = ["enrich_email_mailaccess"]
