import json
import unittest

from context.yquery_ticker.main.classes.yq_data_frame_data import YQDataFrameData
from context.yquery_ticker.main.const import HISTORICAL_EARNINGS_TEST_PATH


class test_data_frame_data(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_data_frame_data, self).__init__(*args, **kwargs)

    @staticmethod
    def convert_data_fra_to_models(self):
        json_file_name = "aapl.data.csv"
        data = json.loads(open(f'{HISTORICAL_EARNINGS_TEST_PATH}{json_file_name}').read())

        pass

    # def test(self):
    #
    #     DataFrameData.get_column_values(
    #         df=Ticker('aapl')
    #         .income_statement(),
    #         column=DataFrame.AS_OF_DATE)
