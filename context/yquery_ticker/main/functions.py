from yahooquery import Ticker
import re
from const import (BLACKLISTED_STOCK_TICKERS_PATH, CONST_COLLECTION)


def put_yahoo_query_ticker_object(ticker):
    # TODO (Hanna)
    pass


def validate_yahoo_query_ticker_objects():
    blacklisted_stocks_file = open(BLACKLISTED_STOCK_TICKERS_PATH, "r+")
    blacklisted_stocks_file_content = blacklisted_stocks_file.read()

    for stock_collection in CONST_COLLECTION.STCOK_COLLECTION_LIST:
        stock_tickers_file = open(stock_collection.file_path, "r").readlines()

        for ticker in stock_tickers_file:

            yquery_ticker = Ticker(ticker.strip())

            if re.search(ticker, blacklisted_stocks_file_content) is not None:
                # Skip for now, will handle this case later
                pass
            elif not bool(yquery_ticker.summary_detail):
                print(f"No information found for ticker '{ticker}'.")
                blacklisted_stocks_file.write(f"{ticker.strip()}\n")
            else:
                put_yahoo_query_ticker_object(ticker.strip())

    blacklisted_stocks_file.close()


def validate_and_get_yahoo_query_ticker_objects():
    validate_yahoo_query_ticker_objects()
