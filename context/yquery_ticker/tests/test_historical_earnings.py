import json
import unittest
from context.yquery_ticker.main.classes.historical_earnings import HistoricalEarnings
from context.yquery_ticker.main.const import YQUERY_TEST_PATH
from context.yquery_ticker.main.data_classes.charts import Date, QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart
from context.yquery_ticker.main.enums.quarter import Quarter


class test_historical_earnings(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_historical_earnings, self).__init__(*args, **kwargs)

        json_file_name = "data.json"
        self.data = json.loads(open(f'{YQUERY_TEST_PATH}{json_file_name}').read())
        self.ticker = next(iter(self.data.keys()))

        self.quarterly_earnings_data_up_trending_list = [
            QuarterlyEarningsDataChart(date=Date(year=2022, quarter=Quarter.SECOND_QUARTER), actual=1.2, estimate=1.16),
            QuarterlyEarningsDataChart(date=Date(year=2022, quarter=Quarter.THIRD_QUARTER), actual=1.29, estimate=1.27),
            QuarterlyEarningsDataChart(date=Date(year=2022, quarter=Quarter.FOURTH_QUARTER), actual=1.88, estimate=1.94),
            QuarterlyEarningsDataChart(date=Date(year=2023, quarter=Quarter.FIRST_QUARTER), actual=1.92, estimate=2)
        ]
        self.quarterly_earnings_data_dip_in_up_trend_list = [
            QuarterlyEarningsDataChart(date=Date(year=2022, quarter=Quarter.SECOND_QUARTER), actual=1.2, estimate=1.94),
            QuarterlyEarningsDataChart(date=Date(year=2022, quarter=Quarter.THIRD_QUARTER), actual=1.1, estimate=1.95),
            QuarterlyEarningsDataChart(date=Date(year=2022, quarter=Quarter.FOURTH_QUARTER), actual=1.88, estimate=1.94),
            QuarterlyEarningsDataChart(date=Date(year=2023, quarter=Quarter.FIRST_QUARTER), actual=1.92, estimate=2.0)
        ]
        self.negative_quarterly_earnings_data_dip_in_up_trend_list = [
            QuarterlyEarningsDataChart(date=Date(year=2022, quarter=Quarter.SECOND_QUARTER), actual=-1.2, estimate=-1.94),
            QuarterlyEarningsDataChart(date=Date(year=2022, quarter=Quarter.THIRD_QUARTER), actual=-1.1, estimate=-1.95),
            QuarterlyEarningsDataChart(date=Date(year=2022, quarter=Quarter.FOURTH_QUARTER), actual=-1.88, estimate=-1.94),
            QuarterlyEarningsDataChart(date=Date(year=2023, quarter=Quarter.FIRST_QUARTER), actual=-1.92, estimate=-2.0)
        ]
        self.quarterly_earnings_data_chart_expected_list = [
            QuarterlyEarningsDataChart(date=Date(year=2022, quarter=Quarter.SECOND_QUARTER), actual=1.2, estimate=1.16),
            QuarterlyEarningsDataChart(date=Date(year=2022, quarter=Quarter.THIRD_QUARTER), actual=1.29, estimate=1.27),
            QuarterlyEarningsDataChart(date=Date(year=2022, quarter=Quarter.FOURTH_QUARTER), actual=1.88, estimate=1.94),
            QuarterlyEarningsDataChart(date=Date(year=2023, quarter=Quarter.FIRST_QUARTER), actual=1.52, estimate=1.43)
        ]
        self.quarterly_financials_data_chart_expected_list = [
            QuarterlyFinancialsDataChart(date=Date(year=2022, quarter=Quarter.SECOND_QUARTER), revenue= 82959000000, earnings=19442000000),
            QuarterlyFinancialsDataChart(date=Date(year=2022, quarter=Quarter.THIRD_QUARTER),  revenue=90146000000, earnings=20721000000),
            QuarterlyFinancialsDataChart(date=Date(year=2022, quarter=Quarter.FOURTH_QUARTER),  revenue=117154000000, earnings=29998000000),
            QuarterlyFinancialsDataChart(date=Date(year=2023, quarter=Quarter.SECOND_QUARTER),  revenue=0, earnings=0,)
        ]
        self.yearly_financials_data_chart_expected_list = [
            YearlyFinancialsDataChart(date=Date(year=2019), revenue= 260174000000, earnings=55256000000),
            YearlyFinancialsDataChart(date=Date(year=2020),  revenue=274515000000, earnings=57411000000),
            YearlyFinancialsDataChart(date=Date(year=2021),  revenue=365817000000, earnings=94680000000),
            YearlyFinancialsDataChart(date=Date(year=2022),  revenue=394328000000, earnings=99803000000)
        ]
        self.excpetion_list = [
            YearlyFinancialsDataChart(date=Date(year=2019), revenue= 0, earnings=0),
            YearlyFinancialsDataChart(date=Date(year=2020),  revenue=None, earnings=""),
        ]
        self.negative_values_list = [
            YearlyFinancialsDataChart(date=Date(year=2019), revenue= 0, earnings=0),
            YearlyFinancialsDataChart(date=Date(year=2020),  revenue=-50, earnings=50),
        ]
        self.one_value_list = [
            YearlyFinancialsDataChart(date=Date(year=2019), revenue= 0, earnings=0),
        ]

    def test_convert_json_to_model_list(self):
        assert HistoricalEarnings().convert_json_to_model_list(ticker=self.ticker,data=self.data, model=QuarterlyEarningsDataChart) == self.quarterly_earnings_data_chart_expected_list
        assert HistoricalEarnings().convert_json_to_model_list(ticker=self.ticker, data=self.data, model=QuarterlyFinancialsDataChart) == self.quarterly_financials_data_chart_expected_list    
        assert HistoricalEarnings().convert_json_to_model_list(ticker=self.ticker, data=self.data, model=YearlyFinancialsDataChart) == self.yearly_financials_data_chart_expected_list

        class WrongClass(): pass
        self.assertRaises(TypeError, HistoricalEarnings().convert_json_to_model_list, ticker=self.ticker,data=self.data, model=WrongClass)

    
    def test_is_consistently_up_trending(self):
        result, _ = HistoricalEarnings().is_consistently_up_trending(chart_list=self.quarterly_earnings_data_up_trending_list, attribute = 'actual'); assert result == True
        self.assertRaises(ValueError, HistoricalEarnings().is_consistently_up_trending, chart_list=self.quarterly_earnings_data_up_trending_list, attribute = 'estimate')
        result, _ = HistoricalEarnings().is_consistently_up_trending(chart_list=self.quarterly_earnings_data_chart_expected_list, attribute = 'actual'); assert result == False
        result, _ = HistoricalEarnings().is_consistently_up_trending(chart_list= self.quarterly_financials_data_chart_expected_list, attribute = 'revenue'); assert result == False
        result, _ = HistoricalEarnings().is_consistently_up_trending(chart_list= self.quarterly_earnings_data_chart_expected_list, attribute = 'estimate'); assert result == False
        self.assertRaises(ValueError, HistoricalEarnings().is_consistently_up_trending, chart_list=self.excpetion_list, attribute = 'revenue')
        self.assertRaises(ValueError, HistoricalEarnings().is_consistently_up_trending, chart_list=self.excpetion_list, attribute = 'earnings')
        result, _ = HistoricalEarnings().is_consistently_up_trending(chart_list= self.negative_values_list, attribute = 'revenue'); assert result == False
        result, _ = HistoricalEarnings().is_consistently_up_trending(chart_list= self.negative_values_list, attribute = 'earnings'); assert result == True
        self.assertRaises(ValueError, HistoricalEarnings().is_consistently_up_trending, chart_list=[], attribute = 'earnings')
        self.assertRaises(ValueError, HistoricalEarnings().is_consistently_up_trending, chart_list=self.one_value_list, attribute = 'earnings')
        self.assertRaises(AttributeError, HistoricalEarnings().is_consistently_up_trending, chart_list=self.quarterly_earnings_data_chart_expected_list, attribute = 'none')
        result, _ = HistoricalEarnings().is_consistently_up_trending(chart_list= [1,2,3]); assert result == True
        result, _ = HistoricalEarnings().is_consistently_up_trending(chart_list= [0,-1,-2,-3]); assert result == False
        result, _ = HistoricalEarnings().is_consistently_up_trending(chart_list= [-3,-2,-1,0]); assert result == True
        result, _ = HistoricalEarnings().is_consistently_up_trending(chart_list= [1,3,2]); assert result == False
        result, _ = HistoricalEarnings().is_consistently_up_trending(chart_list= [1,3]); assert result == True
        self.assertRaises(ValueError, HistoricalEarnings().is_consistently_up_trending, chart_list=[1])

    
    def test_get_consecutive_upward_trend_interval(self):
        (result, interval) = HistoricalEarnings().is_consistently_up_trending(chart_list=[0,1,4,3,4]); assert result == False and interval == 2
        (result, interval) = HistoricalEarnings().is_consistently_up_trending(chart_list= self.quarterly_earnings_data_dip_in_up_trend_list, attribute = 'actual');  assert result == False and interval == 3
        (result, interval) = HistoricalEarnings().is_consistently_up_trending(chart_list= self.quarterly_earnings_data_dip_in_up_trend_list, attribute = 'estimate');  assert result == False and interval == 2
        (result, interval) = HistoricalEarnings().is_consistently_up_trending(chart_list= self.negative_values_list, attribute = 'revenue');  assert result == False and interval == 1
        (result, interval) = HistoricalEarnings().is_consistently_up_trending(chart_list= [1,3,2]);  assert result == False and interval == 1
        (result, interval) = HistoricalEarnings().is_consistently_up_trending(chart_list= [0,-1,-4,-3,-4]);  assert result == False and interval == 1
        (result, interval) = HistoricalEarnings().is_consistently_up_trending(chart_list= [0,-1,-4,-3,-5,-4]);  assert result == False and interval == 2
    