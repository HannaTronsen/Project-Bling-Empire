from const import (
    CONST_COLLECTION
)


def fetch_tickers():
    for collection in CONST_COLLECTION.STCOK_COLLECTION_LIST:
        collection.fetch_stock_tickers()
