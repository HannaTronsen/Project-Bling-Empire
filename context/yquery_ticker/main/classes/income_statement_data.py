from typing import List

import pandas as pd

from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.income_statement import IncomeStatementDataClass, \
    PeriodType, AS_OF_DATE, PERIOD_TYPE, NET_INCOME


def _to_period_type(period_type) -> PeriodType:
    if period_type == "12M":
        return PeriodType.MONTH_12
    elif period_type == "3M":
        return PeriodType.MONTH_3
    elif period_type == "TTM":
        return PeriodType.TTM
    else:
        raise ValueError(f"asOfDate value was either null or not an expected value. period_type: {period_type}")


class IncomeStatementData(TimeSeriesDataCollection):
    annual: List[IncomeStatementDataClass]
    quarterly: List[IncomeStatementDataClass]

    @classmethod
    def convert_csv_to_time_series_model(cls, csv):
        result = []
        df = pd.read_csv(csv)
        for index, row in df.iterrows():
            result.append(
                IncomeStatementDataClass(
                    asOfDate=Date.convert_date(row[AS_OF_DATE]),
                    periodType=_to_period_type(row[PERIOD_TYPE]),
                    netIncome=row[NET_INCOME],
                )
            )
        return result

    @classmethod
    def mockk(cls):
        return IncomeStatementData()
