from typing import Type
import unittest
from context.yquery_ticker.main.classes.universal_stock_data import UniversalStockDataClass
from context.yquery_ticker.main.data_classes.financial_data import FinancialData
from context.yquery_ticker.main.data_classes.financial_summary import FinancialSummary
from context.yquery_ticker.main.data_classes.general_stock_info import GeneralStockInfo


class test_universal_stock_data(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_universal_stock_data, self).__init__(*args, **kwargs)

    def test_general_stock_info(self):
        stock = UniversalStockDataClass(
            general_stock_info=GeneralStockInfo(
                ticker='aapl',
                company_name='Apple Inc',
                country=None,
                industry='Consumer Electronics',
                sector='Technology',
                website='http://www.apple.com',
                long_business_summary='N/A',
                financial_summary=FinancialSummary(
                    previous_close=0.0,
                    open=0.0,
                    dividend_rate=0.0,
                    beta=0.0,
                    trailing_PE=0.0,
                    forward_PE=0.0,
                    market_cap=None,
                    currency=None
                )
            ),
            financial_data=FinancialData.mockk()
        ).general_stock_info

        self.assertIsNone(stock.country)
        self.assertIsNone(stock.long_business_summary)
        self.assertIsNone(stock.financial_summary.market_cap)
        self.assertIsNone(stock.financial_summary.currency)

    def test_financial_data(self):
        stock = UniversalStockDataClass(
            general_stock_info=GeneralStockInfo.mockk(),
            financial_data=FinancialData(
                total_revenue=0.00000,
                revenue_per_share="",
                revenue_growth="N/A",
                total_debt=-1,
                debt_to_equity=0,
                profit_margins=3,
                gross_profit_margins="N/A",
                operating_margins=None,
                dividend_rate=0,
                dividend_yield=0,
                five_year_avg_dividend_yield=0,
                trailing_annual_dividend_rate=0,
                trailing_annual_dividend_yield=0
            )
        ).financial_data
        self.assertIsNone(stock.revenue_per_share)
        self.assertIsNone(stock.revenue_growth)
        self.assertIsNone(stock.total_debt)
        self.assertIsNone(stock.total_debt)
        self.assertIsNone(stock.gross_profit_margins)
        self.assertIsNone(stock.operating_margins)
