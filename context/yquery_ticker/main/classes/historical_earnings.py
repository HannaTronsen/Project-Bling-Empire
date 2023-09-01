from typing import Type
from ..classes.time_series_data_collection import TimeSeriesDataCollection
from ..const import WRONG_TYPE_STRING
from ..data_classes.charts import (
    Chart,
    QuarterlyEarningsDataChart,
    QuarterlyFinancialsDataChart,
    YearlyFinancialsDataChart
)


class HistoricalEarnings(TimeSeriesDataCollection):
    quarterlyEarningsDataChart: list[QuarterlyEarningsDataChart]
    quarterlyFinancialsDataChart: list[QuarterlyFinancialsDataChart]
    yearlyFinancialsDataChart: list[YearlyFinancialsDataChart]

    @classmethod
    def convert_json_to_model_list(cls, ticker, data, model: Type[Chart]) -> list[Chart]:
        if model in [QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart]:
            data = model.get_section_from_json_path(data[ticker])
            return [model(**item).convert_date() for item in data]  # type: ignore
        raise TypeError(WRONG_TYPE_STRING.format(type=model))

    @classmethod
    def mockk(cls):
        return HistoricalEarnings()
