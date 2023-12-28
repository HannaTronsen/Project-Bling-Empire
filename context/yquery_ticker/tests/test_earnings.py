import json
import unittest
from context.yquery_ticker.main.classes.yahoo.historical_earnings_data import HistoricalEarningsData
from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.const import YQUERY_TEST_PATH
from context.yquery_ticker.main.enums.quarter import Quarter
from context.yquery_ticker.main.data_classes.charts import (
    Date,
    QuarterlyEarningsDataChart,
    QuarterlyFinancialsDataChart,
    YearlyFinancialsDataChart
)
from context.yquery_ticker.tests.utils.test_case import TestCase


class test_earnings(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(test_earnings, self).__init__(*args, **kwargs)

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
        self.yearly_financials_data_dip_in_up_trend_list = [
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
        json_file_name = "resources/data.json"
        data = json.loads(open(f'{YQUERY_TEST_PATH}{json_file_name}').read())
        ticker_symbol = next(iter(data.keys()))

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
            assert HistoricalEarningsData.convert_json_to_time_series_model(
                ticker_symbol=ticker_symbol,
                data=data,
                model=model
            ) == expected

        class WrongClass:
            pass

        self.assertRaises(
            TypeError,
            HistoricalEarningsData.convert_json_to_time_series_model,
            ticker=ticker_symbol,
            data=data,
            model=WrongClass
        )

    def test_is_consistently_up_trending(self):

        test_cases = [
            TestCase(
                model_list=self.quarterly_earnings_data_up_trending_list,
                attribute='actual',
                expected_result=True
            ),
            TestCase(
                model_list=self.quarterly_earnings_data_dip_in_up_trend_list,
                attribute='actual',
                expected_result=False
            ),
            TestCase(
                model_list=self.quarterly_earnings_data_dip_in_up_trend_list,
                attribute='estimate',
                expected_result=False
            ),
            TestCase(
                model_list=self.yearly_financials_data_dip_in_up_trend_list,
                attribute='revenue',
                expected_result=False
            ),
        ]

        for case in test_cases:
            result, _ = TimeSeriesDataCollection.is_consistently_up_trending_model_list(
                model_list=case.model_list,
                attribute=case.attribute
            )
            assert result is case.expected_result

        test_cases = [
            TestCase(
                model_list=self.quarterly_earnings_data_up_trending_list,
                attribute='none',
                expected_exception=AttributeError
            ),
            TestCase(
                model_list=self.exception_list,
                attribute='revenue',
                expected_exception=ValueError
            ),
            TestCase(
                model_list=self.exception_list,
                attribute='earnings',
                expected_exception=ValueError
            ),
            TestCase(
                model_list=[],
                attribute='earnings',
                expected_exception=ValueError
            ),
            TestCase(
                model_list=self.one_value_list,
                attribute='earnings',
                expected_exception=ValueError
            ),
        ]

        for case in test_cases:
            self.assertRaises(
                case.expected_exception,
                TimeSeriesDataCollection.is_consistently_up_trending_model_list,
                model_list=case.model_list,
                attribute=case.attribute
            )

    def test_get_consecutive_upward_trend_interval(self):
        test_cases = [
            TestCase(
                model_list=self.quarterly_earnings_data_dip_in_up_trend_list,
                attribute='actual',
                expected_bool=False,
                expected_interval=3
            ),
            TestCase(
                model_list=self.quarterly_earnings_data_dip_in_up_trend_list,
                attribute='estimate',
                expected_bool=False,
                expected_interval=2
            ),
            TestCase(
                model_list=self.negative_values_list,
                attribute='revenue',
                expected_bool=False,
                expected_interval=1
            ),
        ]

        for case in test_cases:
            result, interval = TimeSeriesDataCollection.is_consistently_up_trending_model_list(
                model_list=case.model_list,
                attribute=case.attribute
            )
            assert result is case.expected_bool and interval is case.expected_interval

    def test_calculate_percentage_increase_for_data_set(self):
        assert TimeSeriesDataCollection.calculate_percentage_increase_for_model_list(
            model_list=self.quarterly_earnings_data_up_trending_list,
            attribute='actual'
        ) == [7.5, 45.74, 2.13]

    def test_passes_percentage_increase_requirements(self):
        percentages = TimeSeriesDataCollection.calculate_percentage_increase_for_model_list(
            model_list=self.quarterly_earnings_data_up_trending_list,
            attribute='actual'
        )
        assert TimeSeriesDataCollection.passes_percentage_increase_requirements(
            percentages=percentages,
            percentage_requirement=40
        ) is False

        assert TimeSeriesDataCollection.passes_percentage_increase_requirements(
            percentages=percentages,
            percentage_requirement=2
        ) is True

        assert TimeSeriesDataCollection.passes_percentage_increase_requirements(
            percentages=[10, 15],
            percentage_requirement=20
        ) is False
