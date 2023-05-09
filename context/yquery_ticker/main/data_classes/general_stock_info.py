from dataclasses import dataclass
from .financial_summary import FinancialSummary
from .iterable_data import IterableDataInterface
from ..enums.country import Country

@dataclass
class GeneralStockInfo(IterableDataInterface):
    ticker: str
    company_name: str
    country: Country
    industry: str
    sector: str
    website: str
    long_business_summary: str
    financial_summary: FinancialSummary

    