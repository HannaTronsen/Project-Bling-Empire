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

    @classmethod
    def mockk(cls):
        return GeneralStockInfo(
            ticker= 'aapl',
            company_name='Apple Inc',
            country=Country.US,
            industry='Computer',
            sector='Electronics',
            website='apple.com',
            long_business_summary='Long summary',
            financial_summary=None
        )

    