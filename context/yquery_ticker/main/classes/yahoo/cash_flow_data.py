from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.const import WRONG_TYPE_STRING
from context.yquery_ticker.main.data_classes.date import Date, PeriodType
from context.yquery_ticker.main.data_classes.yq_data_frame_data.cash_flow import (
    CashFlowDataClass,
    CASH_DIVIDENDS_PAID, OPERATING_CASH_FLOW, FREE_CASH_FLOW, CAPITAL_EXPENDITURE, DEPRECIATION_AND_AMORTIZATION
)
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import (
    PERIOD_TYPE,
    AS_OF_DATE, YQDataFrameData,
)
from context.yquery_ticker.main.enums.growth_criteria import GrowthCriteria
from context.yquery_ticker.main.utils.dict_key_enum import DictKey


class CashFlowData(TimeSeriesDataCollection):
    def __init__(self, entries):
        self.entries: list[CashFlowDataClass] = entries

    @classmethod
    def convert_data_frame_to_time_series_model(cls, data_frame):
        result = []
        data_columns = [
            ('cashDividendsPaid', CASH_DIVIDENDS_PAID),
            ('operatingCashFlow', OPERATING_CASH_FLOW),
            ('freeCashFlow', FREE_CASH_FLOW),
            ('capitalExpenditure', CAPITAL_EXPENDITURE),
            ('depreciationAndAmortization', DEPRECIATION_AND_AMORTIZATION),
        ]
        for index, row in data_frame.iterrows():
            result.append(
                CashFlowDataClass(
                    asOfDate=Date.convert_date(Date.from_data_frame(row[AS_OF_DATE])),
                    periodType=Date.to_period_type(row[PERIOD_TYPE]),
                    **{key: row[column] if column in data_frame.columns else 0 for key, column in data_columns}
                )
            )
        return result

    @classmethod
    def extract_date_time_information(cls, entries: list[CashFlowDataClass]):
        result = []
        for entry in entries:
            result.append(
                CashFlowDataClass.mockk(
                    asOfDate=entry.asOfDate,
                    periodType=entry.periodType
                ),
            )
        return result

    def get_entry_of(self, as_of_date: Date, period_type: PeriodType):
        for entry in self.entries:
            if entry.asOfDate == as_of_date and entry.periodType == period_type:
                return entry
        return CashFlowDataClass.mockk(
            asOfDate=as_of_date,
            periodType=period_type,
        )

    def get_most_recent_capital_expenditure(self):
        entry: CashFlowDataClass = YQDataFrameData.get_most_recent_entry(self.entries)
        return entry.capitalExpenditure

    def evaluate_growth_criteria(self, percentage_criteria: int, attribute: str) -> bool:
        return self.passes_percentage_increase_requirements(
            percentages=self.calculate_percentage_increase_for_model_list(
                model_list=YQDataFrameData.sorted(self.entries),
                attribute=attribute
            ),
            percentage_requirement=percentage_criteria
        )


    @classmethod
    def mockk(cls):
        return CashFlowData(entries=[])
