import unittest
import pandas as pd
from context.yquery_ticker.main.classes.balance_sheet_data import BalanceSheetData
from context.yquery_ticker.main.const import YQUERY_TEST_PATH
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.balance_sheet import BalanceSheetDataClass
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import PeriodType
from context.yquery_ticker.main.enums.quarter import Quarter


class test_balance_sheet(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_balance_sheet, self).__init__(*args, **kwargs)

        self.annual_balance_sheet_expected_list = [
            BalanceSheetDataClass(
                asOfDate=Date(year=2019, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
                commonStockEquity=90488000000.0
            ),
            BalanceSheetDataClass(
                asOfDate=Date(year=2020, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
                commonStockEquity=65339000000.0
            ),
            BalanceSheetDataClass(
                asOfDate=Date(year=2021, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
                commonStockEquity=63090000000.0
            ),
            BalanceSheetDataClass(
                asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
                commonStockEquity=50672000000.0
            ),
        ]

        self.quarter_balance_sheet_expected_list = [
            BalanceSheetDataClass(
                asOfDate=Date(year=2022, quarter=Quarter.SECOND_QUARTER),
                periodType=PeriodType.MONTH_3,
                commonStockEquity=58107000000.0
            ),
            BalanceSheetDataClass(
                asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_3,
                commonStockEquity=50672000000.0
            ),
            BalanceSheetDataClass(
                asOfDate=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),
                periodType=PeriodType.MONTH_3,
                commonStockEquity=56727000000.0
            ),
            BalanceSheetDataClass(
                asOfDate=Date(year=2023, quarter=Quarter.FIRST_QUARTER),
                periodType=PeriodType.MONTH_3,
                commonStockEquity=62158000000.0
            ),
            BalanceSheetDataClass(
                asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                periodType=PeriodType.MONTH_3,
                commonStockEquity=60274000000.0
            ),
        ]

    def test_convert_data_frame_to_model(self):
        json_file_name = "resources/balance_sheet/aapl.data.balance_sheet.annually.csv"
        data = f'{YQUERY_TEST_PATH}{json_file_name}'

        assert BalanceSheetData.convert_data_frame_to_time_series_model(
            data_frame=pd.read_csv(data)
        ) == self.annual_balance_sheet_expected_list

        json_file_name = "resources/balance_sheet/aapl.data.balance_sheet.quarterly.csv"
        data = f'{YQUERY_TEST_PATH}{json_file_name}'

        assert BalanceSheetData.convert_data_frame_to_time_series_model(
            data_frame=pd.read_csv(data)
        ) == self.quarter_balance_sheet_expected_list
