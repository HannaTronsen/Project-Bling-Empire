import unittest

from context.yquery_ticker.main.classes.yahoo.historical_earnings_data import HistoricalEarningsData
from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.const import YQUERY_TEST_PATH
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.earnings_history import EarningsHistoryDataClass
from context.yquery_ticker.main.enums.quarter import Quarter
from context.yquery_ticker.tests.utils.test_case import TestCase


class test_earnings_history(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_earnings_history, self).__init__(*args, **kwargs)

        self.aapl_earnings_history_expected_list = [
            EarningsHistoryDataClass(
                epsActual=1.29,
                epsEstimate=1.27,
                epsDifference=0.02,
                quarter=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                asOfDate=None,
                periodType=None
            ),
            EarningsHistoryDataClass(
                epsActual=1.88,
                epsEstimate=1.94,
                epsDifference=-0.06,
                quarter=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),
                asOfDate=None,
                periodType=None
            ),
            EarningsHistoryDataClass(
                epsActual=1.52,
                epsEstimate=1.43,
                epsDifference=0.09,
                quarter=Date(year=2023, quarter=Quarter.FIRST_QUARTER),
                asOfDate=None,
                periodType=None
            ),
            EarningsHistoryDataClass(
                epsActual=1.17,
                epsEstimate=1.11,
                epsDifference=0.06,
                quarter=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                asOfDate=None,
                periodType=None
            )
        ]

        self.earnings_history_up_trending_list = [
            EarningsHistoryDataClass(
                epsActual=1.29,
                epsEstimate=1.27,
                epsDifference=0.02,
                quarter=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                asOfDate=None,
                periodType=None
            ),
            EarningsHistoryDataClass(
                epsActual=1.88,
                epsEstimate=1.94,
                epsDifference=-0.06,
                quarter=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),
                asOfDate=None,
                periodType=None
            ),
            EarningsHistoryDataClass(
                epsActual=1.92,
                epsEstimate=1.43,
                epsDifference=0.09,
                quarter=Date(year=2023, quarter=Quarter.FIRST_QUARTER),
                asOfDate=None,
                periodType=None
            ),
        ]

    def test_convert_data_frame_to_model(self):
        json_file_name = "resources/aapl.data.earnings.csv"
        data = f'{YQUERY_TEST_PATH}{json_file_name}'

        assert HistoricalEarningsData.convert_csv_to_time_series_model(
            csv=data
        ) == self.aapl_earnings_history_expected_list

    def test_is_consistently_up_trending(self):
        test_cases = [
            TestCase(
                model_list=self.aapl_earnings_history_expected_list,
                attribute="epsActual",
                expected_result=False
            ),
            TestCase(
                model_list=self.aapl_earnings_history_expected_list,
                attribute="epsEstimate",
                expected_result=False
            ),
            TestCase(
                model_list=self.aapl_earnings_history_expected_list,
                attribute="epsDifference",
                expected_result=False
            ),
            TestCase(
                model_list=self.earnings_history_up_trending_list,
                attribute="epsActual",
                expected_result=True
            ),
        ]

        for case in test_cases:
            result, _ = TimeSeriesDataCollection.is_consistently_up_trending_model_list(
                model_list=case.model_list,
                attribute=case.attribute
            )
            assert result is case.expected_result
