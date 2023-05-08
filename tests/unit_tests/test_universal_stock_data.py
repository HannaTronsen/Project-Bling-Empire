import unittest
from classes.data_classes.financial_summary import FinancialSummary
from classes.data_classes.general_stock_info import GeneralStockInfo

from classes.universal_stock_data import UniversalStockDataClass


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
                    previousClose=0.0,
                    open=0.0,
                    dividend_rate=0.0,
                    beta=0.0,
                    trailing_PE=0.0,
                    forward_PE=0.0,
                    market_cap=None,
                    currency=None
                )
            )
        ).general_stock_info
        self.assertIsNone(stock.country)
        self.assertIsNone(stock.long_business_summary)
        self.assertIsNone(stock.financial_summary.market_cap)
        self.assertIsNone(stock.financial_summary.currency)
