import json
import unittest
from context.yquery_ticker.main.classes.historical_earnings import HistoricalEarnings
from context.yquery_ticker.main.const import YQUERY_TEST_PATH
from context.yquery_ticker.main.data_classes.charts import Date, QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart
from context.yquery_ticker.main.enums.quarter import Quarter, QuarterId


class test_historical_earnings(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_historical_earnings, self).__init__(*args, **kwargs)

        json_file_name = "data.json"
        self.data = json.loads(open(f'{YQUERY_TEST_PATH}{json_file_name}').read())
        self.ticker = next(iter(self.data.keys()))
        
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

    def convert_json_to_model_list(self):
        assert HistoricalEarnings().convert_json_to_model_list(ticker=self.ticker,data=self.data, model=QuarterlyEarningsDataChart) == self.quarterly_earnings_data_chart_expected_list
        assert HistoricalEarnings().convert_json_to_model_list(ticker=self.ticker, data=self.data, model=QuarterlyFinancialsDataChart) == self.quarterly_financials_data_chart_expected_list    
        assert HistoricalEarnings().convert_json_to_model_list(ticker=self.ticker, data=self.data, model=YearlyFinancialsDataChart) == self.yearly_financials_data_chart_expected_list
    