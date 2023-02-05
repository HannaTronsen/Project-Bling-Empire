from functions import fetch_tickers, initializeEnvironment
from stockCollectionClass import GERMANY, HONG_KONG, NORWAY, STANDARD_AND_POOR_500

def main():

    stockCollection = [
        STANDARD_AND_POOR_500,
        NORWAY,
        GERMANY,
        HONG_KONG
    ]

    initializeEnvironment()
    fetch_tickers(stockCollection)

if __name__ == '__main__':
    main()
