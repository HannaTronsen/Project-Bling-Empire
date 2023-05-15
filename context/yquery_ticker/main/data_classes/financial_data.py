from dataclasses import dataclass
from .iterable_data import IterableDataInterface


@dataclass
class FinancialData(IterableDataInterface):
    total_revenue: float
    revenue_per_share: float
    revenue_growth: float

    @classmethod
    def mockk(cls):
        return FinancialData(
            total_revenue=0,
            revenue_per_share=0,
            revenue_growth=0
        )
