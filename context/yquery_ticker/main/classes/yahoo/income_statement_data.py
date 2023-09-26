from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.income_statement import (
    IncomeStatementDataClass,
    NET_INCOME
)
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import (
    PERIOD_TYPE,
    AS_OF_DATE,
)
from context.yquery_ticker.main.enums.growth_criteria import GrowthCriteria


class IncomeStatementData(TimeSeriesDataCollection):

    @classmethod
    def convert_data_frame_to_time_series_model(cls, data_frame):
        result = []
        for index, row in data_frame.iterrows():
            result.append(
                IncomeStatementDataClass(
                    asOfDate=Date.convert_date(Date.from_data_frame(row[AS_OF_DATE])),
                    periodType=Date.to_period_type(row[PERIOD_TYPE]),
                    netIncome=row[NET_INCOME],
                )
            )
        return result

    @classmethod
    def evaluate_growth_criteria(cls, income_statement) -> bool:
        return TimeSeriesDataCollection.passes_percentage_increase_requirements(
            percentages=TimeSeriesDataCollection._calculate_percentage_increase_for_model_list(
                model_list=income_statement,
                attribute=GrowthCriteria.NET_INCOME.__str__
            ),
            percentage_requirement=GrowthCriteria.NET_INCOME.__percentage_criteria__
        )

    @classmethod
    def mockk(cls):
        return IncomeStatementData()
