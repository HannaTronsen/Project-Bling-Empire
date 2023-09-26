import unittest
import pandas as pd
from context.yquery_ticker.main.classes.cash_flow_data import CashFlowData
from context.yquery_ticker.main.const import YQUERY_TEST_PATH
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.cash_flow import CashFlowDataClass
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import PeriodType
from context.yquery_ticker.main.enums.quarter import Quarter


class test_cash_flow(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_cash_flow, self).__init__(*args, **kwargs)

        self.annual_cash_flow_expected_list = [
            CashFlowDataClass(
                asOfDate=Date(year=2019, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
                cashDividendsPaid=-14119000000.0
            ),
            CashFlowDataClass(
                asOfDate=Date(year=2020, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
                cashDividendsPaid=-14081000000.0
            ),
            CashFlowDataClass(
                asOfDate=Date(year=2021, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
                cashDividendsPaid=-14467000000.0
            ),
            CashFlowDataClass(
                asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_12,
                cashDividendsPaid=-14841000000.0
            ),
            CashFlowDataClass(
                asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                periodType=PeriodType.TTM,
                cashDividendsPaid=-14970000000.0
            ),
        ]

        self.quarter_cash_flow_expected_list = [
            CashFlowDataClass(
                asOfDate=Date(year=2022, quarter=Quarter.SECOND_QUARTER),
                periodType=PeriodType.MONTH_3,
                cashDividendsPaid=-3811000000.0
            ),
            CashFlowDataClass(
                asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                periodType=PeriodType.MONTH_3,
                cashDividendsPaid=-3703000000.0
            ),
            CashFlowDataClass(
                asOfDate=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),
                periodType=PeriodType.MONTH_3,
                cashDividendsPaid=-3768000000.0
            ),
            CashFlowDataClass(
                asOfDate=Date(year=2023, quarter=Quarter.FIRST_QUARTER),
                periodType=PeriodType.MONTH_3,
                cashDividendsPaid=-3650000000.0
            ),
            CashFlowDataClass(
                asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                periodType=PeriodType.MONTH_3,
                cashDividendsPaid=-3849000000.0

            ),
            CashFlowDataClass(
                asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                periodType=PeriodType.TTM,
                cashDividendsPaid=-14970000000.0

            ),
        ]

    def test_convert_data_frame_to_model(self):
        json_file_name = "resources/cash_flow/aapl.data.cash_flow.annually.csv"
        data = f'{YQUERY_TEST_PATH}{json_file_name}'

        assert CashFlowData.convert_data_frame_to_time_series_model(
            data_frame=pd.read_csv(data)
        ) == self.annual_cash_flow_expected_list

        json_file_name = "resources/cash_flow/aapl.data.cash_flow.quarterly.csv"
        data = f'{YQUERY_TEST_PATH}{json_file_name}'

        assert CashFlowData.convert_data_frame_to_time_series_model(
            data_frame=pd.read_csv(data)
        ) == self.quarter_cash_flow_expected_list
