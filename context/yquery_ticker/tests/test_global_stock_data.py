import unittest
from typing import Optional, Type
from context.yquery_ticker.main.classes.historical_earnings_data import HistoricalEarningsData
from context.yquery_ticker.main.classes.global_stock_data import GlobalStockDataClass
from context.yquery_ticker.main.data_classes.expenses import Expenses, ExpensesFields
from context.yquery_ticker.main.data_classes.financial_data import EarningsPerShare, FinancialData, PriceToEarnings
from context.yquery_ticker.main.data_classes.financial_summary import FinancialSummary
from context.yquery_ticker.main.data_classes.general_stock_info import GeneralStockInfo
from context.yquery_ticker.main.enums.cash_flow_type import CashFlowType
from context.yquery_ticker.main.errors.generic_error import GenericError


class test_global_stock_data(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_global_stock_data, self).__init__(*args, **kwargs)

    def setUp(self):
        self.mockStock = GlobalStockDataClass(ticker_symbol="aapl")
        self.mockStock.general_stock_info = GeneralStockInfo.mockk()
        self.mockStock.financial_data = FinancialData.mockk()
        self.mockStock.earnings_and_earnings_history = HistoricalEarningsData.mockk()

    @staticmethod
    def assert_price_to_cash_flow(
            stock: FinancialData,
            price: Optional[float],
            cash_flow: Optional[float],
            expected: Optional[float]
    ):
        stock.price = price
        stock.set_cash_flow(cash_flow=cash_flow)
        assert stock.calculate_price_to_cashflow() == expected

    @staticmethod
    def assert_return_on_invested_capital(
            stock: FinancialData,
            net_income_to_common: Optional[float],
            book_value: Optional[float],
            total_debt: Optional[float],
            expected: Optional[float]
    ):
        stock.net_income_to_common = net_income_to_common
        stock.book_value = book_value
        stock.total_debt = total_debt
        result = stock.calculate_return_on_invested_capital()

        if result is not None:
            assert round(result, 2) == expected
        else:
            assert result == expected

    @staticmethod
    def assert_return_on_investment(
            financial_data: FinancialData,
            expenses: Expenses,
            expected: Optional[float | Type[GenericError]]
    ):
        financial_data.net_income_to_common = 100
        financial_data.expenses = expenses
        result = financial_data.calculate_return_on_investment()

        if not isinstance(result, GenericError):
            assert round(result, 2) == expected
        else:
            isinstance(result, expected)

    def test_general_stock_info(self):
        self.mockStock.general_stock_info = GeneralStockInfo(
            ticker='aapl',
            company='Apple Inc',
            country=None,  # type: ignore
            industry='Consumer Electronics',
            sector='Technology',
            website='https://www.apple.com',
            long_business_summary='N/A',
            financial_summary=FinancialSummary(
                previous_close=None,
                open=0.0,
                dividend_rate="",  # type: ignore
                beta=0.0,
                price_to_earnings=PriceToEarnings(
                    trailing_pe=0.0,
                    forward_pe=0.0,
                ),
                market_cap="N/A",  # type: ignore
                currency="N/A"  # type: ignore
            )
        ).normalize_values()

        self.assertIsNone(self.mockStock.general_stock_info.country)
        self.assertIsNone(self.mockStock.general_stock_info.long_business_summary)
        self.assertIsNone(self.mockStock.general_stock_info.financial_summary.previous_close)
        self.assertIsNone(self.mockStock.general_stock_info.financial_summary.market_cap)
        self.assertIsNone(self.mockStock.general_stock_info.financial_summary.currency)
        self.assertIsNone(self.mockStock.general_stock_info.financial_summary.dividend_rate)

    def test_financial_data(self):
        self.mockStock.financial_data = FinancialData(
            price=10,
            total_revenue=0.00000,
            revenue_per_share="",  # type: ignore
            revenue_growth="N/A",  # type: ignore
            total_debt=-1,
            debt_to_equity=0,
            profit_margins=3,
            gross_profit_margins="N/A",  # type: ignore
            operating_margins=None,
            dividend_rate=0,
            dividend_yield=0,
            five_year_avg_dividend_yield=0,
            trailing_annual_dividend_rate=0,
            trailing_annual_dividend_yield=0,
            free_cash_flow=0,
            operating_cash_flow=0,
            enterprise_to_ebitda=0,
            price_to_book=0,
            return_on_assets=0,
            return_on_equity=0,
            net_income_to_common=0,
            earnings_growth=0,
            book_value=0,
            price_to_earnings=PriceToEarnings(
                trailing_pe="N/A",  # type: ignore
                forward_pe=2
            ),
            earnings_per_share=EarningsPerShare(
                trailing_eps=2,
                forward_eps="N/A"  # type: ignore
            ),
            enterprise_to_revenue=0,
            expenses=None
        ).normalize_values()

        self.assertIsNone(self.mockStock.financial_data.revenue_per_share)
        self.assertIsNone(self.mockStock.financial_data.revenue_growth)
        self.assertIsNone(self.mockStock.financial_data.total_debt)
        self.assertIsNone(self.mockStock.financial_data.total_debt)
        self.assertIsNone(self.mockStock.financial_data.gross_profit_margins)
        self.assertIsNone(self.mockStock.financial_data.operating_margins)
        self.assertIsNone(self.mockStock.financial_data.price_to_earnings.trailing_pe)
        self.assertIsNone(self.mockStock.financial_data.earnings_per_share.forward_eps)
        self.assertIsNone(self.mockStock.financial_data.expenses)

    def test_calculate_price_to_cashflow(self):
        self.assert_price_to_cash_flow(stock=self.mockStock.financial_data, price=None, cash_flow=10, expected=None)
        self.assert_price_to_cash_flow(stock=self.mockStock.financial_data, price=10, cash_flow=None, expected=None)
        self.assert_price_to_cash_flow(stock=self.mockStock.financial_data, price=100.0, cash_flow=10.0, expected=10.0)
        self.assert_price_to_cash_flow(stock=self.mockStock.financial_data, price=0.0, cash_flow=10.0, expected=0.0)
        self.assert_price_to_cash_flow(stock=self.mockStock.financial_data, price=0.0, cash_flow=0.0, expected=None)
        self.assert_price_to_cash_flow(stock=self.mockStock.financial_data, price=100.0, cash_flow=-10.0, expected=-10)
        self.assert_price_to_cash_flow(stock=self.mockStock.financial_data, price=-100.0, cash_flow=10.0, expected=-10)
        self.assert_price_to_cash_flow(stock=self.mockStock.financial_data, price=-100.0, cash_flow=-10.0, expected=10)
        self.assert_price_to_cash_flow(stock=self.mockStock.financial_data, price=100.0, cash_flow=10.0, expected=10.0)

    def test_get_and_set_cash_flow(self):
        self.mockStock.financial_data.free_cash_flow = 10
        self.mockStock.financial_data.set_cash_flow(cash_flow=100, cash_flow_type=CashFlowType.OPERATING_CASH_FLOW)
        assert self.mockStock.financial_data.get_cash_flow(
            cash_flow_type=CashFlowType.OPERATING_CASH_FLOW) == self.mockStock.financial_data.operating_cash_flow

        self.mockStock.financial_data.operating_cash_flow = 100
        self.mockStock.financial_data.set_cash_flow(cash_flow=100, cash_flow_type=CashFlowType.FREE_CASH_FLOW)
        assert self.mockStock.financial_data.get_cash_flow(
            cash_flow_type=CashFlowType.FREE_CASH_FLOW) == self.mockStock.financial_data.free_cash_flow

    def test_calculate_return_on_investments(self):
        self.assert_return_on_invested_capital(
            stock=self.mockStock.financial_data,
            net_income_to_common=1000,
            book_value=2000,
            total_debt=1000,
            expected=0.33
        )
        self.assert_return_on_invested_capital(
            stock=self.mockStock.financial_data,
            net_income_to_common=0,
            book_value=2000,
            total_debt=1000,
            expected=0.0
        )
        self.assert_return_on_invested_capital(
            stock=self.mockStock.financial_data,
            net_income_to_common=1000,
            book_value=0,
            total_debt=0,
            expected=None
        )
        self.assert_return_on_invested_capital(
            stock=self.mockStock.financial_data,
            net_income_to_common=0,
            book_value=0,
            total_debt=0,
            expected=None
        )
        self.assert_return_on_invested_capital(
            stock=self.mockStock.financial_data,
            net_income_to_common=None,
            book_value=None,
            total_debt=None,
            expected=None
        )
        self.assert_return_on_invested_capital(
            stock=self.mockStock.financial_data,
            net_income_to_common=-1000,
            book_value=2000,
            total_debt=1000,
            expected=-0.33
        )
        self.assert_return_on_invested_capital(
            stock=self.mockStock.financial_data,
            net_income_to_common=1000,
            book_value=2000,
            total_debt=-1000,
            expected=1.00
        )

    def test_calculate_return_on_investment(self):
        self.assert_return_on_investment(
            financial_data=self.mockStock.financial_data,
            expenses=Expenses(
                capital_expenditure=0,
                interest_expense=None,
                interest_expense_non_operating=0,
                total_other_finance_cost=0
            ),
            expected=GenericError
        )
        self.assert_return_on_investment(
            financial_data=self.mockStock.financial_data,
            expenses=Expenses(
                capital_expenditure=0,
                interest_expense=0,
                interest_expense_non_operating=0,
                total_other_finance_cost=0
            ),
            expected=GenericError
        )
        self.assert_return_on_investment(
            financial_data=self.mockStock.financial_data,
            expenses=Expenses(
                capital_expenditure=0,
                interest_expense=1,
                interest_expense_non_operating=0,
                total_other_finance_cost=0
            ),
            expected=1.0
        )
        self.assert_return_on_investment(
            financial_data=self.mockStock.financial_data,
            expenses=Expenses(
                capital_expenditure=1,
                interest_expense=1,
                interest_expense_non_operating=0,
                total_other_finance_cost=0
            ),
            expected=0.5
        )
        self.assert_return_on_investment(
            financial_data=self.mockStock.financial_data,
            expenses=Expenses(
                capital_expenditure=-1,
                interest_expense=-1,
                interest_expense_non_operating=0,
                total_other_finance_cost=0
            ),
            expected=-0.5
        )

    def test_sum_expenses(self):
        assert Expenses(
            capital_expenditure=1,
            interest_expense=0,
            interest_expense_non_operating=0,
            total_other_finance_cost=0
        ).sum() == 1
        assert Expenses(
            capital_expenditure=1,
            interest_expense=-2,
            interest_expense_non_operating=0,
            total_other_finance_cost=0
        ).sum() == -1
        assert Expenses(
            capital_expenditure=1,
            interest_expense=1,
            interest_expense_non_operating=2,
            total_other_finance_cost=0
        ).sum(exclude=[ExpensesFields.INTEREST_EXPENSE_NON_OPERATING]) == 2
        assert Expenses(
            capital_expenditure=1,
            interest_expense=1,
            interest_expense_non_operating=3,
            total_other_finance_cost=2
        ).sum(exclude=[ExpensesFields.TOTAL_OTHER_FINANCE_COST]) == 5

    def test_type_checking(self):
        expenses: Expenses = Expenses(
            capital_expenditure=1.0,
            interest_expense="1.01",  # type: ignore
            interest_expense_non_operating="Zero",  # type: ignore
            total_other_finance_cost=None
        ).normalize_values()

        self.assertIsNotNone(expenses.interest_expense)
        assert expenses.interest_expense == 1.01
        self.assertIsNone(expenses.interest_expense_non_operating)
        self.assertIsNone(expenses.total_other_finance_cost)

        financial_data = FinancialData(
            price=10,
            total_revenue=0.00000,
            revenue_per_share="",  # type: ignore
            revenue_growth="N/A",  # type: ignore
            total_debt=-1,
            debt_to_equity=0,
            profit_margins=3,
            gross_profit_margins="n/a",  # type: ignore
            operating_margins=None,
            dividend_rate=0,
            dividend_yield=0,
            five_year_avg_dividend_yield=0,
            trailing_annual_dividend_rate=0,
            trailing_annual_dividend_yield=0,
            free_cash_flow=0,
            operating_cash_flow=0,
            enterprise_to_ebitda=0,
            price_to_book=0,
            return_on_assets=0,
            return_on_equity=0,
            net_income_to_common=0,
            earnings_growth=0,
            book_value=0,
            price_to_earnings=PriceToEarnings(
                trailing_pe="N/A",  # type: ignore
                forward_pe="2.0"  # type: ignore
            ),
            earnings_per_share=EarningsPerShare(
                trailing_eps=10,
                forward_eps="Test"  # type: ignore
            ),
            enterprise_to_revenue=10,
            expenses=None,
        ).normalize_values()

        assert financial_data.price_to_earnings.forward_pe == 2.0
        assert financial_data.earnings_per_share.trailing_eps == 10.0
        self.assertIsNone(financial_data.price_to_earnings.trailing_pe)
        self.assertIsNone(financial_data.gross_profit_margins)
        self.assertIsNone(financial_data.earnings_per_share.forward_eps)

        self.mockStock.financial_data.price = "10"
        self.mockStock.financial_data.five_year_avg_dividend_yield = "n/a"
        self.mockStock.financial_data.debt_to_equity = "Test"
        self.mockStock.financial_data.normalize_values()

        assert self.mockStock.financial_data.price == 10.0
        self.assertIsNone(self.mockStock.financial_data.five_year_avg_dividend_yield)
        self.assertIsNone(self.mockStock.financial_data.debt_to_equity)
