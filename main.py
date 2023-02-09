import yfinance
from functions import fetchTickers, initializeEnvironment


def checkIfValidYahooTicker():
    print(yfinance.Ticker('AGN.AS').financials)
    pass


def main():

    RUN_YAHOO_CHECK = False

    if (not RUN_YAHOO_CHECK):
        initializeEnvironment()
        fetchTickers()
    else:
        checkIfValidYahooTicker()


if __name__ == '__main__':
    main()
