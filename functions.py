import os
import re
from yahooquery import Ticker
from const import (
    AUTO_GENERATED_FILE_STRING,
    BLACKLISTED_STOCK_TICKERS_PATH,
    STOCK_COLLECTIONS_PATH,
)
from stock_collections import (
    FRANCE,
    GERMANY,
    HONG_KONG,
    NETHERLAND,
    NORWAY,
    STANDARD_AND_POOR_500,
    UNITED_KINGDOM
)
stock_collection_list = [
    # STANDARD_AND_POOR_500,
    NORWAY,
    # GERMANY,
    # HONG_KONG,
    # UNITED_KINGDOM, They changed table format
    # NETHERLAND,
    # FRANCE
]

def initialize_environment():

    if not os.path.exists(STOCK_COLLECTIONS_PATH):
        os.makedirs(STOCK_COLLECTIONS_PATH)

    if not os.path.exists(BLACKLISTED_STOCK_TICKERS_PATH):
        with open(BLACKLISTED_STOCK_TICKERS_PATH, "a+") as file:
            file.write(AUTO_GENERATED_FILE_STRING)


def fetch_tickers():

    for collection in stock_collection_list:
        match collection.name:
            case STANDARD_AND_POOR_500.name:
                STANDARD_AND_POOR_500.fetch_stock_tickers()
            case NORWAY.name:
                NORWAY.fetch_stock_tickers()
            case GERMANY.name:
                GERMANY.fetch_stock_tickers()
            case HONG_KONG.name:
                HONG_KONG.fetch_stock_tickers()
            case UNITED_KINGDOM.name:
                UNITED_KINGDOM.fetch_stock_tickers()
            case NETHERLAND.name:
                NETHERLAND.fetch_stock_tickers()
            case FRANCE.name:
                FRANCE.fetch_stock_tickers()


def get_yahoo_query_ticker_object():
    pass


def put_yahoo_query_ticker_object(ticker):
    pass


def validate_yahoo_query_ticker_objects():
    blacklisted_stocks_file = open(BLACKLISTED_STOCK_TICKERS_PATH, "r+")
    blacklisted_stocks_file_content = blacklisted_stocks_file.read()
    new_line = blacklisted_stocks_file.write("\n")

    for stock_collection in stock_collection_list:
        stock_tickers_file = open(stock_collection.file_path, "r").readlines()

        for ticker in stock_tickers_file:

            yquery_ticker = Ticker(ticker.strip())

            if re.search(ticker, blacklisted_stocks_file_content) is not None:
                # Skip for now, will handle this case later
                pass
            elif not bool(yquery_ticker.summary_detail):
                print(f"No information found for ticker '{ticker}'.")
                blacklisted_stocks_file.write(ticker.strip() + new_line)
            else:
                put_yahoo_query_ticker_object(ticker.strip())

    blacklisted_stocks_file.close()
