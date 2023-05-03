import subprocess
import unittest
from functions import fetch_tickers, initialize_environment
from yfinance_repository import validate_and_get_yahoo_finance_ticker_objects


RUN_PYLINT = False
RUN_TESTS = False
RUN_CODE = True


def main():
    initialize_environment()
    fetch_tickers()
    validate_and_get_yahoo_finance_ticker_objects()


if __name__ == '__main__':

    if RUN_PYLINT:
        subprocess.run(["scripts/format.sh runPylint"], shell=True)

    if RUN_TESTS:
        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover('tests/integrationTests')
        unittest.TextTestRunner().run(test_suite)

    if RUN_CODE:
        main()
