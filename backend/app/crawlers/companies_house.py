"""Compatibility shim — the implementation of this source now lives in the
standalone `osintkit` package (https://github.com/BalalaikaDev/osintkit),
extracted from runi-os. This module re-exports it so existing
`from crawlers.companies_house import ...` imports keep working unchanged.
"""
from osintkit.sources.companies_house import (search_companies_house,companies_house_company)

__all__ = ["search_companies_house", "companies_house_company"]
