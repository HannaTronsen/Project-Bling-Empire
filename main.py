import csv
import unittest

from yahooquery import Ticker

from const import TEST_PATHS, GENERATED_CSV_FILES_PATH
from context.ticker_scraper.main.functions import fetch_tickers, initialize_environment
from context.yquery_ticker.main.classes.global_stock_data import GlobalStockDataClass, Section
from context.yquery_ticker.main.data_classes.financial_summary import FinancialSummary
from context.yquery_ticker.main.errors.generic_error import GenericError
from context.yquery_ticker.main.functions import validate_and_get_yahoo_query_ticker_objects

RUN_TESTS = False
RUN_PROD_CODE = False
RUN_DEV_CODE = True


# Will be removed when all relevant testing csv files have been created
def create_testing_csv():
    aaplDataFrame = Ticker("aapl").cash_flow(frequency="a", trailing=True)
    file_path = "context/yquery_ticker/tests/resources/cash_flow/aapl.data.cash_flow.annually.csv"
    aaplDataFrame.to_csv(file_path, index=False)


def main():
    initialize_environment()
    fetch_tickers()
    validate_and_get_yahoo_query_ticker_objects()


if __name__ == '__main__':

    if RUN_TESTS:
        test_suite = unittest.TestSuite()
        for path in TEST_PATHS:
            test_loader = unittest.TestLoader()
            test_suite.addTest(test_loader.discover(path))

        unittest.TextTestRunner().run(test_suite)

    if RUN_DEV_CODE:

        ticker_symbol = "ACR.OL"
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

    if RUN_PROD_CODE:
        main()
