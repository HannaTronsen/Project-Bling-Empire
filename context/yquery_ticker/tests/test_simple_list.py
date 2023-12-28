import unittest

from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.tests.utils.test_case import TestCase


class test_time_series(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_time_series, self).__init__(*args, **kwargs)

    def test_is_consistently_up_trending(self):
        test_cases = [
            TestCase(series_input=[1, 2, 3], expected_result=True),
            TestCase(series_input=[0, -1, -2, -3], expected_result=False),
            TestCase(series_input=[1, 3, 2], expected_result=False),
            TestCase(series_input=[1, 3], expected_result=True),
            TestCase(series_input=[1, 2, 2, 3, 4, 5], expected_result=True),
            TestCase(series_input=[1, 2, 2, 3, 2, 4, 5], expected_result=False),
            TestCase(series_input=[5, 10, 15, 20, 25, 30], expected_result=True),
            TestCase(series_input=[5, 10, 15, 14, 20, 25, 30], expected_result=False),
            TestCase(series_input=[3.1251e+10, 4.5687e+10, 1.7043e+11], expected_result=True),
            TestCase(series_input=[1.7043e+11, 4.5687e+10, 3.1251e+10], expected_result=False),
            TestCase(series_input=[-2.5687e+10, 1.7043e+11, -1.1251e+10], expected_result=False),
        ]

        for case in test_cases:
            result, _ = TimeSeriesDataCollection.is_consistently_up_trending_simple_list(
                simple_list=case.series_input
            )
            assert result is case.expected_result

        self.assertRaises(ValueError, TimeSeriesDataCollection.is_consistently_up_trending_simple_list, simple_list=[1])

    def test_get_consecutive_upward_trend_interval(self):

        test_cases = [
            # Non-consistently upward trending with 2 decreases
            TestCase(series_input=[0, 1, 4, 3, 4], expected_bool=False, expected_result=2),
            # Non-consistently upward trending with 1 decrease
            TestCase(series_input=[1, 3, 2], expected_bool=False, expected_result=1),
            # Non-consistently upward trending with 1 increase
            TestCase(series_input=[0, -1, -4, -3, -4], expected_bool=False, expected_result=1),
            # Non-consistently upward trending with 2 increases
            TestCase(series_input=[0, -1, -4, -3, -5, -4], expected_bool=False, expected_result=2),
            # Consistently upward trending with length 4
            TestCase(series_input=[1, 2, 3, 4], expected_bool=True, expected_result=[1, 2, 3, 4]),
            # Consistently upward trending with length 7
            TestCase(series_input=[0, 1, 2, 3, 4, 5, 6], expected_bool=True, expected_result=[0, 1, 2, 3, 4, 5, 6]),
            # Consistently flat series
            TestCase(series_input=[5, 5, 5, 5, 5], expected_bool=True, expected_result=[5, 5, 5, 5, 5]),
            # Consistently downward trending with length 4
            TestCase(series_input=[-1, -2, -3, -4], expected_bool=True, expected_result=[-1, -2, -3, -4]),
            # Consistently zero series
            TestCase(series_input=[0, 0, 0, 0, 0, 0], expected_bool=True, expected_result=[0, 0, 0, 0, 0, 0]),
            # Upward trend followed by a decrease
            TestCase(series_input=[10, 5, 2, 1, 0], expected_bool=False, expected_result=1),
        ]

        for case in test_cases:
            result, interval = TimeSeriesDataCollection.is_consistently_up_trending_simple_list(
                simple_list=case.series_input)

            if case.expected_bool is False:
                assert result is case.expected_bool and interval == case.expected_result
            else:
                assert case.series_input == case.expected_result

    def test_passes_percentage_increase_requirements(self):
        test_cases = [
            # 50% of 100 is 50, meets requirement
            TestCase(percentages=[100, 50], percentage_requirement=50, expected_result=True),
            # 51% of 100 is 51, doesn't meet requirement
            TestCase(percentages=[100, 50], percentage_requirement=51, expected_result=False),
            # 49% of 100 is 49, meets requirement
            TestCase(percentages=[100, 50], percentage_requirement=49, expected_result=True),
            # 101% of 100 is 101, doesn't meet requirement
            TestCase(percentages=[100, 50], percentage_requirement=101, expected_result=False),
            # 100% of 100 is 100, doesn't meet requirement
            TestCase(percentages=[100, 50], percentage_requirement=100, expected_result=False),
            # Percentage requirement of 1, none meet
            TestCase(percentages=[33.33, 50, 100, 0], percentage_requirement=1, expected_result=False),
            # 26% of 26.67 is 6.94, meets requirement
            TestCase(percentages=[26.67, 281.82], percentage_requirement=26, expected_result=True),
            # 26.68% of 26.67 is 7.12, doesn't meet requirement
            TestCase(percentages=[26.67, 281.82], percentage_requirement=26.68, expected_result=False),
            # 0% of any value is 0, all meet requirement
            TestCase(percentages=[100, 100, 100], percentage_requirement=0, expected_result=True),
            # 0% of any value is 0, all meet requirement
            TestCase(percentages=[0, 0, 0], percentage_requirement=0, expected_result=True),
            # 1% of any value is greater than 0, none meet
            TestCase(percentages=[0, 0, 0], percentage_requirement=1, expected_result=False),
            # -50% of any value is less than or equal, all meet requirement
            TestCase(percentages=[10, 5, 2.5], percentage_requirement=-50, expected_result=True),
        ]

        for case in test_cases:
            assert TimeSeriesDataCollection.passes_percentage_increase_requirements(
                percentages=case.percentages,
                percentage_requirement=case.percentage_requirement
            ) is case.expected_result

    def test_calculate_percentage_increase_for_data_set(self):
        test_cases = [
            # Percentage change from 1 to 2 is 100%, from 2 to 3 is 50%
            TestCase(series_input=[1, 2, 3], expected_result=[100, 50]),
            # Percentage change from 1 to 3 is 200%
            TestCase(series_input=[1, 3], expected_result=[200]),
            # Percentage change from 1 to 3 is 200%, from 3 to 4.5 is 50%
            TestCase(series_input=[1, 3, 4.5], expected_result=[200, 50]),
            # Percentage change from -3 to -2.2 is 26.67%, from -2.2 to 4 is 281.82%
            TestCase(series_input=[-3, -2.2, 4], expected_result=[26.67, 281.82]),
            # Various percentage changes
            TestCase(series_input=[-3, -2, -1, 0, 1], expected_result=[33.33, 50, 100, 100]),
            # No change, all percentages are 0%
            TestCase(series_input=[0, 0, 0], expected_result=[0, 0]),
            # No change, all percentages are 0%
            TestCase(series_input=[5, 5, 5], expected_result=[0, 0]),
            # Percentage change from 1 to 0 is -100%, from 0 to 1 is 100%
            TestCase(series_input=[1, 0, 1], expected_result=[-100, 100]),
            # Various percentage changes
            TestCase(series_input=[100, 50, 10], expected_result=[-50, -80]),
            # Percentage change from 10 to 50 is 400%, from 50 to 100 is 100%
            TestCase(series_input=[10, 50, 100], expected_result=[400, 100]),
            # Percentage change from 1 to 0 is -100%, followed by no change
            TestCase(series_input=[1, 0, 0, 0], expected_result=[-100, 0, 0]),
            # Percentage change from 1 to 0 is -100%, from 0 to 3 is 300%
            TestCase(series_input=[1, 0, 0, 3], expected_result=[-100, 0, 300]),
        ]

        for case in test_cases:
            assert TimeSeriesDataCollection.calculate_percentage_increase_for_simple_list(
                simple_list=case.series_input
            ) == case.expected_result
