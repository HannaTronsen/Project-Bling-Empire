import os
from .const import STOCK_COLLECTIONS_PATH
from const import (
    AUTO_GENERATED_FILE_STRING,
    BLACKLISTED_STOCK_TICKERS_PATH,
    CONST_COLLECTION,
    GENERATED_CSV_FILES_PATH
)


def initialize_environment():
    if not os.path.exists(STOCK_COLLECTIONS_PATH):
        os.makedirs(STOCK_COLLECTIONS_PATH)

    if not os.path.exists(GENERATED_CSV_FILES_PATH):
        os.makedirs(GENERATED_CSV_FILES_PATH)

    if not os.path.exists(BLACKLISTED_STOCK_TICKERS_PATH):
        with open(BLACKLISTED_STOCK_TICKERS_PATH, "a+") as file:
            file.write(AUTO_GENERATED_FILE_STRING)


def fetch_tickers():
    for collection in CONST_COLLECTION.STCOK_COLLECTION_LIST:
        collection.fetch_stock_tickers()
