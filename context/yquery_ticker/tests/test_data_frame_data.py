import unittest
from context.yquery_ticker.main.classes.data_frame_data import DataFrameData
from yahooquery import Ticker

from context.yquery_ticker.main.enums.data_frame import DataFrame

class test_data_frame_data(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_data_frame_data, self).__init__(*args, **kwargs)

    #def tes(self):
    #    DataFrameData().get_column_values(df=Ticker('aapl').income_statement(), column=DataFrame.AS_OF_DATE)