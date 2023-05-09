import unittest
from context.ticker_scraper.main.functions import fetch_tickers, initialize_environment
from context.yquery_ticker.main.functions import validate_and_get_yahoo_query_ticker_objects
from const import TEST_PATHS


RUN_TESTS = True
RUN_CODE = False


def main():
    initialize_environment()
    fetch_tickers()
    validate_and_get_yahoo_query_ticker_objects()


if __name__ == '__main__':

    if RUN_TESTS:
        test_suite = unittest.TestSuite()

        for path in TEST_PATHS:
            test_loader = unittest.TestLoader()
            test_suite.addTest(test_loader.discover(path))

        unittest.TextTestRunner().run(test_suite)

    if RUN_CODE:
        main()
