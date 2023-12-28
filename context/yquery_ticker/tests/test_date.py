import unittest
from context.yquery_ticker.main.data_classes.charts import Date
from context.yquery_ticker.main.enums.quarter import Quarter, QuarterId
from context.yquery_ticker.tests.utils.test_case import TestCase


class test_date(unittest.TestCase):

    # TODO (Hanna): "2019-02-29" Add tests for leap year
    # TODO (Hanna): Add tests for different time formats

    def __init__(self, *args, **kwargs):
        super(test_date, self).__init__(*args, **kwargs)

    def test_convert_date(self):
        test_cases = [
            TestCase(date_input=2022, expected_date=Date(year=2022)),
            TestCase(date_input="2022", expected_date=Date(year=2022)),
            TestCase(date_input="3Q2023", expected_date=Date(year=2023, quarter=Quarter.from_id(QuarterId.Q3))),
            TestCase(date_input="2Q2020", expected_date=Date(year=2020, quarter=Quarter.SECOND_QUARTER)),
            TestCase(date_input="2Q", expected_date=Date(quarter=Quarter.SECOND_QUARTER)),
            TestCase(date_input="2q", expected_date=Date(quarter=Quarter.SECOND_QUARTER)),
            TestCase(date_input="2020-09-30", expected_date=Date(year=2020, quarter=Quarter.THIRD_QUARTER)),
            TestCase(date_input="2023-01-30", expected_date=Date(year=2023, quarter=Quarter.FIRST_QUARTER)),
            TestCase(date_input="2025-12-31", expected_date=Date(year=2025, quarter=Quarter.FOURTH_QUARTER)),
            TestCase(date_input="4Q2030", expected_date=Date(year=2030, quarter=Quarter.FOURTH_QUARTER)),
            TestCase(date_input="1Q2021", expected_date=Date(year=2021, quarter=Quarter.FIRST_QUARTER)),
            TestCase(date_input="2021-06-15", expected_date=Date(year=2021, quarter=Quarter.SECOND_QUARTER)),
            TestCase(date_input="2023-03-01", expected_date=Date(year=2023, quarter=Quarter.FIRST_QUARTER)),
            TestCase(date_input="2024-12-01", expected_date=Date(year=2024, quarter=Quarter.FOURTH_QUARTER)),
        ]

        for case in test_cases:
            assert Date.convert_date(date_input=case.date_input) == case.expected_date

        test_cases = [
            TestCase(invalid_date_input="2023-01-32"),
            TestCase(invalid_date_input="2020-13-30"),
            TestCase(invalid_date_input="2020-0-30"),
            TestCase(invalid_date_input="200-03-30"),
            TestCase(invalid_date_input="2020-00-30"),
            TestCase(invalid_date_input="2020-02"),
            TestCase(invalid_date_input=-2020),
            TestCase(invalid_date_input="-2022"),
            TestCase(invalid_date_input="2022.2"),
            TestCase(invalid_date_input=2022.2),
            TestCase(invalid_date_input="2Q2"),
            TestCase(invalid_date_input="2023Q2"),
            TestCase(invalid_date_input="0Q2023"),
            TestCase(invalid_date_input="5Q2023"),
            TestCase(invalid_date_input="4QQ2023"),
            TestCase(invalid_date_input=None),
            TestCase(invalid_date_input="N/A"),
            TestCase(invalid_date_input=""),
        ]

        for case in test_cases:
            self.assertIsNone(Date.convert_date(date_input=case.invalid_date_input))
