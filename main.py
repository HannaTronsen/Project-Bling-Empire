from functions import fetch_tickers, initializeEnvironment

from stockCollectionClass import STANDARD_AND_POOR_500
from stockCollectionClass import NORWAY

def main():

    stockCollection = [
        STANDARD_AND_POOR_500,
        NORWAY
    ]

    initializeEnvironment()
    fetch_tickers(stockCollection)


if __name__ == '__main__':
    main()
