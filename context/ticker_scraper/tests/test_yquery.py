import unittest
from yahooquery import Ticker


class test_yquery(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_yquery, self).__init__(*args, **kwargs)
        try:
            self.error_message_prefix = "yquery.Ticker('MSFT')"
            self.error_message_suffix = "caused and exception:"
            self.ticker = Ticker("MSFT")
            self.ticker_fields = [
                (self.ticker.summary_detail, "summary_detail"),
                (self.ticker.summary_profile, "summary_profile"),
                (self.ticker.history, "history"),
                (self.ticker.dividend_history, "dividend_history"),
                (self.ticker.history, "history"),
                (self.ticker.income_statement, "income_statement"),
                (self.ticker.balance_sheet, "balance_sheet"),
                (self.ticker.cash_flow, "cash_flow"),
                (self.ticker.major_holders, "major_holders"),
                (self.ticker.earnings, "earnings"),
                (self.ticker.recommendations, "recommendations"),
                (self.ticker.news, "news")
            ]
        except Exception as e:
            self.fail(
                f'{self.error_message_prefix} in init {self.error_message_suffix} {e}. API might be down!'
            )
        self.assertIsNone(None)

    def test_ticker(self):
        pass
        for field, field_name in self.ticker_fields:
            try:
                self.assertIsNotNone(field)
            except Exception as e:
                self.throw_generic_error(f"${field_name}()", e)

    def throw_generic_error(self, method_name, e):
        self.fail(
            f'{self.error_message_prefix} {method_name} {self.error_message_suffix} {e}'
        )

    if __name__ == '__main__':
        unittest.main()
