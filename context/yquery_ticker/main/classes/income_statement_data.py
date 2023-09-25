from typing import List

import pandas as pd

from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.income_statement import IncomeStatementDataClass, \
    PeriodType, AS_OF_DATE, PERIOD_TYPE, NET_INCOME
from context.yquery_ticker.main.enums.growth_criteria import GrowthCriteria


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
    def convert_data_frame_to_time_series_model(cls, data_frame):
        result = []
        for index, row in data_frame.iterrows():
            result.append(
                IncomeStatementDataClass(
                    asOfDate=Date.convert_date(row[AS_OF_DATE].strftime("%Y-%m-%d")),
                    periodType=_to_period_type(row[PERIOD_TYPE]),
                    netIncome=row[NET_INCOME],
                )
            )
        return result

    @classmethod
    def evaluate_growth_criteria(cls, income_statement) -> bool:
        return TimeSeriesDataCollection._passes_percentage_increase_requirements(
            percentages=TimeSeriesDataCollection._calculate_percentage_increase_for_model_list(
                model_list=income_statement,
                attribute=GrowthCriteria.NET_INCOME.__str__
            ),
            percentage_requirement=GrowthCriteria.NET_INCOME.__percentage_criteria__
        )

    @classmethod
    def mockk(cls):
        return IncomeStatementData()
