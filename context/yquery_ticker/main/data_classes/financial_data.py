from dataclasses import dataclass
from .iterable_data import IterableDataInterface


@dataclass
class FinancialData(IterableDataInterface):
    total_revenue: float
    revenue_per_share: float
    revenue_growth: float
    total_debt: float
    debt_to_equity: float
    gross_profit_margins: float
    operating_margins: float
    profit_margins: float
    dividend_rate: float
    dividend_yield: float
    five_year_avg_dividend_yield: float
    trailing_annual_dividend_rate: float
    trailing_annual_dividend_yield: float


    def apply_local_rules(self):
        if self.total_debt < 0:
            self.total_debt = None

    @classmethod
    def mockk(cls):
        return FinancialData(
            total_revenue=0,
            revenue_per_share=0,
            revenue_growth=0,
            total_debt=0,
            debt_to_equity=0,
            gross_profit_margins=0,
            operating_margins=0,
            profit_margins=0,
            dividend_rate=0,
            dividend_yield=0,
            five_year_avg_dividend_yield=0,
            trailing_annual_dividend_rate=0,
            trailing_annual_dividend_yield=0
        )
