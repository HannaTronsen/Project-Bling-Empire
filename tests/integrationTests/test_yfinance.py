import unittest
import numpy as np
import pandas as pd
import yfinance

# https://github.com/ranaroussi/yfinance/issues/1407


class test_yfinance(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_yfinance, self).__init__(*args, **kwargs)
        try:
            self.error_prefix = "yfinance.Ticker('MSFT')"
            self.error_suffix = "caused and exception:"
            self.ticker = yfinance.Ticker('MSFT')
        except Exception as e:
            self.fail(
                f'{self.error_prefix} in init {self.error_suffix} {e}. API might be down!'
            )
        self.assertIsNone(None)

    def test_info(self):
        try:
            self.ticker.fast_info
            self.ticker.info
        except Exception as e:
            self.throw_generic_error("test_info()", e)
        self.assertIsNone(None)

    def test_history_and_metadata(self):
        try:
            self.ticker.history
            self.assert_equal_values(
                "history and metadata",
                self.ticker.history_metadata,
                self.ticker.get_history_metadata(),
            )

        except Exception as e:
            self.throw_generic_error("test_history_and_metadata()", e)
        self.assertIsNone(None)

    def test_dividends(self):
        try:

            self.assert_equal_values(
                "dividends",
                self.ticker.dividends,
                self.ticker.get_dividends(),
            )

        except Exception as e:
            self.throw_generic_error("test_dividends()", e)
        self.assertIsNone(None)

    def test_splits(self):
        try:

            self.assert_equal_values(
                "split",
                self.ticker.splits,
                self.ticker.get_splits(),
            )

        except Exception as e:
            self.throw_generic_error("test_splits()", e)
        self.assertIsNone(None)

    def test_income_statement(self):
        try:

            self.assert_equal_values(
                "income statement",
                self.ticker.income_stmt,
                self.ticker.incomestmt,
                self.ticker.get_income_stmt(),
                self.ticker.get_incomestmt(),
            )

        except Exception as e:
            self.throw_generic_error("test_income_statement()", e)
        self.assertIsNone(None)

    def test_balance_sheet(self):
        try:

            self.assert_equal_values(
                "balance sheet",
                self.ticker.balance_sheet,
                self.ticker.balancesheet,
                self.ticker.get_balancesheet(),
                self.ticker.get_balance_sheet(),
            )

        except Exception as e:
            self.throw_generic_error("test_balance_sheet()", e)
        self.assertIsNone(None)

    def test_cash_flow_statement(self):
        try:

            self.assert_equal_values(
                "cash flow",
                self.ticker.cash_flow,
                self.ticker.cashflow,
                self.ticker.get_cash_flow(),
                self.ticker.get_cashflow(),
            )

        except Exception as e:
            self.throw_generic_error("test_cash_flow_statement()", e)
        self.assertIsNone(None)

    def test_holders(self):
        try:

            self.assert_equal_values(
                "majord holders",
                self.ticker.major_holders,
                self.ticker.get_major_holders(),
            )

            self.assert_equal_values(
                "institutional holders",
                self.ticker.institutional_holders,
                self.ticker.get_institutional_holders(),
            )

            self.assert_equal_values(
                "mutual fund holders",
                self.ticker.mutualfund_holders,
                self.ticker.get_mutualfund_holders(),
            )

        except Exception as e:
            self.throw_generic_error("test_holders()", e)
        self.assertIsNone(None)

    def test_earnings(self):
        try:

            self.assert_equal_values(
                "earnings",
                self.ticker.earnings,
                self.ticker.get_earnings(),
            )

        except Exception as e:
            self.throw_generic_error("test_earnings()", e)
        self.assertIsNone(None)

    def test_sustainability(self):
        try:

            self.assert_equal_values(
                "sustainability ",
                self.ticker.sustainability,
                self.ticker.get_sustainability(),
            )

        except Exception as e:
            self.throw_generic_error("test_sustainability()", e)
        self.assertIsNone(None)

    def test_recommendations(self):
        try:

            self.assert_equal_values(
                "recommendations",
                self.ticker.recommendations,
                self.ticker.get_recommendations(),
            )

            self.assert_equal_values(
                "recommendation summary",
                self.ticker.recommendations_summary,
                self.ticker.get_recommendations_summary(),
            )

        except Exception as e:
            self.throw_generic_error("test_recommendations()", e)
        self.assertIsNone(None)

    def test_price_target(self):
        try:

            self.assert_equal_values(
                "analyst price target",
                self.ticker.analyst_price_target,
                self.ticker.get_analyst_price_target(),
            )

        except Exception as e:
            self.throw_generic_error("test_price_target()", e)
        self.assertIsNone(None)

    def test_forcasts_and_trends(self):
        try:

            self.assert_equal_values(
                "revenue forcast",
                self.ticker.revenue_forecasts,
                self.ticker.get_rev_forecast(),
            )

            self.assert_equal_values(
                "earnings forcast",
                self.ticker.earnings_forecasts,
                self.ticker.get_earnings_forecast(),
            )

            self.assert_equal_values(
                "earnings trend forcast",
                self.ticker.earnings_trend,
                self.ticker.get_earnings_trend(),
            )

        except Exception as e:
            self.throw_generic_error("test_forcasts_and_trends()", e)
        self.assertIsNone(None)

    def test_news(self):
        try:

            self.assert_equal_values(
                "news",
                self.ticker.news,
                self.ticker.get_news(),
            )

        except Exception as e:
            self.throw_generic_error("test_news()", e)
        self.assertIsNone(None)

    def throw_generic_error(self, methodName, e):
        self.fail(
            f'{self.error_prefix} {methodName} {self.error_suffix} {e}'
        )

    def assert_equal_values(self, valueName, *args):
        first_value = args[0]
        with self.subTest(f'{valueName} values should be identical'):
            for value in args[1:]:
                # convert Series to numpy array for comparison
                if isinstance(first_value, pd.Series):
                    first_value = first_value.values.flatten()
                if isinstance(value, pd.Series):
                    value = value.values.flatten()
                self.assertTrue(np.array_equal(value, first_value))
