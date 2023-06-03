from ctypes import Union
import json
from typing import Optional, Type
from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.data_classes.charts import QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart


class HistoricalEarnings(TimeSeriesDataCollection):

    quarterlyEarningsDataChart: list[QuarterlyEarningsDataChart]
    quarterlyFinancialsDataChart: list[QuarterlyFinancialsDataChart]
    yearlyFinancialsDataChart: list[YearlyFinancialsDataChart]

    def convert_json_to_model_list(self, ticker, data, model: Optional[Type]) -> Type:
        if model == QuarterlyEarningsDataChart:
            data = data[ticker] + QuarterlyEarningsDataChart.get_json_path()
            return ([QuarterlyEarningsDataChart(**item).convert_date() for item in data])
        if model == QuarterlyFinancialsDataChart:
            data = data[ticker] + QuarterlyEarningsDataChart.get_json_path()
            return ([QuarterlyFinancialsDataChart(**item).convert_date() for item in data])
        if model == YearlyFinancialsDataChart:
            data = data[ticker] + YearlyFinancialsDataChart.get_json_path()
            return ([YearlyFinancialsDataChart(**item).convert_date() for item in data])
    
