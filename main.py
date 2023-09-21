import unittest

from yahooquery import Ticker
from const import TEST_PATHS
from context.ticker_scraper.main.functions import fetch_tickers, initialize_environment
from context.yquery_ticker.main.functions import validate_and_get_yahoo_query_ticker_objects

RUN_TESTS = True
RUN_CODE = False


# Will be removed when all relevant testing csv files have been created
def create_testing_csv():
    aaplDataFrame = Ticker("aapl").cash_flow(frequency="a", trailing=True)
    file_path = "context/yquery_ticker/tests/resources/cash_flow/aapl.data.cash_flow.annually.csv"
    aaplDataFrame.to_csv(file_path, index=False)


def main():
    initialize_environment()
    fetch_tickers()
    validate_and_get_yahoo_query_ticker_objects()


if __name__ == '__main__':
    # create_testing_csv()
    if RUN_TESTS:
        test_suite = unittest.TestSuite()
        for path in TEST_PATHS:
            test_loader = unittest.TestLoader()
            test_suite.addTest(test_loader.discover(path))

        unittest.TextTestRunner().run(test_suite)

    if RUN_CODE:
        main()
