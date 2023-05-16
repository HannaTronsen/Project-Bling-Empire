from dataclasses import dataclass
from .iterable_data import IterableDataInterface


@dataclass
class PriceToEarnings(IterableDataInterface):
    trailing_pe: float
    forward_pe: float

@dataclass
class EarningsPerShare(IterableDataInterface):
    trailing_eps: float
    forward_eps: float

@dataclass
class FinancialData(IterableDataInterface):
    price: float
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
    cash_flow: float
    enterprise_to_ebitda: float
    price_to_book: float
    price_to_earnings: PriceToEarnings
    earnings_per_share: EarningsPerShare
    enterprise_to_revenue: float

    def apply_local_rules(self):
        if self.total_debt < 0:
            self.total_debt = None

    def calculate_price_to_cashflow(self): 
        if self.price is not None and self.cash_flow is not None:
            if float(self.cash_flow) != 0.0:
                return self.price / self.cash_flow
        return None
        

    @classmethod
    def mockk(cls):
        return FinancialData(
            price = 0,
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
            trailing_annual_dividend_yield=0,
            cash_flow=0,
            enterprise_to_ebitda=0,
            price_to_book=0,
            price_to_earnings = None,
            earnings_per_share = None,
            enterprise_to_revenue=0
        )
