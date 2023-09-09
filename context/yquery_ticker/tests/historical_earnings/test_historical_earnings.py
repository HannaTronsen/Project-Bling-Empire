import json
import unittest
from context.yquery_ticker.main.classes.earnings_history import EarningsHistory
from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.const import HISTORICAL_EARNINGS_TEST_PATH
from context.yquery_ticker.main.enums.quarter import Quarter
from context.yquery_ticker.main.data_classes.charts import (
    Date,
    QuarterlyEarningsDataChart,
    QuarterlyFinancialsDataChart,
    YearlyFinancialsDataChart
)


class test_historical_earnings(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(test_historical_earnings, self).__init__(*args, **kwargs)

        self.quarterly_earnings_data_up_trending_list = [
            QuarterlyEarningsDataChart(
                date=Date(year=2022, quarter=Quarter.SECOND_QUARTER),
                actual=1.2,
                estimate=1.16
            ),
            QuarterlyEarningsDataChart(
                date=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                actual=1.29,
                estimate=1.27
            ),
            QuarterlyEarningsDataChart(
                date=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),
                actual=1.88,
                estimate=1.94
            ),
            QuarterlyEarningsDataChart(
                date=Date(year=2023, quarter=Quarter.FIRST_QUARTER),
                actual=1.92,
                estimate=2
            )
        ]
        self.quarterly_earnings_data_dip_in_up_trend_list = [
            QuarterlyEarningsDataChart(
                date=Date(year=2022, quarter=Quarter.SECOND_QUARTER),
                actual=1.2,
                estimate=1.94
            ),
            QuarterlyEarningsDataChart(
                date=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                actual=1.1,
                estimate=1.95
            ),
            QuarterlyEarningsDataChart(
                date=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),
                actual=1.88,
                estimate=1.94
            ),
            QuarterlyEarningsDataChart(
                date=Date(year=2023, quarter=Quarter.FIRST_QUARTER),
                actual=1.92, estimate=2.0
            )
        ]
        self.negative_quarterly_earnings_data_dip_in_up_trend_list = [
            QuarterlyEarningsDataChart(
                date=Date(year=2022, quarter=Quarter.SECOND_QUARTER),
                actual=-1.2,
                estimate=-1.94
            ),
            QuarterlyEarningsDataChart(
                date=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                actual=-1.1,
                estimate=-1.95
            ),
            QuarterlyEarningsDataChart(
                date=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),
                actual=-1.88,
                estimate=-1.94
            ),
            QuarterlyEarningsDataChart(
                date=Date(year=2023, quarter=Quarter.FIRST_QUARTER),
                actual=-1.92,
                estimate=-2.0
            )
        ]
        self.yearly_financials_data__dip_in_up_trend_list = [
            YearlyFinancialsDataChart(
                date=Date(year=2019),
                revenue=260174000000,
                earnings=55256000000
            ),
            YearlyFinancialsDataChart(
                date=Date(year=2020),
                revenue=274515000000,
                earnings=57411000000
            ),
            YearlyFinancialsDataChart(
                date=Date(year=2021),
                revenue=365817000000,
                earnings=94680000000
            ),
            YearlyFinancialsDataChart(
                date=Date(year=2022),
                revenue=500,
                earnings=99803000000
            )
        ]
        self.exception_list = [
            YearlyFinancialsDataChart(date=Date(year=2019), revenue=0, earnings=0),
            YearlyFinancialsDataChart(date=Date(year=2020), revenue=None, earnings=""),  # type: Ignore
        ]
        self.negative_values_list = [
            YearlyFinancialsDataChart(date=Date(year=2019), revenue=0, earnings=0),
            YearlyFinancialsDataChart(date=Date(year=2020), revenue=-50, earnings=50),
        ]
        self.one_value_list = [
            YearlyFinancialsDataChart(date=Date(year=2019), revenue=0, earnings=0),
        ]

    def test_convert_json_to_model_list(self):
        json_file_name = "data.json"
        data = json.loads(open(f'{HISTORICAL_EARNINGS_TEST_PATH}{json_file_name}').read())
        ticker = next(iter(data.keys()))

        quarterly_earnings_data_expected_list = [
            QuarterlyEarningsDataChart(
                date=Date(year=2022, quarter=Quarter.SECOND_QUARTER),
                actual=1.2,
                estimate=1.16
            ),
            QuarterlyEarningsDataChart(
                date=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                actual=1.29,
                estimate=1.27
            ),
            QuarterlyEarningsDataChart(
                date=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),
                actual=1.88,
                estimate=1.94
            ),
            QuarterlyEarningsDataChart(
                date=Date(year=2023, quarter=Quarter.FIRST_QUARTER),
                actual=1.52,
                estimate=1.43
            )
        ]
        quarterly_financials_data_expected_list = [
            QuarterlyFinancialsDataChart(
                date=Date(year=2022, quarter=Quarter.SECOND_QUARTER),
                revenue=82959000000,
                earnings=19442000000
            ),
            QuarterlyFinancialsDataChart(
                date=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                revenue=90146000000,
                earnings=20721000000
            ),
            QuarterlyFinancialsDataChart(
                date=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),
                revenue=117154000000,
                earnings=29998000000
            ),
            QuarterlyFinancialsDataChart(
                date=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                revenue=0,
                earnings=0,
            )
        ]
        yearly_financials_data_expected_list = [
            YearlyFinancialsDataChart(
                date=Date(year=2019),
                revenue=260174000000,
                earnings=55256000000
            ),
            YearlyFinancialsDataChart(
                date=Date(year=2020),
                revenue=274515000000,
                earnings=57411000000
            ),
            YearlyFinancialsDataChart(
                date=Date(year=2021),
                revenue=365817000000,
                earnings=94680000000
            ),
            YearlyFinancialsDataChart(
                date=Date(year=2022),
                revenue=394328000000,
                earnings=99803000000
            )
        ]

        models_with_expected_results = [
            (QuarterlyEarningsDataChart, quarterly_earnings_data_expected_list),
            (QuarterlyFinancialsDataChart, quarterly_financials_data_expected_list),
            (YearlyFinancialsDataChart, yearly_financials_data_expected_list)
        ]

        for model, expected in models_with_expected_results:
            assert EarningsHistory.convert_json_to_time_series_model(
                ticker=ticker,
                data=data,
                model=model
            ) == expected

        class WrongClass:
            pass

        self.assertRaises(
            TypeError,
            EarningsHistory.convert_json_to_time_series_model,
            ticker=ticker,
            data=data,
            model=WrongClass
        )

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
        ]

        for series_input, expected_result in test_cases:
            result, _ = TimeSeriesDataCollection.is_consistently_up_trending_series(
                series=series_input
            )
            assert result is expected_result

        test_cases = [
            # chart_list, attribute, expected_result
            (self.quarterly_earnings_data_up_trending_list, 'actual', True),
            (self.quarterly_earnings_data_dip_in_up_trend_list, 'actual', False),
            (self.quarterly_earnings_data_dip_in_up_trend_list, 'estimate', False),
            (self.yearly_financials_data__dip_in_up_trend_list, 'revenue', False),
        ]

        for chart, attribute, expected_result in test_cases:
            result, _ = TimeSeriesDataCollection.is_consistently_up_trending_chart_list(
                chart_list=chart,
                attribute=attribute
            )
            assert result is expected_result

        test_cases = [
            # chart_list, attribute, expected_exception
            (self.quarterly_earnings_data_up_trending_list, 'estimate', ValueError),
            (self.quarterly_earnings_data_up_trending_list, 'none', AttributeError),
            (self.exception_list, 'revenue', ValueError),
            (self.exception_list, 'earnings', ValueError),
            ([], 'earnings', ValueError),
            (self.one_value_list, 'earnings', ValueError),
        ]

        for chart, attribute, expected_exception in test_cases:
            self.assertRaises(
                expected_exception,
                TimeSeriesDataCollection.is_consistently_up_trending_chart_list,
                chart_list=chart,
                attribute=attribute
            )
        self.assertRaises(ValueError, TimeSeriesDataCollection.is_consistently_up_trending_series, series=[1])

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
            result, interval = TimeSeriesDataCollection.is_consistently_up_trending_series(series=series_input)

            if expected_bool is False:
                assert result is expected_bool and interval == expected_output
            else:
                assert series_input == expected_output

        test_cases = [
            # chart_list, attribute, expected_bool, expected_interval
            (self.quarterly_earnings_data_dip_in_up_trend_list, 'actual', False, 3),
            (self.quarterly_earnings_data_dip_in_up_trend_list, 'estimate', False, 2),
            (self.negative_values_list, 'revenue', False, 1),
        ]

        for chart, attribute, expected_bool, expected_interval in test_cases:
            result, interval = TimeSeriesDataCollection.is_consistently_up_trending_chart_list(
                chart_list=chart,
                attribute=attribute
            )
            assert result is expected_bool and interval is expected_interval

    def test_passes_percentage_increase_requirements(self):
        series = [100, 50]
        test_cases = [
            # series_input, percentage_requirement, expected_output
            (series, 50, True),  # 50% of 100 is 50, meets requirement
            (series, 51, False),  # 51% of 100 is 51, doesn't meet requirement
            (series, 49, True),  # 49% of 100 is 49, meets requirement
            (series, 101, False),  # 101% of 100 is 101, doesn't meet requirement
            (series, 100, False),  # 100% of 100 is 100, doesn't meet requirement
            ([33.33, 50, 100, 0], 1, False),  # Percentage requirement of 1, none meet
            ([26.67, 281.82], 26, True),  # 26% of 26.67 is 6.94, meets requirement
            ([26.67, 281.82], 26.68, False),  # 26.68% of 26.67 is 7.12, doesn't meet requirement
            ([100, 100, 100], 0, True),  # 0% of any value is 0, all meet requirement
            ([0, 0, 0], 0, True),  # 0% of any value is 0, all meet requirement
            ([0, 0, 0], 1, False),  # 1% of any value is greater than 0, none meet
            ([10, 5, 2.5], -50, True),  # -50% of any value is less than or equal, all meet requirement
        ]

        for series_input, percentage_requirement, expected_output in test_cases:
            assert TimeSeriesDataCollection._passes_percentage_increase_requirements(
                series=series_input,
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
            assert TimeSeriesDataCollection._calculate_percentage_increase_for_series(
                series=series_input
            ) == expected_result

        assert TimeSeriesDataCollection._calculate_percentage_increase_for_chart_list(
            chart_list=self.quarterly_earnings_data_up_trending_list,
            attribute='actual'
        ) == [7.5, 45.74, 2.13]
