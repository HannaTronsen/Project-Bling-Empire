from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.const import WRONG_TYPE_STRING
from context.yquery_ticker.main.data_classes.date import Date, PeriodType
from context.yquery_ticker.main.data_classes.expenses import Expenses
from context.yquery_ticker.main.data_classes.yq_data_frame_data.income_statement import (
    IncomeStatementDataClass,
    NET_INCOME, TOTAL_REVENUE,
    INTEREST_EXPENSE,
    INTEREST_EXPENSE_NON_OPERATING,
    TOTAL_OTHER_FINANCE_COST, TAX_PROVISION
)
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import (
    PERIOD_TYPE,
    AS_OF_DATE, YQDataFrameData,
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
                    interest_expense=row[INTEREST_EXPENSE] if INTEREST_EXPENSE in data_frame.columns else 0,
                    interest_expense_non_operating=row[INTEREST_EXPENSE_NON_OPERATING] if INTEREST_EXPENSE_NON_OPERATING in data_frame.columns else 0,
                    total_other_finance_cost=row[TOTAL_OTHER_FINANCE_COST] if TOTAL_OTHER_FINANCE_COST in data_frame.columns else 0,
                    taxProvision=row[TAX_PROVISION] if TAX_PROVISION in data_frame.columns else 0,
                )
            )
        return result

    @classmethod
    def extract_date_time_information(cls, entries: list[IncomeStatementDataClass]):
        result = []
        for entry in entries:
            result.append(
                IncomeStatementDataClass.mockk(
                    asOfDate=entry.asOfDate,
                    periodType=entry.periodType
                ),
            )
        return  result

    def get_entry_of(self, as_of_date: Date, period_type: PeriodType):
        for entry in self.entries:
            if entry.asOfDate == as_of_date and entry.periodType == period_type:
                return entry
        return 0

    def get_most_recent_expenses(self, capital_expenditure):
        entry: IncomeStatementDataClass = YQDataFrameData.get_most_recent_entry(self.entries)
        return Expenses(
            capital_expenditure=capital_expenditure,
            interest_expense=entry.interest_expense,
            interest_expense_non_operating=entry.interest_expense_non_operating,
            total_other_finance_cost=entry.total_other_finance_cost
        )

    def evaluate_growth_criteria(self, attribute: DictKey) -> bool:
        if attribute == DictKey.NET_INCOME:
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=YQDataFrameData.sorted(self.entries),
                    attribute=GrowthCriteria.NET_INCOME.__str__
                ),
                percentage_requirement=GrowthCriteria.NET_INCOME.__percentage_criteria__
            )
        elif attribute == DictKey.SALES:
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=YQDataFrameData.sorted(self.entries),
                    attribute=GrowthCriteria.SALES.__str__
                ),
                percentage_requirement=GrowthCriteria.SALES.__percentage_criteria__
            )
        raise TypeError(WRONG_TYPE_STRING.format(type=attribute))

    @classmethod
    def mockk(cls):
        return IncomeStatementData(entries=[])
