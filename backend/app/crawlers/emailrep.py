"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.emailrep import ...` imports keep working unchanged.
"""
from osintkit.sources.emailrep import (check_email_rep)

__all__ = ["check_email_rep"]
