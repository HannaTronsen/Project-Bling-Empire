import os
import re
import yfinance
from stockCollections import stockCollectionsList
from const import AUTO_GENERATED_FILE_STRING, BLACKLISTED_STOCK_TICKERS_PATH, STOCK_COLLECTIONS_PATH
from stockCollections import FRANCE, GERMANY, HONG_KONG, NETHERLAND, NORWAY, STANDARD_AND_POOR_500, UNITED_KINGDOM


def initializeEnvironment():

    if not os.path.exists(STOCK_COLLECTIONS_PATH):
        os.makedirs(STOCK_COLLECTIONS_PATH)

    if not os.path.exists(BLACKLISTED_STOCK_TICKERS_PATH):
        file = open(BLACKLISTED_STOCK_TICKERS_PATH, 'a+')
        file.write(AUTO_GENERATED_FILE_STRING)
        file.close()


def fetchTickers():
    for collection in stockCollectionsList:
        match collection.name:
            case STANDARD_AND_POOR_500.name:
                STANDARD_AND_POOR_500.fetchStockTickers()
            case NORWAY.name:
                NORWAY.fetchStockTickers()
            case  GERMANY.name:
                GERMANY.fetchStockTickers()
            case HONG_KONG.name:
                HONG_KONG.fetchStockTickers()
            case UNITED_KINGDOM.name:
                UNITED_KINGDOM.fetchStockTickers()
            case NETHERLAND.name:
                NETHERLAND.fetchStockTickers()
            case FRANCE.name:
                FRANCE.fetchStockTickers()


def getYahooFinanceTickerObject():
    pass


def putYahooFinanceTickerObject(ticker):
    pass


def validateYahooFinanceTickerObjects():
    blacklistedStocksFile = open(BLACKLISTED_STOCK_TICKERS_PATH, 'r+')
    blacklistedStocksFileContent = blacklistedStocksFile.read()
    newLine = blacklistedStocksFile.write("\n")

    for stockCollection in stockCollectionsList:
        stockTickersFile = open(stockCollection.filePath, 'r').readlines()

        for ticker in stockTickersFile:
            yFinanceTicker = yfinance.Ticker(ticker)

            if re.search(ticker, blacklistedStocksFileContent) is not None:
                # Skip for now, will handle this case later
                pass
            elif not bool(yFinanceTicker.info):
                print(f"No information found for ticker '{ticker}'.")
                blacklistedStocksFile.write(ticker) + newLine
            else:
                putYahooFinanceTickerObject(ticker)

    blacklistedStocksFile.close()
