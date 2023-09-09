import unittest

from context.yquery_ticker.main.classes.earnings_history import EarningsAndEarningsHistory
from context.yquery_ticker.main.const import HISTORICAL_EARNINGS_TEST_PATH
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.earnings_history import EarningsHistoryDataClass
from context.yquery_ticker.main.enums.quarter import Quarter


class test_earnings_history(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_earnings_history, self).__init__(*args, **kwargs)

    def test_convert_data_frame_to_model(self):
        json_file_name = "aapl.data.csv"
        data = f'{HISTORICAL_EARNINGS_TEST_PATH}{json_file_name}'

        assert EarningsAndEarningsHistory.convert_csv_to_yq_data_frame_data(csv=data) == [
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
