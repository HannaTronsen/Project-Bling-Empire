import unittest

from const import TEST_PATHS
from context.ticker_scraper.main.functions import (
    fetch_tickers,
    initialize_environment,
)
from context.yquery_ticker.main.functions import (
    validate_and_get_yahoo_query_ticker_objects,
    validate_and_get_yahoo_query_ticker_object,
    generate_comparable_csv_for_tickers
)

RUN_TESTS = False
RUN_PROD_CODE = True
RUN_DEV_CODE = False


def main():
    initialize_environment()
    fetch_tickers()
    generate_comparable_csv_for_tickers(tickers=sorted(
        validate_and_get_yahoo_query_ticker_objects(),
        key=lambda ticker: ticker.criteria_pass_count,
        reverse=True
    ))


if __name__ == '__main__':
    if RUN_TESTS:
        test_suite = unittest.TestSuite()
        for path in TEST_PATHS:
            test_loader = unittest.TestLoader()
            test_suite.addTest(test_loader.discover(path))

        unittest.TextTestRunner().run(test_suite)

    if RUN_DEV_CODE:
        validate_and_get_yahoo_query_ticker_object(ticker_symbol="ACR.OL")

    if RUN_PROD_CODE:
        main()
