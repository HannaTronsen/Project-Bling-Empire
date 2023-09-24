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
        self.general_stock_info = GeneralStockInfo.mockk()
        self.financial_data = FinancialData.mockk()
        self.earnings_and_earnings_history = HistoricalEarningsData.mockk()

    @staticmethod
    def assert_price_to_cash_flow(
            financial_data: FinancialData,
            price: Optional[float],
            cash_flow: Optional[float],
            expected: Optional[float]
    ):
        financial_data.price = price
        financial_data.set_cash_flow(cash_flow=cash_flow)
        assert financial_data.calculate_price_to_cashflow() == expected

    @staticmethod
    def assert_return_on_invested_capital(
            financial_data: FinancialData,
            net_income_to_common: Optional[float],
            book_value: Optional[float],
            total_debt: Optional[float],
            expected: Optional[float]
    ):
        financial_data.net_income_to_common = net_income_to_common
        financial_data.book_value = book_value
        financial_data.total_debt = total_debt
        result = financial_data.calculate_return_on_invested_capital()

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
        general_stock_info = GeneralStockInfo(
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

        test_cases = [
            general_stock_info.country,
            general_stock_info.long_business_summary,
            general_stock_info.financial_summary.previous_close,
            general_stock_info.financial_summary.market_cap,
            general_stock_info.financial_summary.currency,
            general_stock_info.financial_summary.dividend_rate
        ]

        for test_case in test_cases:
            self.assertIsNone(test_case)

    def test_financial_data(self):
        financial_data = FinancialData(
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

        test_cases = [
            financial_data.revenue_per_share,
            financial_data.revenue_growth,
            financial_data.total_debt,
            financial_data.total_debt,
            financial_data.gross_profit_margins,
            financial_data.operating_margins,
            financial_data.price_to_earnings.trailing_pe,
            financial_data.earnings_per_share.forward_eps,
            financial_data.expenses
        ]

        for test_case in test_cases:
            self.assertIsNone(test_case)

    def test_calculate_price_to_cashflow(self):
        test_cases = [
            # price, cash flow, expected
            (None, 10, None),
            (10, None, None),
            (100.0, 10.0, 10.0),
            (0.0, 10.0, 0.0),
            (0.0, 0.0, None),
            (100.0, -10.0, -10),
            (-100.0, 10.0, -10),
            (-100.0, -10.0, 10),
        ]

        for price, cash_flow, expected in test_cases:
            self.assert_price_to_cash_flow(
                financial_data=self.financial_data,
                price=price,
                cash_flow=cash_flow,
                expected=expected
            )

    def test_get_and_set_cash_flow(self):
        operating_cash_flow = 100
        free_cash_flow = 50

        self.financial_data.set_cash_flow(
            cash_flow=operating_cash_flow,
            cash_flow_type=CashFlowType.OPERATING_CASH_FLOW
        )
        self.financial_data.set_cash_flow(cash_flow=free_cash_flow, cash_flow_type=CashFlowType.FREE_CASH_FLOW)
        operating_cash_flow_result = self.financial_data.get_cash_flow(cash_flow_type=CashFlowType.OPERATING_CASH_FLOW)
        free_cash_flow_result = self.financial_data.get_cash_flow(cash_flow_type=CashFlowType.FREE_CASH_FLOW)

        assert operating_cash_flow_result == operating_cash_flow
        assert free_cash_flow_result == free_cash_flow
        assert operating_cash_flow_result != free_cash_flow_result

    def test_calculate_return_on_investments(self):
        self.assert_return_on_invested_capital(
            financial_data=self.financial_data,
            net_income_to_common=1000,
            book_value=2000,
            total_debt=1000,
            expected=0.33
        )
        self.assert_return_on_invested_capital(
            financial_data=self.financial_data,
            net_income_to_common=0,
            book_value=2000,
            total_debt=1000,
            expected=0.0
        )
        self.assert_return_on_invested_capital(
            financial_data=self.financial_data,
            net_income_to_common=1000,
            book_value=0,
            total_debt=0,
            expected=None
        )
        self.assert_return_on_invested_capital(
            financial_data=self.financial_data,
            net_income_to_common=0,
            book_value=0,
            total_debt=0,
            expected=None
        )
        self.assert_return_on_invested_capital(
            financial_data=self.financial_data,
            net_income_to_common=None,
            book_value=None,
            total_debt=None,
            expected=None
        )
        self.assert_return_on_invested_capital(
            financial_data=self.financial_data,
            net_income_to_common=-1000,
            book_value=2000,
            total_debt=1000,
            expected=-0.33
        )
        self.assert_return_on_invested_capital(
            financial_data=self.financial_data,
            net_income_to_common=1000,
            book_value=2000,
            total_debt=-1000,
            expected=1.00
        )

    def test_calculate_return_on_investment(self):
        self.assert_return_on_investment(
            financial_data=self.financial_data,
            expenses=Expenses(
                capital_expenditure=0,
                interest_expense=None,
                interest_expense_non_operating=0,
                total_other_finance_cost=0
            ),
            expected=GenericError
        )
        self.assert_return_on_investment(
            financial_data=self.financial_data,
            expenses=Expenses(
                capital_expenditure=0,
                interest_expense=0,
                interest_expense_non_operating=0,
                total_other_finance_cost=0
            ),
            expected=GenericError
        )
        self.assert_return_on_investment(
            financial_data=self.financial_data,
            expenses=Expenses(
                capital_expenditure=0,
                interest_expense=1,
                interest_expense_non_operating=0,
                total_other_finance_cost=0
            ),
            expected=1.0
        )
        self.assert_return_on_investment(
            financial_data=self.financial_data,
            expenses=Expenses(
                capital_expenditure=1,
                interest_expense=1,
                interest_expense_non_operating=0,
                total_other_finance_cost=0
            ),
            expected=0.5
        )
        self.assert_return_on_investment(
            financial_data=self.financial_data,
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

        financial_data.price = "10"
        financial_data.five_year_avg_dividend_yield = "n/a"
        financial_data.debt_to_equity = "Test"
        financial_data.normalize_values()

        assert financial_data.price == 10.0
        self.assertIsNone(financial_data.five_year_avg_dividend_yield)
        self.assertIsNone(financial_data.debt_to_equity)
