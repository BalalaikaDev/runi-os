"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.etherscan import ...` imports keep working unchanged.
"""
from osintkit.sources.etherscan import (trace_eth_address)

__all__ = ["trace_eth_address"]
