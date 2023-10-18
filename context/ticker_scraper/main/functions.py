from const import (
    CONST_COLLECTION
)


def fetch_tickers():
    for collection in CONST_COLLECTION.STCOK_COLLECTION_LIST:
        data_frame = collection.fetch_stock_tickers_data_frame()
        collection.save_stock_tickers_data_frame_to_csv(data_frame=data_frame)
