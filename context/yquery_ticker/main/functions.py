import re
from typing import Optional
from yahooquery import Ticker
from const import (
    BLACKLISTED_STOCK_TICKERS_PATH,
    CONST_COLLECTION
)
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
        print(f"Required information for ticker {ticker_symbol} is missing.")
    return None


def validate_and_get_yahoo_query_ticker_objects() -> list[GlobalStockDataClass]:
    blacklisted_stocks_file = open(BLACKLISTED_STOCK_TICKERS_PATH, "r+")
    blacklisted_stocks_file_content = blacklisted_stocks_file.read()
    yquery_tickers: list[GlobalStockDataClass] = []

    for stock_collection in CONST_COLLECTION.STCOK_COLLECTION_LIST:
        stock_tickers_file = open(stock_collection.file_path, "r").readlines()

        for ticker in stock_tickers_file:
            stripped_ticker = ticker.strip()
            if re.search(ticker, blacklisted_stocks_file_content) is None:
                yquery_ticker = Ticker(stripped_ticker)
                if not passed_yahoo_query_validation_check(ticker_symbol=stripped_ticker, ticker=yquery_ticker):
                    print(f"Required information for ticker {stripped_ticker} is missing.")
                    blacklisted_stocks_file.write(f"{stripped_ticker}\n")
                else:
                    print(f"Found information for ticker {stripped_ticker}")
                    ticker = GlobalStockDataClass(ticker_symbol=stripped_ticker, ticker=yquery_ticker)
                    yquery_tickers.append(ticker)
            else:
                print(f"Ticker symbol: {stripped_ticker} found in blacklisted stock file and will be skipped")
    blacklisted_stocks_file.close()
    return yquery_tickers
