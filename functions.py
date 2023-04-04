import os
import re
import yfinance
from stock_collections import stock_collection_classsList
from const import AUTO_GENERATED_FILE_STRING, BLACKLISTED_STOCK_TICKERS_PATH, STOCK_COLLECTIONS_PATH
from stock_collections import FRANCE, GERMANY, HONG_KONG, NETHERLAND, NORWAY, STANDARD_AND_POOR_500, UNITED_KINGDOM


def initialize_environment():

    if not os.path.exists(STOCK_COLLECTIONS_PATH):
        os.makedirs(STOCK_COLLECTIONS_PATH)

    if not os.path.exists(BLACKLISTED_STOCK_TICKERS_PATH):
        file = open(BLACKLISTED_STOCK_TICKERS_PATH, 'a+')
        file.write(AUTO_GENERATED_FILE_STRING)
        file.close()


def fetch_tickers():
    for collection in stock_collection_classsList:
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


def get_yahoo_finance_ticker_object():
    pass


def put_yahoo_finance_ticker_object(ticker):
    pass


def validate_yahoo_finance_ticker_objects():
    blacklistedStocksFile = open(BLACKLISTED_STOCK_TICKERS_PATH, 'r+')
    blacklistedStocksFileContent = blacklistedStocksFile.read()
    newLine = blacklistedStocksFile.write("\n")

    for stock_collection_class in stock_collection_classsList:
        stockTickersFile = open(stock_collection_class.filePath, 'r').readlines()

        for ticker in stockTickersFile:
            yFinanceTicker = yfinance.Ticker(ticker)

            if re.search(ticker, blacklistedStocksFileContent) is not None:
                # Skip for now, will handle this case later
                pass
            elif not bool(yFinanceTicker.info):
                print(f"No information found for ticker '{ticker}'.")
                blacklistedStocksFile.write(ticker) + newLine
            else:
                put_yahoo_finance_ticker_object(ticker)

    blacklistedStocksFile.close()
