import unittest
from context.yquery_ticker.main.data_classes.charts import Date
from context.yquery_ticker.main.enums.quarter import Quarter, QuarterId


class test_date(unittest.TestCase):

    # TODO (Hanna): "2019-02-29" Add tests for leap year

    def __init__(self, *args, **kwargs):
        super(test_date, self).__init__(*args, **kwargs)

    def test_convert_date(self):
        test_cases = [
            # date_input, expected_date
            (2022, Date(year=2022)),
            ("2022", Date(year=2022)),
            ("3Q2023", Date(year=2023, quarter=Quarter.from_id(QuarterId.Q3))),
            ("2Q2020", Date(year=2020, quarter=Quarter.SECOND_QUARTER)),
            ("2Q", Date(quarter=Quarter.SECOND_QUARTER)),
            ("2q", Date(quarter=Quarter.SECOND_QUARTER)),
            ("2020-09-30", Date(year=2020, quarter=Quarter.THIRD_QUARTER)),
            ("2023-01-30", Date(year=2023, quarter=Quarter.FIRST_QUARTER)),
            ("2025-12-31", Date(year=2025, quarter=Quarter.FOURTH_QUARTER)),
            ("4Q2030", Date(year=2030, quarter=Quarter.FOURTH_QUARTER)),
            ("1Q2021", Date(year=2021, quarter=Quarter.FIRST_QUARTER)),
            ("2021-06-15", Date(year=2021, quarter=Quarter.SECOND_QUARTER)),
            ("2023-03-01", Date(year=2023, quarter=Quarter.FIRST_QUARTER)),
            ("2024-12-01", Date(year=2024, quarter=Quarter.FOURTH_QUARTER)),
        ]

        for date_input, expected_date in test_cases:
            assert Date.convert_date(date_input=date_input) == expected_date

        test_cases = [
            "2023-01-32",
            "2020-13-30",
            "2020-0-30",
            "200-03-30",
            "2020-00-30",
            "2020-02",
            -2020,
            "-2022",
            "2022.2",
            2022.2,
            "2Q2",
            "2023Q2",
            "0Q2023",
            "5Q2023",
            "4QQ2023",
            None,
            "N/A",
            "",
        ]

        for date_input in test_cases:
            self.assertIsNone(Date.convert_date(date_input=date_input))
