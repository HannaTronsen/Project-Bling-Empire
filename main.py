import yfinance
from functions import fetch_tickers, initializeEnvironment
from stockCollections import FRANCE, GERMANY, HONG_KONG, NETHERLAND, NORWAY, STANDARD_AND_POOR_500, UNITED_KINGDOM

def checkIfValidYahooTicker():
    print(yfinance.Ticker('AGN.AS').financials)
    pass

def main():

    RUN_YAHOO_CHECK = False

    stockCollection = [
        STANDARD_AND_POOR_500,
        NORWAY,
        GERMANY,
        HONG_KONG,
        UNITED_KINGDOM,
        NETHERLAND,
        FRANCE
    ]

    if(not RUN_YAHOO_CHECK):
        initializeEnvironment()
        fetch_tickers(stockCollection)
    else:
        checkIfValidYahooTicker()

if __name__ == '__main__':
    main()


