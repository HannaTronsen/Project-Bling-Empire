import unittest

from config import initialize_environment, RUN_TESTS, GENERATE_TICKER_CSV, GENERATE_COMPARABLE_CSV
from const import TEST_PATHS
from context.ticker_scraper.main.functions import fetch_tickers
from context.ticker_scraper.main.stock_collections import NORWAY
from context.yquery_ticker.main.functions import (
    get_grouped_yahoo_query_ticker_objects,
    validate_and_get_yahoo_query_ticker_object,
)
from context.yquery_ticker.main.utils.comparable_csv import ComparableCSV


def main():
    initialize_environment()
    fetch_tickers()
    ComparableCSV(stock_collection=get_grouped_yahoo_query_ticker_objects()).create()


if __name__ == '__main__':
    if RUN_TESTS:
        test_suite = unittest.TestSuite()
        for path in TEST_PATHS:
            test_loader = unittest.TestLoader()
            test_suite.addTest(test_loader.discover(path))

        unittest.TextTestRunner().run(test_suite)

    if GENERATE_TICKER_CSV:
        validate_and_get_yahoo_query_ticker_object(ticker_symbol="ACR.OL").to_csv(
            stock_collection=NORWAY.stock_index_name
        )

    if GENERATE_COMPARABLE_CSV:
        main()
