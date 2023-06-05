from typing import Type
from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.const import WRONG_TYPE_STRING
from context.yquery_ticker.main.data_classes.charts import Chart, QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart


class HistoricalEarnings(TimeSeriesDataCollection):

    quarterlyEarningsDataChart: list[QuarterlyEarningsDataChart]
    quarterlyFinancialsDataChart: list[QuarterlyFinancialsDataChart]
    yearlyFinancialsDataChart: list[YearlyFinancialsDataChart]

    def convert_json_to_model_list(self, ticker, data, model: Type[Chart]) -> list[Chart]:
        if model in [QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart]:
            data = model.get_section_from_json_path(base=data[ticker])
            return [model(**item).convert_date() for item in data]
        raise TypeError(WRONG_TYPE_STRING.format(type=model))