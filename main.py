import yfinance
from functions import fetchTickers, initializeEnvironment, validateAndGetYahooFinanceTickerObjects


def checkIfValidYahooTicker():
    print(yfinance.Ticker('AAPL').earnings)
    pass


def main():

    RUN_YAHOO_CHECK = True

    if (not RUN_YAHOO_CHECK):
        initializeEnvironment()
        fetchTickers()
        validateAndGetYahooFinanceTickerObjects()
    else:
        checkIfValidYahooTicker()


if __name__ == '__main__':
    main()
