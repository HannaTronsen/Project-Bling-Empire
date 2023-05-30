from dataclasses import dataclass
from context.yquery_ticker.main.classes.historical_earnings import HistoricalEarnings

from context.yquery_ticker.main.const import DEFAULT_CASH_FLOW_METRIC
from context.yquery_ticker.main.classes.castable_data import CastableDataInterface
from context.yquery_ticker.main.data_classes.expenses import Expenses
from context.yquery_ticker.main.enums.cash_flow_type import CashFlowType
from ..classes.iterable_data import IterableDataInterface


@dataclass
class PriceToEarnings(IterableDataInterface, CastableDataInterface):
    trailing_pe: float
    forward_pe: float


@dataclass
class EarningsPerShare(IterableDataInterface, CastableDataInterface):
    trailing_eps: float
    forward_eps: float


@dataclass
class FinancialData(IterableDataInterface, CastableDataInterface):
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
    net_income_to_common: float  # net earnings
    earnings_growth: float
    book_value: float
    expenses: Expenses
    historical_earnings: HistoricalEarnings

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
            if numerator != 0:
                return self.net_income_to_common / numerator

        return None

    def calculate_return_on_investment(self):
        if (
            self.net_income_to_common is not None
            and self.expenses.check_has_invalid_value(
                [
                    self.expenses.capital_expenditure,
                    self.expenses.interest_expense,
                    self.expenses.interest_expense_non_operating,
                    self.expenses.total_other_finance_cost
                ]
            ) == False
        ):
            sum_expenses = self.expenses.sum()
            if(sum_expenses != 0):
                return self.net_income_to_common / (sum_expenses * 100)

        return False

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
            earnings_growth=0,
            book_value=0,
            expenses=None,
            historical_earnings=None
        )
