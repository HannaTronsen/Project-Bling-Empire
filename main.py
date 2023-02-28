import unittest

from functions import fetchTickers, initializeEnvironment
from yFinanceRepository import validateAndGetYahooFinanceTickerObjects

RUN_TESTS = False
RUN_CODE = True


def main():

    initializeEnvironment()
    fetchTickers()
    #validateAndGetYahooFinanceTickerObjects()


if __name__ == '__main__':

    if RUN_TESTS:
        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover('tests/integrationTests')
        unittest.TextTestRunner().run(test_suite)

    if RUN_CODE:
        main()
