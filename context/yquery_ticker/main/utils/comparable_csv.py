import csv
import os
from concurrent.futures import ThreadPoolExecutor
from enum import Enum
from typing import Dict, List

from config import TIME_STAMP
from const import GENERATED_CSV_FILES_PATH
from context.ticker_scraper.main.classes.stock_collection import StockCollectionClass
from context.yquery_ticker.main.classes.global_stock_data import YahooStockDataClass, SimpleStockDataClass

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
    def __init__(self, stock_collection: Dict[StockCollectionClass, List[YahooStockDataClass | SimpleStockDataClass]]):
        self.stock_collection = stock_collection

    def create(self):

        for collection in self.stock_collection.keys():

            pathPrefix = f'{GENERATED_CSV_FILES_PATH}{collection.stock_index_name}/comparison/{TIME_STAMP}/'
            if not os.path.exists(pathPrefix):
                os.makedirs(pathPrefix)
            with open(file=f"{pathPrefix}ticker_comparison_by_criteria.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([header.value for header in Headers])

                if len(self.stock_collection[collection]) > 0:
                    first_stock = self.stock_collection[collection][0]
                    if isinstance(first_stock, YahooStockDataClass):
                        self._create_from_tickers(collection=collection, writer=writer)
                    elif isinstance(first_stock, SimpleStockDataClass):
                        self._create_from_csv_files(collection=collection, writer=writer)

            file.close()

    def _create_from_tickers(self, collection: StockCollectionClass, writer: csv.writer):
        sorted_collection: list[YahooStockDataClass] = sorted(
            self.stock_collection[collection],
            key=lambda stock_ticker: stock_ticker.criteria_pass_count,
            reverse=True
        )

        for ticker in sorted_collection:
            # if GENERATE_INDIVIDUAL_TICKER_CSV and not os.path.exists(
            #         f'{GENERATED_CSV_FILES_PATH}{collection.stock_index_name}/comparison/{TIME_STAMP}/'
            # ):
            if GENERATE_INDIVIDUAL_TICKER_CSV:
                with ThreadPoolExecutor() as executor:
                    executor.submit(ticker.to_csv(stock_collection=collection.stock_index_name))

            currency = ticker.general_stock_info.financial_summary.currency

            writer.writerow([
                ticker.general_stock_info.ticker,
                ticker.general_stock_info.company,
                ticker.general_stock_info.website,
                ticker.general_stock_info.industry,
                ticker.general_stock_info.sector,
                ticker.financial_data.price,
                currency.value if currency is not None else collection.get_default_currency(),
                ticker.criteria_pass_count,
            ])

    def _create_from_csv_files(self, collection: StockCollectionClass, writer: csv.writer):
        sorted_collection: list[SimpleStockDataClass] = sorted(
            self.stock_collection[collection],
            key=lambda stock_ticker: stock_ticker.criteria_pass_count,
            reverse=True
        )

        for ticker in sorted_collection:
            writer.writerow([
                ticker.ticker_symbol,
                ticker.company,
                ticker.website,
                ticker.industry,
                ticker.sector,
                ticker.price,
                ticker.currency,
                ticker.criteria_pass_count,
            ])
