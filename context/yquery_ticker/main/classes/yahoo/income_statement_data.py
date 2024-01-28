from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
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


class IncomeStatementData(TimeSeriesDataCollection):

    def __init__(self, entries):
        self.entries: list[IncomeStatementDataClass] = entries

    @classmethod
    def convert_data_frame_to_time_series_model(cls, data_frame):
        result = []
        data_columns = [
            ('netIncome', NET_INCOME),
            ('totalRevenue', TOTAL_REVENUE),
            ('interest_expense', INTEREST_EXPENSE),
            ('interest_expense_non_operating', INTEREST_EXPENSE_NON_OPERATING),
            ('total_other_finance_cost', TOTAL_OTHER_FINANCE_COST),
            ('taxProvision', TAX_PROVISION),
        ]

        for index, row in data_frame.iterrows():
            result.append(
                IncomeStatementDataClass(
                    asOfDate=Date.convert_date(Date.from_data_frame(row[AS_OF_DATE])),
                    periodType=Date.to_period_type(row[PERIOD_TYPE]),
                    **{key: row[column] if column in data_frame.columns else 0 for key, column in data_columns}
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

    def get_entry_of(self, as_of_date: Date, period_type: PeriodType):
        for entry in self.entries:
            if entry.asOfDate == as_of_date and entry.periodType == period_type:
                return entry
        return IncomeStatementDataClass.mockk(
            asOfDate=as_of_date,
            periodType=period_type,
        )

    def get_most_recent_expenses(self, capital_expenditure):
        entry: IncomeStatementDataClass = YQDataFrameData.get_most_recent_entry(self.entries)
        return Expenses(
            capital_expenditure=capital_expenditure,
            interest_expense=entry.interest_expense,
            interest_expense_non_operating=entry.interest_expense_non_operating,
            total_other_finance_cost=entry.total_other_finance_cost
        )

    def evaluate_growth_criteria(self, percentage_criteria: int, attribute: str) -> bool:
        model_list = YQDataFrameData.sorted(self.entries)
        if self.is_consistently_up_trending_model_list(
                model_list=model_list,
                attribute=attribute
        ) and len(model_list) > 1:
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=model_list,
                    attribute=attribute
                ),
                percentage_requirement=percentage_criteria
            )
        return False

    @classmethod
    def mockk(cls):
        return IncomeStatementData(entries=[])
