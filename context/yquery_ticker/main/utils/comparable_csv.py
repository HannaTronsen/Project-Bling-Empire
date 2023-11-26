import csv
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from enum import Enum
from const import GENERATED_CSV_FILES_PATH, OBEX_COMPARISON_CSV_FILES_PATH
from context.yquery_ticker.main.classes.global_stock_data import GlobalStockDataClass
from context.yquery_ticker.main.enums.currency import Currency

GENERATE_INDIVIDUAL_TICKER_CSV = True


class Headers(Enum):
    TICKER = "TICKER"
    COMPANY = "COMPANY"
    WEBSITE = "WEBSITE"
    INDUSTRY = "INDUSTRY"
    SECTOR = "SECTOR"
    PRICE = "PRICE"
    CURRENCY = "CURRENCY"
    CRITERIA_PASS_COUNT = "CRITERIA PASSED"


class ComparableCSV:
    def __init__(self, tickers: list[GlobalStockDataClass]):
        self.tickers = tickers

    def create(self):
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
            writer.writerow([header.value for header in Headers])
            for ticker in self.tickers:
                if GENERATE_INDIVIDUAL_TICKER_CSV:
                    with ThreadPoolExecutor() as executor:
                        executor.submit(ticker.to_csv())
                ticker_symbol = ticker.general_stock_info.ticker
                company_name = ticker.general_stock_info.company
                website = ticker.general_stock_info.website
                industry = ticker.general_stock_info.industry
                sector = ticker.general_stock_info.sector
                price = ticker.financial_data.price
                criteria_pass_count = ticker.criteria_pass_count

                writer.writerow([
                    ticker_symbol,
                    company_name,
                    website,
                    industry,
                    sector,
                    price,
                    Currency.NOK.value,
                    criteria_pass_count,
                ])
        file.close()
