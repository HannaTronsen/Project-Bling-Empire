import json
from typing import Type

import pandas as pd
from ..data_classes.date import Date
from ..classes.time_series_data_collection import TimeSeriesDataCollection
from ..const import WRONG_TYPE_STRING
from ..data_classes.charts import (
    Chart,
    QuarterlyEarningsDataChart,
    QuarterlyFinancialsDataChart,
    YearlyFinancialsDataChart
)
from ..data_classes.yq_data_frame_data.earnings_history import (
    EarningsHistoryDataClass,
    EPS_ACTUAL, EPS_ESTIMATE,
    EPS_DIFFERENCE, EPS_QUARTER
)
from ..enums.growth_criteria import GrowthCriteria
from ..utils.dict_key_enum import DictKey


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
    def evaluate_growth_criteria(cls, chart_list: [Chart], attribute: DictKey) -> bool:
        if attribute == DictKey.EARNINGS_HISTORY:
            return TimeSeriesDataCollection._passes_percentage_increase_requirements(
                percentages=TimeSeriesDataCollection._calculate_percentage_increase_for_model_list(
                    model_list=chart_list,
                    attribute=GrowthCriteria.EARNINGS.__str__
                ),
                percentage_requirement=GrowthCriteria.EARNINGS.__percentage_criteria__
            )
        elif attribute == DictKey.REVENUE_HISTORY:
            return TimeSeriesDataCollection._passes_percentage_increase_requirements(
                percentages=TimeSeriesDataCollection._calculate_percentage_increase_for_model_list(
                    model_list=chart_list,
                    attribute=GrowthCriteria.REVENUE.__str__
                ),
                percentage_requirement=GrowthCriteria.REVENUE.__percentage_criteria__
            )
        else:
            raise TypeError(WRONG_TYPE_STRING.format(type=attribute))

    @classmethod
    def mockk(cls):
        return HistoricalEarningsData()
