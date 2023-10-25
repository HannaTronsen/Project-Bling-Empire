from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.const import WRONG_TYPE_STRING
from context.yquery_ticker.main.data_classes.date import Date, PeriodType
from context.yquery_ticker.main.data_classes.yq_data_frame_data.income_statement import (
    IncomeStatementDataClass,
    NET_INCOME, TOTAL_REVENUE
)
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import (
    PERIOD_TYPE,
    AS_OF_DATE,
)
from context.yquery_ticker.main.enums.growth_criteria import GrowthCriteria
from context.yquery_ticker.main.utils.dict_key_enum import DictKey


class IncomeStatementData(TimeSeriesDataCollection):

    def __init__(self, entries):
        self.entries: list[IncomeStatementDataClass] = entries

    @classmethod
    def convert_data_frame_to_time_series_model(cls, data_frame):
        result = []
        for index, row in data_frame.iterrows():
            result.append(
                IncomeStatementDataClass(
                    asOfDate=Date.convert_date(Date.from_data_frame(row[AS_OF_DATE])),
                    periodType=Date.to_period_type(row[PERIOD_TYPE]),
                    netIncome=row[NET_INCOME],
                    totalRevenue=row[TOTAL_REVENUE],
                )
            )
        return result

    def get_entry_of(self, as_of_date: Date, period_type: PeriodType):
        for entry in self.entries:
            if entry.asOfDate == as_of_date and entry.periodType == period_type:
                return entry.netIncome
        return 0

    def evaluate_growth_criteria(self, attribute: DictKey) -> bool:
        if attribute == DictKey.NET_INCOME:
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=self.entries,
                    attribute=GrowthCriteria.NET_INCOME.__str__
                ),
                percentage_requirement=GrowthCriteria.NET_INCOME.__percentage_criteria__
            )
        elif attribute == DictKey.SALES:
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=self.entries,
                    attribute=GrowthCriteria.SALES.__str__
                ),
                percentage_requirement=GrowthCriteria.SALES.__percentage_criteria__
            )
        raise TypeError(WRONG_TYPE_STRING.format(type=attribute))

    @classmethod
    def mockk(cls):
        return IncomeStatementData(entries=[])
