import unittest
import pandas as pd
from context.yquery_ticker.main.classes.yahoo.balance_sheet_data import BalanceSheetData
from context.yquery_ticker.main.const import YQUERY_TEST_PATH
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.balance_sheet import BalanceSheetDataClass
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import PeriodType
from context.yquery_ticker.main.enums.quarter import Quarter


class test_balance_sheet(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_balance_sheet, self).__init__(*args, **kwargs)

        self.annual_balance_sheet_expected_list = [
            BalanceSheetDataClass.mockk(
                asOfDate=Date(year=2019, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
            ),
            BalanceSheetDataClass.mockk(
                asOfDate=Date(year=2020, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
            ),
            BalanceSheetDataClass.mockk(
                asOfDate=Date(year=2021, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
            ),
            BalanceSheetDataClass.mockk(
                asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
            ),
        ]

        self.quarter_balance_sheet_expected_list = [
            BalanceSheetDataClass.mockk(
                asOfDate=Date(year=2022, quarter=Quarter.SECOND_QUARTER),
                periodType=PeriodType.MONTH_3,
            ),
            BalanceSheetDataClass.mockk(
                asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_3,
            ),
            BalanceSheetDataClass.mockk(
                asOfDate=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),
                periodType=PeriodType.MONTH_3,
            ),
            BalanceSheetDataClass.mockk(
                asOfDate=Date(year=2023, quarter=Quarter.FIRST_QUARTER),
                periodType=PeriodType.MONTH_3,
            ),
            BalanceSheetDataClass.mockk(
                asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                periodType=PeriodType.MONTH_3,
            ),
        ]

    def test_convert_data_frame_to_model(self):
        json_file_name = "resources/balance_sheet/aapl.data.balance_sheet.annually.csv"
        data = f'{YQUERY_TEST_PATH}{json_file_name}'

        assert BalanceSheetData.extract_date_time_information(
            entries=BalanceSheetData.convert_data_frame_to_time_series_model(
                data_frame=pd.read_csv(data)
            )
        ) == self.annual_balance_sheet_expected_list

        json_file_name = "resources/balance_sheet/aapl.data.balance_sheet.quarterly.csv"
        data = f'{YQUERY_TEST_PATH}{json_file_name}'

        assert BalanceSheetData.extract_date_time_information(
            entries=BalanceSheetData.convert_data_frame_to_time_series_model(
                data_frame=pd.read_csv(data)
            )
        ) == self.quarter_balance_sheet_expected_list


