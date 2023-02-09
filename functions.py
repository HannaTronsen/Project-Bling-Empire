import os

from const import AUTO_GENERATED_FILE_STRING, BLACKLISTED_STOCK_TICKERS_PATH, STOCK_COLLECTIONS_PATH
from stockCollections import stockCollectionsList
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
                STANDARD_AND_POOR_500.convertDataFrameToCsv()
            case NORWAY.name:
                NORWAY.convertDataFrameToCsv()
            case  GERMANY.name:
                GERMANY.convertDataFrameToCsv()
            case HONG_KONG.name:
                HONG_KONG.convertDataFrameToCsv()
            case UNITED_KINGDOM.name:
                UNITED_KINGDOM.convertDataFrameToCsv()
            case NETHERLAND.name:
                NETHERLAND.convertDataFrameToCsv()
            case FRANCE.name:
                FRANCE.convertDataFrameToCsv()


def validateAndGetYahooFinanceTickerObjects():

    def getYahooFinanceTickerObject(ticker):
        pass

    def validateYahooFinanceTickerObjects():
        pass
    blacklistedStocksFile = open(BLACKLISTED_STOCK_TICKERS_PATH, 'a+')
    validateYahooFinanceTickerObjects()
    blacklistedStocksFile.close()