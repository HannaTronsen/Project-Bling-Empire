import os
from .const import STOCK_COLLECTIONS_PATH
from const import (
    AUTO_GENERATED_FILE_STRING,
    BLACKLISTED_STOCK_TICKERS_PATH,
    CONST_COLLECTION
)


def initialize_environment():
    if not os.path.exists(STOCK_COLLECTIONS_PATH):
        os.makedirs(STOCK_COLLECTIONS_PATH)

    if not os.path.exists(BLACKLISTED_STOCK_TICKERS_PATH):
        with open(BLACKLISTED_STOCK_TICKERS_PATH, "a+") as file:
            file.write(AUTO_GENERATED_FILE_STRING)


def fetch_tickers():

    for collection in CONST_COLLECTION.STCOK_COLLECTION_LIST:
        match collection.stock_index_name:
            case CONST_COLLECTION.STANDARD_AND_POOR_500.stock_index_name:
                CONST_COLLECTION.STANDARD_AND_POOR_500.fetch_stock_tickers()
            case CONST_COLLECTION.NORWAY.stock_index_name:
                CONST_COLLECTION.NORWAY.fetch_stock_tickers()
            case CONST_COLLECTION.GERMANY.stock_index_name:
                CONST_COLLECTION.GERMANY.fetch_stock_tickers()
            case CONST_COLLECTION.HONG_KONG.stock_index_name:
                CONST_COLLECTION.HONG_KONG.fetch_stock_tickers()
            case CONST_COLLECTION.UNITED_KINGDOM.stock_index_name:
                CONST_COLLECTION.UNITED_KINGDOM.fetch_stock_tickers()
            case CONST_COLLECTION.NETHERLAND.stock_index_name:
                CONST_COLLECTION.NETHERLAND.fetch_stock_tickers()
            case CONST_COLLECTION.FRANCE.stock_index_name:
                CONST_COLLECTION.FRANCE.fetch_stock_tickers()
