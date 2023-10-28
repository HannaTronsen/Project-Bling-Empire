import unittest

import pandas as pd

from context.yquery_ticker.main.classes.yahoo.income_statement_data import IncomeStatementData
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.const import YQUERY_TEST_PATH
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import PeriodType
from context.yquery_ticker.main.enums.quarter import Quarter
from context.yquery_ticker.main.data_classes.yq_data_frame_data.income_statement import IncomeStatementDataClass


class test_income_statement(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_income_statement, self).__init__(*args, **kwargs)

        self.annual_income_statement_expected_list = [
            IncomeStatementDataClass.mockk(
                asOfDate=Date(year=2019, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(year=2020, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(year=2021, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                periodType=PeriodType.TTM,
            )
        ]

        self.quarter_income_statement_expected_list = [
            IncomeStatementDataClass.mockk(
                asOfDate=Date(year=2022, quarter=Quarter.SECOND_QUARTER),
                periodType=PeriodType.MONTH_3,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_3,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),
                periodType=PeriodType.MONTH_3,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(year=2023, quarter=Quarter.FIRST_QUARTER),
                periodType=PeriodType.MONTH_3,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                periodType=PeriodType.MONTH_3,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                periodType=PeriodType.TTM,
            ),
        ]

    def test_convert_data_frame_to_model(self):
        json_file_name = "resources/income_statement/aapl.data.income_statement.annually.csv"
        data = f'{YQUERY_TEST_PATH}{json_file_name}'

        assert IncomeStatementData.extract_date_time_information(
            entries=IncomeStatementData.convert_data_frame_to_time_series_model(
                data_frame=pd.read_csv(data)
            )
        ) == self.annual_income_statement_expected_list

        json_file_name = "resources/income_statement/aapl.data.income_statement.quarterly.csv"
        data = f'{YQUERY_TEST_PATH}{json_file_name}'

        assert IncomeStatementData.extract_date_time_information(
            entries=IncomeStatementData.convert_data_frame_to_time_series_model(
                data_frame=pd.read_csv(data)
            )
        ) == self.quarter_income_statement_expected_list
