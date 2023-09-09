import unittest

from context.yquery_ticker.main.classes.historical_earnings_data import HistoricalEarningsData
from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.const import HISTORICAL_EARNINGS_TEST_PATH
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.earnings_history import EarningsHistoryDataClass
from context.yquery_ticker.main.enums.quarter import Quarter


class test_earnings_history(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_earnings_history, self).__init__(*args, **kwargs)

        self.aapl_earnings_history_expected_list = [
            EarningsHistoryDataClass(
                epsActual=1.29,
                epsEstimate=1.27,
                epsDifference=0.02,
                quarter=Date(year=2022, quarter=Quarter.THIRD_QUARTER)
            ),
            EarningsHistoryDataClass(
                epsActual=1.88,
                epsEstimate=1.94,
                epsDifference=-0.06,
                quarter=Date(year=2022, quarter=Quarter.FOURTH_QUARTER)
            ),
            EarningsHistoryDataClass(
                epsActual=1.52,
                epsEstimate=1.43,
                epsDifference=0.09,
                quarter=Date(year=2023, quarter=Quarter.FIRST_QUARTER)
            ),
            EarningsHistoryDataClass(
                epsActual=1.17,
                epsEstimate=1.11,
                epsDifference=0.06,
                quarter=Date(year=2023, quarter=Quarter.SECOND_QUARTER)
            )
        ]

        self.earnings_history_up_trending_list = [
            EarningsHistoryDataClass(
                epsActual=1.29,
                epsEstimate=1.27,
                epsDifference=0.02,
                quarter=Date(year=2022, quarter=Quarter.THIRD_QUARTER)
            ),
            EarningsHistoryDataClass(
                epsActual=1.88,
                epsEstimate=1.94,
                epsDifference=-0.06,
                quarter=Date(year=2022, quarter=Quarter.FOURTH_QUARTER)
            ),
            EarningsHistoryDataClass(
                epsActual=1.92,
                epsEstimate=1.43,
                epsDifference=0.09,
                quarter=Date(year=2023, quarter=Quarter.FIRST_QUARTER)
            ),
        ]

    def test_convert_data_frame_to_model(self):
        json_file_name = "aapl.data.csv"
        data = f'{HISTORICAL_EARNINGS_TEST_PATH}{json_file_name}'

        assert HistoricalEarningsData.convert_csv_to_time_series_model(
            csv=data
        ) == self.aapl_earnings_history_expected_list

    def test_is_consistently_up_trending(self):
        test_cases = [
            # model_list, attribute, expected_result
            (self.aapl_earnings_history_expected_list, 'epsActual', False),
            (self.aapl_earnings_history_expected_list, 'epsEstimate', False),
            (self.aapl_earnings_history_expected_list, 'epsDifference', False),
            (self.earnings_history_up_trending_list, 'epsActual', True),
        ]

        for model_list, attribute, expected_result in test_cases:
            result, _ = TimeSeriesDataCollection.is_consistently_up_trending_model_list(
                model_list=model_list,
                attribute=attribute
            )
            assert result is expected_result
