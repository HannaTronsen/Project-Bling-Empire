import unittest
from context.yquery_ticker.main.data_classes.charts import Date
from context.yquery_ticker.main.enums.quarter import Quarter, QuarterId


class test_date(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_date, self).__init__(*args, **kwargs)

    def test_convert_date(self):
        # Test valid date conversions
        assert Date.convert_date(value=2022) == Date(year=2022)
        assert Date.convert_date(value="2022") == Date(year=2022)
        assert Date.convert_date(value="3Q2023") == Date(year=2023, quarter=Quarter.from_id(QuarterId.Q3))
        assert Date.convert_date(value="2Q2020") == Date(year=2020, quarter=Quarter.SECOND_QUARTER)
        assert Date.convert_date(value="2Q") == Date(quarter=Quarter.SECOND_QUARTER)
        assert Date.convert_date(value="2q") == Date(quarter=Quarter.SECOND_QUARTER)
        assert Date.convert_date(value="2020-09-30") == Date(year=2020, quarter=Quarter.THIRD_QUARTER)
        assert Date.convert_date(value="2023-01-30") == Date(year=2023, quarter=Quarter.FIRST_QUARTER)

        # Test invalid date conversions (should return None)
        self.assertIsNone(Date.convert_date(value="2023-01-32"))
        self.assertIsNone(Date.convert_date(value="2020-13-30"))
        self.assertIsNone(Date.convert_date(value="2020-0-30"))
        self.assertIsNone(Date.convert_date(value="200-03-30"))
        self.assertIsNone(Date.convert_date(value="2020-00-30"))
        self.assertIsNone(Date.convert_date(value="2020-02"))
        self.assertIsNone(Date.convert_date(value=-2020))
        self.assertIsNone(Date.convert_date(value="-2022"))
        self.assertIsNone(Date.convert_date(value="2022.2"))
        self.assertIsNone(Date.convert_date(value=2022.2))
        self.assertIsNone(Date.convert_date(value="2Q2"))
        self.assertIsNone(Date.convert_date(value="2023Q2"))
        self.assertIsNone(Date.convert_date(value="0Q2023"))
        self.assertIsNone(Date.convert_date(value="5Q2023"))
        self.assertIsNone(Date.convert_date(value="4QQ2023"))
        self.assertIsNone(Date.convert_date(value=None))
        self.assertIsNone(Date.convert_date(value="N/A"))
        self.assertIsNone(Date.convert_date(value=""))
