import unittest
from yahooquery import Ticker


class test_yquery(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_yquery, self).__init__(*args, **kwargs)
        try:
            self.error_prefix = "yquery.Ticker('MSFT')"
            self.error_suffix = "caused and exception:"
            self.ticker = Ticker('MSFT')
        except Exception as e:
            self.fail(
                f'{self.error_prefix} in init {self.error_suffix} {e}. API might be down!'
            )
        self.assertIsNone(None)

    def test_summary(self):
        try:
            self.ticker.summary_detail
            self.ticker.summary_profile
        except Exception as e:
            self.throw_generic_error("test_summary()", e)
        self.assertIsNone(None)

    def test_history(self):
        try:
            self.ticker.history
        except Exception as e:
            self.throw_generic_error("test_history()", e)
        self.assertIsNone(None)

    def test_dividends(self):
        try:
            self.ticker.dividend_history,
        except Exception as e:
            self.throw_generic_error("test_dividends()", e)
        self.assertIsNone(None)

    def test_income_statement(self):
        try:
            self.ticker.income_statement
        except Exception as e:
            self.throw_generic_error("test_income_statement()", e)
        self.assertIsNone(None)

    def test_balance_sheet(self):
        try:
            self.ticker.balance_sheet
        except Exception as e:
            self.throw_generic_error("test_balance_sheet()", e)
        self.assertIsNone(None)

    def test_cash_flow(self):
        try:
            self.ticker.cash_flow
        except Exception as e:
            self.throw_generic_error("test_cash_flow()", e)
        self.assertIsNone(None)

    def test_holders(self):
        try:
            self.ticker.major_holders
            self.ticker.insider_holders
        except Exception as e:
            self.throw_generic_error("test_holders()", e)
        self.assertIsNone(None)

    def test_earnings(self):

        try:
            self.ticker.earnings
        except Exception as e:
            self.throw_generic_error("test_earnings()", e)
        self.assertIsNone(None)

    def test_recommendations(self):
        try:
            self.ticker.recommendations
        except Exception as e:
            self.throw_generic_error("test_recommendations()", e)
        self.assertIsNone(None)

    def test_news(self):
        try:
            self.ticker.news
        except Exception as e:
            self.throw_generic_error("test_news()", e)
        self.assertIsNone(None)

    def throw_generic_error(self, methodName, e):
        self.fail(
            f'{self.error_prefix} {methodName} {self.error_suffix} {e}'
        )
