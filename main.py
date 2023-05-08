import unittest
from functions import fetch_tickers, initialize_environment
from yquery_repository import validate_and_get_yahoo_query_ticker_objects


RUN_TESTS = True
RUN_CODE = False


def main():
    initialize_environment()
    fetch_tickers()
    validate_and_get_yahoo_query_ticker_objects()


if __name__ == '__main__':

    if RUN_TESTS:
        test_loader = unittest.TestLoader()
        #test_suite = test_loader.discover('tests/integration_tests', 'tests/unit_tests')
        test_suite = test_loader.discover('tests/unit_tests')
        unittest.TextTestRunner().run(test_suite)

    if RUN_CODE:
        main()
