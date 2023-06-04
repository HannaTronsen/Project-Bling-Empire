from typing import Type
from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.data_classes.charts import Chart, QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart


class HistoricalEarnings(TimeSeriesDataCollection):

    quarterlyEarningsDataChart: list[QuarterlyEarningsDataChart]
    quarterlyFinancialsDataChart: list[QuarterlyFinancialsDataChart]
    yearlyFinancialsDataChart: list[YearlyFinancialsDataChart]

    def convert_json_to_model_list(self, ticker, data, model: Type[Chart]) -> list[Chart]:
        if model in [QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart]:
            data = model.get_section_from_json_path(base=data[ticker])
            return [model(**item).convert_date() for item in data]
        raise TypeError(f"Wrong model type: {model}.")

    def _is_invalid_comparison( self, i, j): return i is None or j is None or type(i) != type(j)

    def _not_up_trending(self, i, j): return i > j

    def is_consistently_up_trending(self, chart_list: list[Chart], attribute: str):
        for index in range(len(chart_list) - 1):
            i = getattr(chart_list[index], attribute)
            j = getattr(chart_list[index + 1], attribute)
            if (
                self._is_invalid_comparison(i=i, j=j) or
                self._not_up_trending(i=i, j=j)
            ):
                return False
        return True
