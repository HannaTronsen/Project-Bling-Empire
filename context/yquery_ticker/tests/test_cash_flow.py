import unittest

import pandas as pd
from context.yquery_ticker.main.classes.cash_flow_data import CashFlowData
from context.yquery_ticker.main.const import YQUERY_TEST_PATH


class test_cash_flow(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_cash_flow, self).__init__(*args, **kwargs)

        # self.annual_income_statement_expected_list = [
        #     IncomeStatementDataClass(
        #         asOfDate=Date(year=2019, quarter=Quarter.THIRD_QUARTER),
        #         periodType=PeriodType.MONTH_12,
        #         netIncome=55256000000.0
        #     ),
        #     IncomeStatementDataClass(
        #         asOfDate=Date(year=2020, quarter=Quarter.THIRD_QUARTER),
        #         periodType=PeriodType.MONTH_12,
        #         netIncome=57411000000.0
        #     ),
        #     IncomeStatementDataClass(
        #         asOfDate=Date(year=2021, quarter=Quarter.THIRD_QUARTER),
        #         periodType=PeriodType.MONTH_12,
        #         netIncome=94680000000.0
        #     ),
        #     IncomeStatementDataClass(
        #         asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
        #         periodType=PeriodType.MONTH_12,
        #         netIncome=99803000000.0
        #     ),
        #     IncomeStatementDataClass(
        #         asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
        #         periodType=PeriodType.TTM,
        #         netIncome=94760000000.0
        #     )
        # ]
        #
        # self.quarter_income_statement_expected_list = [
        #     IncomeStatementDataClass(
        #         asOfDate=Date(year=2022, quarter=Quarter.SECOND_QUARTER),
        #         periodType=PeriodType.MONTH_3,
        #         netIncome=19442000000.0
        #     ),
        #     IncomeStatementDataClass(
        #         asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
        #         periodType=PeriodType.MONTH_3,
        #         netIncome=20721000000.0
        #     ),
        #     IncomeStatementDataClass(
        #         asOfDate=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),
        #         periodType=PeriodType.MONTH_3,
        #         netIncome=29998000000.0
        #     ),
        #     IncomeStatementDataClass(
        #         asOfDate=Date(year=2023, quarter=Quarter.FIRST_QUARTER),
        #         periodType=PeriodType.MONTH_3,
        #         netIncome=24160000000.0
        #     ),
        #     IncomeStatementDataClass(
        #         asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
        #         periodType=PeriodType.MONTH_3,
        #         netIncome=19881000000.0
        #     ),
        #     IncomeStatementDataClass(
        #         asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
        #         periodType=PeriodType.TTM,
        #         netIncome=94760000000.0
        #     )
        # ]

    def test_convert_data_frame_to_model(self):
        json_file_name = "resources/cash_flow/aapl.data.cash_flow.annually.csv"
        data = f'{YQUERY_TEST_PATH}{json_file_name}'

        CashFlowData.convert_data_frame_to_time_series_model(
            data_frame=pd.read_csv(data)
        )

    #     assert IncomeStatementData.convert_data_frame_to_time_series_model(
    #         data_frame=pd.read_csv(data)
    #     ) == self.annual_income_statement_expected_list
    #
        json_file_name = "resources/cash_flow/aapl.data.cash_flow.quarterly.csv"
        data = f'{YQUERY_TEST_PATH}{json_file_name}'

        CashFlowData.convert_data_frame_to_time_series_model(
            data_frame=pd.read_csv(data)
        )
    #
    #     assert IncomeStatementData.convert_data_frame_to_time_series_model(
    #         data_frame=pd.read_csv(data)
    #     ) == self.quarter_income_statement_expected_list
