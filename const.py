# context based consts
import re
from context.ticker_scraper.main.const import *
from context.yquery_ticker.main.const import *

def _get_all_test_paths_list():
    all_vars = globals().keys()
    pattern = re.compile('.*TEST_PATH.*')
    return [globals()[var] for var in all_vars if pattern.match(var)]

class CONST_COLLECTION:
    from context.ticker_scraper.main.stock_collections import (
        FRANCE,
        GERMANY,
        HONG_KONG,
        NETHERLAND,
        NORWAY,
        STANDARD_AND_POOR_500,
        UNITED_KINGDOM
    ) 
    STCOK_COLLECTION_LIST = [
        # STANDARD_AND_POOR_500,
        NORWAY,
        # GERMANY,
        # HONG_KONG,
        # UNITED_KINGDOM, They changed table format
        # NETHERLAND,
        # FRANCE
]


BLACKLISTED_STOCK_TICKERS_PATH = f'black_listed_stock_tickers.txt'
AUTO_GENERATED_FILE_STRING = " ### This file is auto generated and shouldn't be touched! ### "
TEST_PATHS = _get_all_test_paths_list()    
CONST_COLLECTION = CONST_COLLECTION()


