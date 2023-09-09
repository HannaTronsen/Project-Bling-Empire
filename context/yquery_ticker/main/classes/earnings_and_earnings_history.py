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


class EarningsAndEarningsHistory(TimeSeriesDataCollection):
    quarterly_earnings_data: list[QuarterlyEarningsDataChart]
    quarterly_financials_data: list[QuarterlyFinancialsDataChart]
    yearly_financials_data: list[YearlyFinancialsDataChart]
    earnings_history_data: list[EarningsHistoryDataClass]

    @classmethod
    def convert_json_to_time_series_model(cls, ticker, data, model: Type[Chart]) -> list[Chart]:
        if model in [QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart]:
            data = model.get_section_from_json_path(data[ticker])
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
                    quarter=Date.convert_date(date_input=row[EPS_QUARTER])
                )
            )
        return earnings_history

    @classmethod
    def mockk(cls):
        return EarningsAndEarningsHistory()
