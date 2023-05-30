import datetime
import unittest
from context.yquery_ticker.main.classes.historical_earnings import HistoricalEarnings
from context.yquery_ticker.main.data_classes.charts import Date
from context.yquery_ticker.main.enums.quarter import Quarter, QuarterId

class test_histoical_earnings(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_histoical_earnings, self).__init__(*args, **kwargs)

    
    def test_convert_date(self):
        assert HistoricalEarnings.convert_date(value=2022) == Date(year=2022)
        assert HistoricalEarnings.convert_date(value="2022") == Date(year=2022)
        assert HistoricalEarnings.convert_date(value="3Q2023") == Date(year=2023, quarter=Quarter.from_id(QuarterId.Q3))
        assert HistoricalEarnings.convert_date(value="2Q2020") == Date(year=2020, quarter=Quarter.SECOND_QUARTER)
        assert HistoricalEarnings.convert_date(value="2Q") == Date(year=datetime.datetime.year, quarter=Quarter.SECOND_QUARTER)
        assert HistoricalEarnings.convert_date(value="2q") == Date(year=datetime.datetime.year, quarter=Quarter.SECOND_QUARTER)
        self.assertIsNone(HistoricalEarnings.convert_date(value="2022.2"))
        self.assertIsNone(HistoricalEarnings.convert_date(value=2022.2))
        self.assertIsNone(HistoricalEarnings.convert_date(value="2Q2"))
        self.assertIsNone(HistoricalEarnings.convert_date(value="2023Q2"))
        self.assertIsNone(HistoricalEarnings.convert_date(value="0Q2023"))
        self.assertIsNone(HistoricalEarnings.convert_date(value="5Q2023"))
        self.assertIsNone(HistoricalEarnings.convert_date(value="4QQ2023"))
        self.assertIsNone(HistoricalEarnings.convert_date(value=None))
        self.assertIsNone(HistoricalEarnings.convert_date(value="N/A"))
        self.assertIsNone(HistoricalEarnings.convert_date(value=""))
