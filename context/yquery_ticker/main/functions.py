import csv

from yahooquery import Ticker
import re
from const import (BLACKLISTED_STOCK_TICKERS_PATH, CONST_COLLECTION, GENERATED_CSV_FILES_PATH)
from context.yquery_ticker.main.classes.global_stock_data import GlobalStockDataClass, Section
from context.yquery_ticker.main.data_classes.financial_summary import FinancialSummary
from context.yquery_ticker.main.errors.generic_error import GenericError


def generate_csv_for_ticker(ticker_symbol: str):
    ticker = GlobalStockDataClass(
        ticker_symbol=ticker_symbol
    )
    csv_file = f"{ticker_symbol}.csv"
    with open(f"{GENERATED_CSV_FILES_PATH}/{csv_file}", mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write general stock information section
        writer.writerow([Section.GENERAL_STOCK_INFO.value])
        for key, value in ticker.general_stock_info:
            if not isinstance(value, FinancialSummary) and value is not None and key != "long_business_summary":
                writer.writerow([key.capitalize(), value])
            else:
                if value is None:
                    writer.writerow([f'{key.capitalize()}', "None"])
        writer.writerow([])

        # Write each section
        for section, data_func in ticker.map_section_headers_with_data().items():
            if section == Section.GROWTH_CRITERIA_DATA:
                writer.writerows([[], []])

            writer.writerow([section.value])  # Write section header

            for key, value in data_func().items():
                if not isinstance(value, GenericError) and value is not None:
                    writer.writerow([f'{key.value}', value])
                else:
                    if value is None:
                        writer.writerow([f'{key.value}', "None"])
                    else:
                        error = GenericError(value.reason)
                        writer.writerow([f'{key.value}', error.reason])
            writer.writerow([])


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
