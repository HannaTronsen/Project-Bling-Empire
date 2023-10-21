import os
from context.ticker_scraper.main.const import STOCK_COLLECTIONS_PATH
from const import (
    AUTO_GENERATED_FILE_STRING,
    BLACKLISTED_STOCK_TICKERS_PATH,
    GENERATED_CSV_FILES_PATH
)

RUN_TESTS = True
RUN_PROD_CODE = False
RUN_DEV_CODE = False

GENERATE_DEV_CSV = True
GENERATE_PROD_CSV = True

CASTABLE_DATA_SHOW_DEBUG_PRINT = False
QUARTER_SHOW_DEBUG_PRINT = True
ITERABLE_DATA_SHOW_DEBUG_PRINT = False


def initialize_environment():
    if not os.path.exists(STOCK_COLLECTIONS_PATH):
        os.makedirs(STOCK_COLLECTIONS_PATH)

    if not os.path.exists(GENERATED_CSV_FILES_PATH):
        os.makedirs(GENERATED_CSV_FILES_PATH)

    if not os.path.exists(BLACKLISTED_STOCK_TICKERS_PATH):
        with open(BLACKLISTED_STOCK_TICKERS_PATH, "a+") as file:
            file.write(AUTO_GENERATED_FILE_STRING)
