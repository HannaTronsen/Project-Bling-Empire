import csv
import os
import re
from datetime import datetime
from typing import Optional
from yahooquery import Ticker
from config import GENERATE_DEV_CSV, GENERATE_PROD_CSV
from const import (
    BLACKLISTED_STOCK_TICKERS_PATH,
    CONST_COLLECTION,
    GENERATED_CSV_FILES_PATH,
    OBEX_COMPARISON_CSV_FILES_PATH
)
from context.yquery_ticker.main.classes.global_stock_data import GlobalStockDataClass, Section
from context.yquery_ticker.main.data_classes.financial_summary import FinancialSummary
from context.yquery_ticker.main.enums.growth_criteria import GrowthCriteria
from context.yquery_ticker.main.errors.generic_error import GenericError


def passed_yahoo_query_validation_check(ticker_symbol: str, ticker: Ticker) -> bool:
    try:
        if "Quote not found for ticker symbol" in ticker.summary_detail.get(ticker_symbol) or \
                "Quote not found for ticker symbol" in ticker.financial_data.get(ticker_symbol) or \
                "Quote not found for ticker symbol" in ticker.key_stats.get(ticker_symbol) or \
                ticker.earnings.items() == {} or \
                ticker.cash_flow().empty:
            return False
    except Exception as e:
        print(f"Failed yahoo query validation check for ticker: {ticker_symbol} - {e}")
        return False
    return True


def generate_csv_for_ticker(ticker_symbol: str, ticker: GlobalStockDataClass):
    if GENERATE_DEV_CSV or GENERATE_PROD_CSV:
        with open(f"{GENERATED_CSV_FILES_PATH}/{ticker_symbol}.csv", mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write general stock information section
            writer.writerow([Section.GENERAL_STOCK_INFO.value])
            for key, value in ticker.general_stock_info:
                if not isinstance(value, FinancialSummary) and value is not None and key != "long_business_summary":
                    writer.writerow([key.capitalize(), value])
                else:
                    if value is None:
                        writer.writerow([key.capitalize(), "None"])
            writer.writerow([])

            # Write each section
            for section, data_func in ticker.map_section_headers_with_data().items():
                if section == Section.GROWTH_CRITERIA:
                    writer.writerows([[], []])

                writer.writerow([section.value])  # Write section header

                for key, value in data_func().items():
                    if not isinstance(value, GenericError) and value is not None:
                        writer.writerow([key, value])
                    else:
                        if value is None:
                            writer.writerow([key, "None"])
                        else:
                            error = GenericError(value.reason)
                            writer.writerow([key, error.reason])
                writer.writerow([])
            writer.writerows([[], []])
            writer.writerow(["CRITERIA PASS COUNT", ticker.criteria_pass_count])
        file.close()


def generate_comparable_csv_for_tickers(tickers: list[GlobalStockDataClass]):
    if GENERATE_DEV_CSV or GENERATE_PROD_CSV:
        print("generating comparable csv for tickers")
        time_stamp = datetime.now().strftime("%Y-%m-%d")
        pathPrefix = f'{GENERATED_CSV_FILES_PATH}{OBEX_COMPARISON_CSV_FILES_PATH}{time_stamp}/'
        if not os.path.exists(pathPrefix):
            os.makedirs(pathPrefix)
        with open(
                file=f"{pathPrefix}ticker_comparison_by_criteria.csv",
                mode='w',
                newline=''
        ) as file:
            writer = csv.writer(file)
            writer.writerow(["TICKER", "COMPANY", "WEBSITE", "INDUSTRY", "SECTOR", "CRITERIA PASSED"])
            for ticker in tickers:
                ticker_symbol = ticker.general_stock_info.ticker
                company_name = ticker.general_stock_info.company
                website = ticker.general_stock_info.website
                industry = ticker.general_stock_info.industry
                sector = ticker.general_stock_info.sector
                criteria_pass_count = ticker.criteria_pass_count

                writer.writerow([
                    ticker_symbol,
                    company_name,
                    website,
                    industry,
                    sector,
                    criteria_pass_count,
                ])
        file.close()


def validate_and_get_yahoo_query_ticker_object(ticker_symbol: str) -> Optional[GlobalStockDataClass]:
    yquery_ticker = Ticker(ticker_symbol)
    if passed_yahoo_query_validation_check(ticker_symbol=ticker_symbol, ticker=yquery_ticker):
        ticker = GlobalStockDataClass(
            ticker_symbol=ticker_symbol
        )
        generate_csv_for_ticker(ticker_symbol=ticker_symbol, ticker=ticker)
        return ticker
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
                    generate_csv_for_ticker(ticker_symbol=stripped_ticker, ticker=ticker)
                    yquery_tickers.append(ticker)
            else:
                print(f"Ticker symbol: {stripped_ticker} found in blacklisted stock file and will be skipped")
    blacklisted_stocks_file.close()
    return yquery_tickers
