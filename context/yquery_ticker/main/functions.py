import os
import re
import concurrent.futures
from typing import Optional, Dict, List, TextIO
from yahooquery import Ticker

from config import ITERABLE_DATA_SHOW_DEBUG_PRINT
from const import (
    BLACKLISTED_STOCK_TICKERS_PATH,
    CONST_COLLECTION, AUTO_GENERATED_FILE_STRING
)
from context.ticker_scraper.main.classes.stock_collection import StockCollectionClass
from context.yquery_ticker.main.classes.global_stock_data import GlobalStockDataClass
from context.yquery_ticker.main.const import DATA_NOT_AVAILABLE


def passed_yahoo_query_validation_check(ticker_symbol: str, ticker: Ticker) -> bool:
    try:
        if DATA_NOT_AVAILABLE in ticker.summary_detail.get(ticker_symbol) or \
                DATA_NOT_AVAILABLE in ticker.financial_data.get(ticker_symbol) or \
                DATA_NOT_AVAILABLE in ticker.key_stats.get(ticker_symbol) or \
                DATA_NOT_AVAILABLE in ticker.earnings[ticker_symbol] or \
                ticker.earnings.items() == {} or \
                isinstance(ticker.cash_flow(), str) or ticker.cash_flow().empty is True:
            return False
    except Exception as e:
        print(f"Failed yahoo query validation check for ticker: {ticker_symbol} - {e}")
        return False
    return True


def validate_and_get_yahoo_query_ticker_object(ticker_symbol: str) -> Optional[GlobalStockDataClass]:
    yquery_ticker = Ticker(ticker_symbol)
    if passed_yahoo_query_validation_check(ticker_symbol=ticker_symbol, ticker=yquery_ticker):
        return GlobalStockDataClass(
            ticker_symbol=ticker_symbol
        )
    else:
        if ITERABLE_DATA_SHOW_DEBUG_PRINT:
            print(f"Required information for ticker {ticker_symbol} is missing.")
    return None


def _open_or_create_blacklisted_stock_file(stock_collection: str) -> TextIO:
    full_blacklisted_path = BLACKLISTED_STOCK_TICKERS_PATH + stock_collection + ".txt"

    if not os.path.exists(BLACKLISTED_STOCK_TICKERS_PATH):
        os.makedirs(BLACKLISTED_STOCK_TICKERS_PATH)

    if not os.path.exists(full_blacklisted_path):
        with open(full_blacklisted_path, "a+") as file:
            file.write(AUTO_GENERATED_FILE_STRING)

    return open(full_blacklisted_path, "r+")


def get_query_ticker_objects(stock_collection: StockCollectionClass) -> List[GlobalStockDataClass]:
    yquery_tickers: List[GlobalStockDataClass] = []

    blacklisted_stocks_file = _open_or_create_blacklisted_stock_file(stock_collection.stock_index_name)

    blacklisted_stocks_file_content = blacklisted_stocks_file.read()

    stock_tickers_file = open(stock_collection.file_path, "r").readlines()

    stock_collection_tickers: List[GlobalStockDataClass] = []

    for ticker in stock_tickers_file:
        stripped_ticker = ticker.strip()
        if re.search(ticker, blacklisted_stocks_file_content) is None:
            yquery_ticker = Ticker(stripped_ticker)
            if not passed_yahoo_query_validation_check(ticker_symbol=stripped_ticker, ticker=yquery_ticker):
                if ITERABLE_DATA_SHOW_DEBUG_PRINT:
                    print(f"Required information for ticker {stripped_ticker} is missing.")
                blacklisted_stocks_file.write(f"{stripped_ticker}\n")
            else:
                if ITERABLE_DATA_SHOW_DEBUG_PRINT:
                    print(f"Found information for ticker {stripped_ticker}")
                ticker = GlobalStockDataClass(ticker_symbol=stripped_ticker, ticker=yquery_ticker)
                stock_collection_tickers.append(ticker)
        else:
            if ITERABLE_DATA_SHOW_DEBUG_PRINT:
                print(f"Ticker symbol: {stripped_ticker} found in blacklisted stock file and will be skipped")

    yquery_tickers.extend(stock_collection_tickers)
    blacklisted_stocks_file.close()
    return yquery_tickers


def get_grouped_yahoo_query_ticker_objects() -> Dict[StockCollectionClass, List[GlobalStockDataClass]]:
    yquery_tickers: Dict[StockCollectionClass, List[GlobalStockDataClass]] = {}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Create a dictionary to store the future and corresponding stock collection
        futures_to_collections = {
            executor.submit(get_query_ticker_objects, stock_collection): stock_collection
            for stock_collection in CONST_COLLECTION.STCOK_COLLECTION_LIST
        }

        # Iterate over completed futures and retrieve results
        for future in concurrent.futures.as_completed(futures_to_collections):
            stock_collection = futures_to_collections[future]
            try:
                result = future.result()
                yquery_tickers[stock_collection] = result
            except Exception as e:
                print(f"An error occurred while processing {stock_collection}: {e}")
    return yquery_tickers
