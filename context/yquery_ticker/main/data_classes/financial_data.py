from dataclasses import dataclass

from context.yquery_ticker.main.const import DEFAULT_CASH_FLOW_METRIC
from context.yquery_ticker.main.enums.cash_flow_type import CashFlowType

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
    free_cash_flow: float
    operating_cash_flow: float
    enterprise_to_ebitda: float
    price_to_book: float
    price_to_earnings: PriceToEarnings
    earnings_per_share: EarningsPerShare
    enterprise_to_revenue: float
    return_on_equity: float
    return_on_assets: float
    net_income_to_common: float
    book_value: float

    def apply_local_rules(self):
        if self.total_debt < 0:
            self.total_debt = None

    def get_cash_flow(self, cash_flow_type: CashFlowType = DEFAULT_CASH_FLOW_METRIC):
        if cash_flow_type == CashFlowType.FREE_CASH_FLOW:
            return self.free_cash_flow
        elif cash_flow_type == CashFlowType.OPERATING_CASH_FLOW:
            return self.operating_cash_flow
        return None

    def set_cash_flow(self, cash_flow, cash_flow_type: CashFlowType = DEFAULT_CASH_FLOW_METRIC):
        if cash_flow_type == CashFlowType.FREE_CASH_FLOW:
            self.free_cash_flow = cash_flow
        elif cash_flow_type == CashFlowType.OPERATING_CASH_FLOW:
            self.operating_cash_flow = cash_flow

    def calculate_price_to_cashflow(self):
        cash_flow = self.get_cash_flow()
        if self.price is not None and cash_flow is not None:
            if float(cash_flow) != 0.0:
                return self.price / cash_flow
        return None

    def calculate_return_on_invested_capital(self):
        if (
            self.net_income_to_common is not None
            and self.book_value is not None
            and self.total_debt is not None
        ): 
            numerator = self.book_value + self.total_debt
            if  numerator != 0:
                return self.net_income_to_common / numerator
         
        return None

    @classmethod
    def mockk(cls):
        return FinancialData(
            price=0,
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
            free_cash_flow=0,
            operating_cash_flow=0,
            enterprise_to_ebitda=0,
            price_to_book=0,
            price_to_earnings=None,
            earnings_per_share=None,
            enterprise_to_revenue=0,
            return_on_equity=0,
            return_on_assets=0,
            net_income_to_common=0,
            book_value=0
        )
