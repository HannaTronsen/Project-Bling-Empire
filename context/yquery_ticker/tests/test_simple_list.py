import unittest

from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection


class test_time_series(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_time_series, self).__init__(*args, **kwargs)

    def test_is_consistently_up_trending(self):
        test_cases = [
            # series_input, expected_result
            ([1, 2, 3], True),  # Simple ascending sequence
            ([0, -1, -2, -3], False),  # Simple descending sequence
            ([1, 3, 2], False),  # Not consistently trending up
            ([1, 3], True),  # Only two points, but ascending
            ([1, 2, 2, 3, 4, 5], True),  # Ascending with a plateau
            ([1, 2, 2, 3, 2, 4, 5], False),  # Plateau broken by a decrease
            ([5, 10, 15, 20, 25, 30], True),  # Larger increments
            ([5, 10, 15, 14, 20, 25, 30], False),  # Decrease in the middle
            ([3.1251e+10, 4.5687e+10, 1.7043e+11], True),  # Decrease in the middle
            ([1.7043e+11, 4.5687e+10, 3.1251e+10], False),  # Decrease in the middle
            ([-2.5687e+10, 1.7043e+11, -1.1251e+10], False)
        ]

        for series_input, expected_result in test_cases:
            result, _ = TimeSeriesDataCollection.is_consistently_up_trending_simple_list(
                simple_list=series_input
            )
            assert result is expected_result

        self.assertRaises(ValueError, TimeSeriesDataCollection.is_consistently_up_trending_simple_list, simple_list=[1])

    def test_get_consecutive_upward_trend_interval(self):
        test_cases = [
            # series_input, expected_bool, expected_output
            ([0, 1, 4, 3, 4], False, 2),  # Non-consistently upward trending with 2 decreases
            ([1, 3, 2], False, 1),  # Non-consistently upward trending with 1 decrease
            ([0, -1, -4, -3, -4], False, 1),  # Non-consistently upward trending with 1 increase
            ([0, -1, -4, -3, -5, -4], False, 2),  # Non-consistently upward trending with 2 increases
            ([1, 2, 3, 4], True, [1, 2, 3, 4]),  # Consistently upward trending with length 4
            ([0, 1, 2, 3, 4, 5, 6], True, [0, 1, 2, 3, 4, 5, 6]),  # Consistently upward trending with length 7
            ([5, 5, 5, 5, 5], True, [5, 5, 5, 5, 5]),  # Consistently flat series
            ([-1, -2, -3, -4], True, [-1, -2, -3, -4]),  # Consistently downward trending with length 4
            ([0, 0, 0, 0, 0, 0], True, [0, 0, 0, 0, 0, 0]),  # Consistently zero series
            ([10, 5, 2, 1, 0], False, 1),  # Upward trend followed by a decrease
        ]

        for series_input, expected_bool, expected_output in test_cases:
            result, interval = TimeSeriesDataCollection.is_consistently_up_trending_simple_list(
                simple_list=series_input)

            if expected_bool is False:
                assert result is expected_bool and interval == expected_output
            else:
                assert series_input == expected_output

    def test_passes_percentage_increase_requirements(self):
        test_cases = [
            # percentages, percentage_requirement, expected_output
            ([100, 50], 50, True),  # 50% of 100 is 50, meets requirement
            ([100, 50], 51, False),  # 51% of 100 is 51, doesn't meet requirement
            ([100, 50], 49, True),  # 49% of 100 is 49, meets requirement
            ([100, 50], 101, False),  # 101% of 100 is 101, doesn't meet requirement
            ([100, 50], 100, False),  # 100% of 100 is 100, doesn't meet requirement
            ([33.33, 50, 100, 0], 1, False),  # Percentage requirement of 1, none meet
            ([26.67, 281.82], 26, True),  # 26% of 26.67 is 6.94, meets requirement
            ([26.67, 281.82], 26.68, False),  # 26.68% of 26.67 is 7.12, doesn't meet requirement
            ([100, 100, 100], 0, True),  # 0% of any value is 0, all meet requirement
            ([0, 0, 0], 0, True),  # 0% of any value is 0, all meet requirement
            ([0, 0, 0], 1, False),  # 1% of any value is greater than 0, none meet
            ([10, 5, 2.5], -50, True),  # -50% of any value is less than or equal, all meet requirement
        ]

        for percentages, percentage_requirement, expected_output in test_cases:
            assert TimeSeriesDataCollection.passes_percentage_increase_requirements(
                percentages=percentages,
                percentage_requirement=percentage_requirement
            ) is expected_output

    def test_calculate_percentage_increase_for_data_set(self):
        test_cases = [
            # series_input, expected_result
            ([1, 2, 3], [100, 50]),  # Percentage change from 1 to 2 is 100%, from 2 to 3 is 50%
            ([1, 3], [200]),  # Percentage change from 1 to 3 is 200%
            ([1, 3, 4.5], [200, 50]),  # Percentage change from 1 to 3 is 200%, from 3 to 4.5 is 50%
            ([-3, -2.2, 4], [26.67, 281.82]),  # Percentage change from -3 to -2.2 is 26.67%, from -2.2 to 4 is 281.82%
            ([-3, -2, -1, 0, 1], [33.33, 50, 100, 100]),  # Various percentage changes
            ([0, 0, 0], [0, 0]),  # No change, all percentages are 0%
            ([5, 5, 5], [0, 0]),  # No change, all percentages are 0%
            ([1, 0, 1], [-100, 100]),  # Percentage change from 1 to 0 is -100%, from 0 to 1 is 100%
            ([100, 50, 10], [-50, -80]),  # Various percentage changes
            ([10, 50, 100], [400, 100]),  # Percentage change from 10 to 50 is 400%, from 50 to 100 is 100%
            ([1, 0, 0, 0], [-100, 0, 0]),  # Percentage change from 1 to 0 is -100%, followed by no change
            ([1, 0, 0, 3], [-100, 0, 300])  # Percentage change from 1 to 0 is -100%, from 0 to 3 is 300%
        ]

        for series_input, expected_result in test_cases:
            assert TimeSeriesDataCollection.calculate_percentage_increase_for_simple_list(
                simple_list=series_input
            ) == expected_result
