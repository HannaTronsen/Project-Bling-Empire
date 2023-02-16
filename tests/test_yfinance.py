import unittest
import yfinance

# https://github.com/ranaroussi/yfinance/issues/1407
class TestYFinance(unittest.TestCase):
    
    def test_yfinance_api_is_working(self):
        try:
            yfinance.Ticker('MSFT')
        except Exception as e:
            self.fail(f"yfinance.Ticker('MSFT') raised {e}")
        self.assertIsNone(None)



        
