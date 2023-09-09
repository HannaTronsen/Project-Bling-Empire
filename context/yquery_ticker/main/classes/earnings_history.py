from typing import Type

from .yq_data_frame_data import YQDataFrameData
from ..classes.time_series_data_collection import TimeSeriesDataCollection
from ..const import WRONG_TYPE_STRING
from ..data_classes.charts import (
    Chart,
    QuarterlyEarningsDataChart,
    QuarterlyFinancialsDataChart,
    YearlyFinancialsDataChart
)


class EarningsHistory(TimeSeriesDataCollection):
    quarterly_earnings_data: list[QuarterlyEarningsDataChart]
    quarterly_financials_data: list[QuarterlyFinancialsDataChart]
    yearly_financials_data: list[YearlyFinancialsDataChart]
    earnings_history: YQDataFrameData

    @classmethod
    def convert_json_to_time_series_model(cls, ticker, data, model: Type[Chart]) -> list[Chart]:
        if model in [QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart]:
            data = model.get_section_from_json_path(data[ticker])
            return [model(**item).convert_date() for item in data]  # type: ignore
        raise TypeError(WRONG_TYPE_STRING.format(type=model))

    @classmethod
    def convert_csv_to_yq_data_frame_data(cls, csv):
        pass

    @classmethod
    def mockk(cls):
        return EarningsHistory()
