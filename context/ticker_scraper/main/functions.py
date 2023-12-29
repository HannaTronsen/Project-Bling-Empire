import concurrent.futures
import os

from config import USE_OPTIMIZED_ALGORITHM, TIME_STAMP
from const import CONST_COLLECTION, GENERATED_CSV_FILES_PATH


def fetch_tickers_for_collection(collection):
    data_frame = collection.fetch_stock_tickers_data_frame()
    collection.save_stock_tickers_data_frame_to_csv(data_frame=data_frame)


def fetch_tickers():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(fetch_tickers_for_collection if USE_OPTIMIZED_ALGORITHM and os.path.exists(
                f'{GENERATED_CSV_FILES_PATH}{collection.stock_index_name}/comparison/{TIME_STAMP}/'
            ) else None, collection)
            for collection in CONST_COLLECTION.STCOK_COLLECTION_LIST
        ]
        concurrent.futures.wait(futures)
