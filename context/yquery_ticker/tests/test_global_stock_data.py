# TODO(Hanna): Fix these tests

# import unittest
# from typing import Optional
# from context.yquery_ticker.main.classes.historical_earnings_data import HistoricalEarningsData
# from context.yquery_ticker.main.classes.global_stock_data import GlobalStockDataClass
# from context.yquery_ticker.main.data_classes.expenses import Expenses, ExpensesFields
# from context.yquery_ticker.main.data_classes.financial_data import EarningsPerShare, FinancialData, PriceToEarnings
# from context.yquery_ticker.main.data_classes.financial_summary import FinancialSummary
# from context.yquery_ticker.main.data_classes.general_stock_info import GeneralStockInfo
# from context.yquery_ticker.main.enums.cash_flow_type import CashFlowType
#
#
# class test_global_stock_data(unittest.TestCase):
#
#     def __init__(self, *args, **kwargs):
#         super(test_global_stock_data, self).__init__(*args, **kwargs)
#
#     def setUp(self):
#         self.mockStock = GlobalStockDataClass(
#             general_stock_info=GeneralStockInfo.mockk(),
#             financial_data=FinancialData.mockk(),
#             earnings_and_earnings_history=HistoricalEarningsData.mockk(),
#         ).financial_data.mockk()
#
#     @staticmethod
#     def assert_price_to_cash_flow(
#             stock: FinancialData,
#             price: Optional[float],
#             cash_flow: Optional[float],
#             expected: Optional[float]
#     ):
#         stock.price = price
#         stock.set_cash_flow(cash_flow=cash_flow)
#         assert stock.calculate_price_to_cashflow() == expected
#
#     @staticmethod
#     def assert_return_on_invested_capital(
#             stock: FinancialData,
#             net_income_to_common: Optional[float],
#             book_value: Optional[float],
#             total_debt: Optional[float],
#             expected: Optional[float]
#     ):
#         stock.net_income_to_common = net_income_to_common
#         stock.book_value = book_value
#         stock.total_debt = total_debt
#         result = stock.calculate_return_on_invested_capital()
#
#         if result is not None:
#             assert round(result, 2) == expected
#         else:
#             assert result == expected
#
#     @staticmethod
#     def assert_return_on_investment(
#             stock: FinancialData,
#             expenses: Expenses,
#             expected: Optional[float]
#     ):
#         stock.net_income_to_common = 100
#         stock.expenses = expenses
#         result = stock.calculate_return_on_investment()
#
#         if result is not False:
#             assert round(result, 2) == expected
#         else:
#             assert result == expected
#
#     def test_general_stock_info(self):
#         stock = GlobalStockDataClass(
#             general_stock_info=GeneralStockInfo(
#                 ticker='aapl',
#                 company='Apple Inc',
#                 country=None,  # type: ignore
#                 industry='Consumer Electronics',
#                 sector='Technology',
#                 website='https://www.apple.com',
#                 long_business_summary='N/A',
#                 financial_summary=FinancialSummary(
#                     previous_close=None,
#                     open=0.0,
#                     dividend_rate="",  # type: ignore
#                     beta=0.0,
#                     trailing_PE=0.0,
#                     forward_PE=0.0,
#                     market_cap="N/A",  # type: ignore
#                     currency="N/A"  # type: ignore
#                 )
#             ),
#             financial_data=FinancialData.mockk(),
#             earnings_and_earnings_history=HistoricalEarningsData.mockk()
#         ).general_stock_info
#
#         self.assertIsNone(stock.country)
#         self.assertIsNone(stock.long_business_summary)
#         self.assertIsNone(stock.financial_summary.previous_close)
#         self.assertIsNone(stock.financial_summary.market_cap)
#         self.assertIsNone(stock.financial_summary.currency)
#         self.assertIsNone(stock.financial_summary.dividend_rate)
#
#     def test_financial_data(self):
#         stock = GlobalStockDataClass(
#             general_stock_info=GeneralStockInfo.mockk(),
#             financial_data=FinancialData(
#                 price=10,
#                 total_revenue=0.00000,
#                 revenue_per_share="",  # type: ignore
#                 revenue_growth="N/A",  # type: ignore
#                 total_debt=-1,
#                 debt_to_equity=0,
#                 profit_margins=3,
#                 gross_profit_margins="N/A",  # type: ignore
#                 operating_margins=None,
#                 dividend_rate=0,
#                 dividend_yield=0,
#                 five_year_avg_dividend_yield=0,
#                 trailing_annual_dividend_rate=0,
#                 trailing_annual_dividend_yield=0,
#                 free_cash_flow=0,
#                 operating_cash_flow=0,
#                 enterprise_to_ebitda=0,
#                 price_to_book=0,
#                 return_on_assets=0,
#                 return_on_equity=0,
#                 net_income_to_common=0,
#                 earnings_growth=0,
#                 book_value=0,
#                 price_to_earnings=PriceToEarnings(
#                     trailing_pe="N/A",  # type: ignore
#                     forward_pe=2
#                 ),
#                 earnings_per_share=EarningsPerShare(
#                     trailing_eps=2,
#                     forward_eps="N/A"  # type: ignore
#                 ),
#                 enterprise_to_revenue=0,
#                 expenses=None
#             ),
#             earnings_and_earnings_history=HistoricalEarningsData.mockk()
#         ).financial_data
#         self.assertIsNone(stock.revenue_per_share)
#         self.assertIsNone(stock.revenue_growth)
#         self.assertIsNone(stock.total_debt)
#         self.assertIsNone(stock.total_debt)
#         self.assertIsNone(stock.gross_profit_margins)
#         self.assertIsNone(stock.operating_margins)
#         self.assertIsNone(stock.price_to_earnings.trailing_pe)
#         self.assertIsNone(stock.earnings_per_share.forward_eps)
#         self.assertIsNone(stock.expenses)
#
#     def test_calculate_price_to_cashflow(self):
#         self.assert_price_to_cash_flow(stock=self.mockStock, price=None, cash_flow=10, expected=None)
#         self.assert_price_to_cash_flow(stock=self.mockStock, price=10, cash_flow=None, expected=None)
#         self.assert_price_to_cash_flow(stock=self.mockStock, price=100.0, cash_flow=10.0, expected=10.0)
#         self.assert_price_to_cash_flow(stock=self.mockStock, price=0.0, cash_flow=10.0, expected=0.0)
#         self.assert_price_to_cash_flow(stock=self.mockStock, price=0.0, cash_flow=0.0, expected=None)
#         self.assert_price_to_cash_flow(stock=self.mockStock, price=100.0, cash_flow=-10.0, expected=-10)
#         self.assert_price_to_cash_flow(stock=self.mockStock, price=-100.0, cash_flow=10.0, expected=-10)
#         self.assert_price_to_cash_flow(stock=self.mockStock, price=-100.0, cash_flow=-10.0, expected=10)
#         self.assert_price_to_cash_flow(stock=self.mockStock, price=100.0, cash_flow=10.0, expected=10.0)
#
#     def test_get_and_set_cash_flow(self):
#         self.mockStock.free_cash_flow = 10
#         self.mockStock.set_cash_flow(cash_flow=100, cash_flow_type=CashFlowType.OPERATING_CASH_FLOW)
#         assert self.mockStock.get_cash_flow(
#             cash_flow_type=CashFlowType.OPERATING_CASH_FLOW) == self.mockStock.operating_cash_flow
#
#         self.mockStock.operating_cash_flow = 100
#         self.mockStock.set_cash_flow(cash_flow=100, cash_flow_type=CashFlowType.FREE_CASH_FLOW)
#         assert self.mockStock.get_cash_flow(cash_flow_type=CashFlowType.FREE_CASH_FLOW) == self.mockStock.free_cash_flow
#
#     def test_calculate_return_on_investments(self):
#         self.assert_return_on_invested_capital(
#             stock=self.mockStock,
#             net_income_to_common=1000,
#             book_value=2000,
#             total_debt=1000,
#             expected=0.33
#         )
#         self.assert_return_on_invested_capital(
#             stock=self.mockStock,
#             net_income_to_common=0,
#             book_value=2000,
#             total_debt=1000,
#             expected=0.0
#         )
#         self.assert_return_on_invested_capital(
#             stock=self.mockStock,
#             net_income_to_common=1000,
#             book_value=0,
#             total_debt=0,
#             expected=None
#         )
#         self.assert_return_on_invested_capital(
#             stock=self.mockStock,
#             net_income_to_common=0,
#             book_value=0,
#             total_debt=0,
#             expected=None
#         )
#         self.assert_return_on_invested_capital(
#             stock=self.mockStock,
#             net_income_to_common=None,
#             book_value=None,
#             total_debt=None,
#             expected=None
#         )
#         self.assert_return_on_invested_capital(
#             stock=self.mockStock,
#             net_income_to_common=-1000,
#             book_value=2000,
#             total_debt=1000,
#             expected=-0.33
#         )
#         self.assert_return_on_invested_capital(
#             stock=self.mockStock,
#             net_income_to_common=1000,
#             book_value=2000,
#             total_debt=-1000,
#             expected=1.00
#         )
#
#     def test_calculate_return_on_investment(self):
#         self.assert_return_on_investment(
#             stock=self.mockStock,
#             expenses=Expenses(
#                 capital_expenditure=0,
#                 interest_expense=None,
#                 interest_expense_non_operating=0,
#                 total_other_finance_cost=0
#             ),
#             expected=False
#         )
#         self.assert_return_on_investment(
#             stock=self.mockStock,
#             expenses=Expenses(
#                 capital_expenditure=0,
#                 interest_expense=0,
#                 interest_expense_non_operating=0,
#                 total_other_finance_cost=0
#             ),
#             expected=False
#         )
#         self.assert_return_on_investment(
#             stock=self.mockStock,
#             expenses=Expenses(
#                 capital_expenditure=0,
#                 interest_expense=1,
#                 interest_expense_non_operating=0,
#                 total_other_finance_cost=0
#             ),
#             expected=1.0
#         )
#         self.assert_return_on_investment(
#             stock=self.mockStock,
#             expenses=Expenses(
#                 capital_expenditure=1,
#                 interest_expense=1,
#                 interest_expense_non_operating=0,
#                 total_other_finance_cost=0
#             ),
#             expected=0.5
#         )
#         self.assert_return_on_investment(
#             stock=self.mockStock,
#             expenses=Expenses(
#                 capital_expenditure=-1,
#                 interest_expense=-1,
#                 interest_expense_non_operating=0,
#                 total_other_finance_cost=0
#             ),
#             expected=-0.5
#         )
#
#     def test_sum_expenses(self):
#         assert Expenses(
#             capital_expenditure=1,
#             interest_expense=0,
#             interest_expense_non_operating=0,
#             total_other_finance_cost=0
#         ).sum() == 1
#         assert Expenses(
#             capital_expenditure=1,
#             interest_expense=-2,
#             interest_expense_non_operating=0,
#             total_other_finance_cost=0
#         ).sum() == -1
#         assert Expenses(
#             capital_expenditure=1,
#             interest_expense=1,
#             interest_expense_non_operating=2,
#             total_other_finance_cost=0
#         ).sum(exclude=[ExpensesFields.INTEREST_EXPENSE_NON_OPERATING]) == 2
#         assert Expenses(
#             capital_expenditure=1,
#             interest_expense=1,
#             interest_expense_non_operating=3,
#             total_other_finance_cost=2
#         ).sum(exclude=[ExpensesFields.TOTAL_OTHER_FINANCE_COST]) == 5
#
#     def test_type_checking(self):
#         expenses: Expenses = Expenses(
#             capital_expenditure=1.0,
#             interest_expense="1.01",  # type: ignore
#             interest_expense_non_operating="Zero",  # type: ignore
#             total_other_finance_cost=None
#         ).normalize_values()
#
#         self.assertIsNotNone(expenses.interest_expense)
#         assert expenses.interest_expense == 1.01
#         self.assertIsNone(expenses.interest_expense_non_operating)
#         self.assertIsNone(expenses.total_other_finance_cost)
#
#         stock = GlobalStockDataClass(
#             general_stock_info=GeneralStockInfo.mockk(),
#             financial_data=FinancialData(
#                 price=10,
#                 total_revenue=0.00000,
#                 revenue_per_share="",  # type: ignore
#                 revenue_growth="N/A",  # type: ignore
#                 total_debt=-1,
#                 debt_to_equity=0,
#                 profit_margins=3,
#                 gross_profit_margins="n/a",  # type: ignore
#                 operating_margins=None,
#                 dividend_rate=0,
#                 dividend_yield=0,
#                 five_year_avg_dividend_yield=0,
#                 trailing_annual_dividend_rate=0,
#                 trailing_annual_dividend_yield=0,
#                 free_cash_flow=0,
#                 operating_cash_flow=0,
#                 enterprise_to_ebitda=0,
#                 price_to_book=0,
#                 return_on_assets=0,
#                 return_on_equity=0,
#                 net_income_to_common=0,
#                 earnings_growth=0,
#                 book_value=0,
#                 price_to_earnings=PriceToEarnings(
#                     trailing_pe="N/A",  # type: ignore
#                     forward_pe="2.0"  # type: ignore
#                 ),
#                 earnings_per_share=EarningsPerShare(
#                     trailing_eps=10,
#                     forward_eps="Test"  # type: ignore
#                 ),
#                 enterprise_to_revenue=10,
#                 expenses=None,
#             ),
#             earnings_and_earnings_history=HistoricalEarningsData.mockk()
#         ).financial_data
#
#         assert stock.price_to_earnings.forward_pe == 2.0
#         assert stock.earnings_per_share.trailing_eps == 10.0
#         self.assertIsNone(stock.price_to_earnings.trailing_pe)
#         self.assertIsNone(stock.gross_profit_margins)
#         self.assertIsNone(stock.earnings_per_share.forward_eps)
#
#         self.mockStock.price = "10"
#         self.mockStock.five_year_avg_dividend_yield = "n/a"
#         self.mockStock.debt_to_equity = "Test"
#         self.mockStock.normalize_values()
#
#         assert self.mockStock.price == 10.0
#         self.assertIsNone(self.mockStock.five_year_avg_dividend_yield)
#         self.assertIsNone(self.mockStock.debt_to_equity)
