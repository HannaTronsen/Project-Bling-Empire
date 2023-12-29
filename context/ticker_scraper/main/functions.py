import concurrent.futures

from const import CONST_COLLECTION


def fetch_tickers_for_collection(collection):
    data_frame = collection.fetch_stock_tickers_data_frame()
    collection.save_stock_tickers_data_frame_to_csv(data_frame=data_frame)


def fetch_tickers():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(fetch_tickers_for_collection, collection)
            for collection in CONST_COLLECTION.STCOK_COLLECTION_LIST
        ]
        concurrent.futures.wait(futures)
