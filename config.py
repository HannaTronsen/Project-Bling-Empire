import os
from context.ticker_scraper.main.const import STOCK_COLLECTIONS_PATH
from const import GENERATED_CSV_FILES_PATH

RUN_TESTS = True
GENERATE_TICKER_CSV = False
GENERATE_COMPARABLE_CSV = False

CASTABLE_DATA_SHOW_DEBUG_PRINT = False
QUARTER_SHOW_DEBUG_PRINT = True
ITERABLE_DATA_SHOW_DEBUG_PRINT = False


def initialize_environment():
    if not os.path.exists(STOCK_COLLECTIONS_PATH):
        os.makedirs(STOCK_COLLECTIONS_PATH)

    if not os.path.exists(GENERATED_CSV_FILES_PATH):
        os.makedirs(GENERATED_CSV_FILES_PATH)
