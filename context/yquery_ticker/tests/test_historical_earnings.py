import json
import unittest
from context.yquery_ticker.main.classes.historical_earnings import HistoricalEarnings
from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.const import YQUERY_TEST_PATH
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

        json_file_name = "data.json"
        self.data = json.loads(open(f'{YQUERY_TEST_PATH}{json_file_name}').read())
        self.ticker = next(iter(self.data.keys()))

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
        self.quarterly_earnings_data_chart_expected_list = [
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
        self.quarterly_financials_data_chart_expected_list = [
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
        self.yearly_financials_data_chart_expected_list = [
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
        models_with_expected_results = [
            (QuarterlyEarningsDataChart, self.quarterly_earnings_data_chart_expected_list),
            (QuarterlyFinancialsDataChart, self.quarterly_financials_data_chart_expected_list),
            (YearlyFinancialsDataChart, self.yearly_financials_data_chart_expected_list)
        ]

        for model, expected in models_with_expected_results:
            assert HistoricalEarnings.convert_json_to_time_series_model(
                ticker=self.ticker,
                data=self.data,
                model=model
            ) == expected

        class WrongClass:
            pass

        self.assertRaises(
            TypeError,
            HistoricalEarnings.convert_json_to_time_series_model,
            ticker=self.ticker,
            data=self.data,
            model=WrongClass
        )

    def test_is_consistently_up_trending(self):
        test_cases = [
            # series_input, expected_result
            ([1, 2, 3], True),
            ([0, -1, -2, -3], False),
            ([1, 3, 2], False),
            ([1, 3], True),
        ]

        for series_input, expected_result in test_cases:
            result, _ = TimeSeriesDataCollection.is_consistently_up_trending_series(
                series=series_input
            )
            assert result is expected_result

        test_cases = [
            # chart_list, attribute, expected_result
            (self.quarterly_earnings_data_up_trending_list, 'actual', True),
            (self.quarterly_earnings_data_chart_expected_list, 'actual', False),
            (self.quarterly_earnings_data_chart_expected_list, 'estimate', False),
            (self.quarterly_financials_data_chart_expected_list, 'revenue', False),
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
            (self.exception_list, 'revenue', ValueError),
            (self.exception_list, 'earnings', ValueError),
            ([], 'earnings', ValueError),
            (self.one_value_list, 'earnings', ValueError),
            (self.quarterly_earnings_data_chart_expected_list, 'none', AttributeError),
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
            # series_input, expected_bool, expected_interval
            ([0, 1, 4, 3, 4], False, 2),
            ([1, 3, 2], False, 1),
            ([0, -1, -4, -3, -4], False, 1),
            ([0, -1, -4, -3, -5, -4], False, 2),
        ]

        for series_input, expected_bool, expected_interval in test_cases:
            result, interval = TimeSeriesDataCollection.is_consistently_up_trending_series(series=series_input)
            assert result is expected_bool and interval is expected_interval

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
            (series, 50, True),
            (series, 51, False),
            (series, 49, True),
            (series, 101, False),
            (series, 100, False),
            ([33.33, 50, 100, 0], 1, False),
            ([26.67, 281.82], 26, True),
            ([26.67, 281.82], 26.68, False),
        ]

        for series_input, percentage_requirement, expected_output in test_cases:
            assert TimeSeriesDataCollection._passes_percentage_increase_requirements(
                series=series_input,
                percentage_requirement=percentage_requirement
            ) is expected_output

    def test_calculate_percentage_increase_for_data_set(self):
        test_cases = [
            # series_input, expected_result
            ([1, 2, 3], [100, 50]),
            ([1, 3], [200]),
            ([1, 3, 4.5], [200, 50]),
            ([-3, -2.2, 4], [26.67, 281.82]),
            ([-3, -2, -1, 0, 1], [33.33, 50, 100, 0]),
        ]

        for series_input, expected_result in test_cases:
            assert TimeSeriesDataCollection._calculate_percentage_increase_for_series(
                series=series_input
            ) == expected_result

        assert TimeSeriesDataCollection._calculate_percentage_increase_for_chart_list(
            chart_list=self.quarterly_earnings_data_up_trending_list,
            attribute='actual'
        ) == [7.5, 45.74, 2.13]
