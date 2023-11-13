import unittest

from config import initialize_environment, RUN_TESTS, RUN_DEV_CODE, RUN_PROD_CODE
from const import TEST_PATHS
from context.ticker_scraper.main.functions import (
    fetch_tickers
)
from context.yquery_ticker.main.functions import (
    validate_and_get_yahoo_query_ticker_objects,
    validate_and_get_yahoo_query_ticker_object,
    generate_comparable_csv_for_tickers
)


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
        validate_and_get_yahoo_query_ticker_object(ticker_symbol="NOR.OL")

    if RUN_PROD_CODE:
        main()
