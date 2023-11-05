import json
from typing import Type

import pandas as pd

from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.const import WRONG_TYPE_STRING
from context.yquery_ticker.main.data_classes.charts import (
    Chart,
    QuarterlyEarningsDataChart,
    QuarterlyFinancialsDataChart,
    YearlyFinancialsDataChart
)
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.earnings_history import (
    EarningsHistoryDataClass,
    EPS_ACTUAL, EPS_ESTIMATE,
    EPS_DIFFERENCE, EPS_QUARTER
)


class HistoricalEarningsData(TimeSeriesDataCollection):

    @classmethod
    def convert_json_to_time_series_model(cls, ticker_symbol: str, data: json, model: Type[Chart]) -> list[Chart]:
        if model in [QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart]:
            data = model.get_section_from_json_path(data[ticker_symbol])
            return [model(**item).convert_date() for item in data]  # type: ignore
        raise TypeError(WRONG_TYPE_STRING.format(type=model))

    @classmethod
    def convert_csv_to_time_series_model(cls, csv):
        df = pd.read_csv(csv)
        earnings_history: list[EarningsHistoryDataClass] = []
        for index, row in df.iterrows():
            earnings_history.append(
                EarningsHistoryDataClass(
                    epsActual=row[EPS_ACTUAL],
                    epsEstimate=row[EPS_ESTIMATE],
                    epsDifference=row[EPS_DIFFERENCE],
                    quarter=Date.convert_date(date_input=row[EPS_QUARTER]),
                    asOfDate=None,
                    periodType=None
                )
            )
        return earnings_history

    @classmethod
    def evaluate_growth_criteria(cls, chart_list: [Chart], percentage_criteria: int, attribute: str) -> bool:
        return cls.passes_percentage_increase_requirements(
            percentages=cls.calculate_percentage_increase_for_model_list(
                model_list=Chart.sorted(chart_list),
                attribute=attribute
            ),
            percentage_requirement=percentage_criteria
        )

    @classmethod
    def mockk(cls):
        return HistoricalEarningsData()
