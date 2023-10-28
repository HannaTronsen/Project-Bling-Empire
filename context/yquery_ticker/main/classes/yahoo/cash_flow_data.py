from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.const import WRONG_TYPE_STRING
from context.yquery_ticker.main.data_classes.date import Date, PeriodType
from context.yquery_ticker.main.data_classes.yq_data_frame_data.cash_flow import (
    CashFlowDataClass,
    CASH_DIVIDENDS_PAID, OPERATING_CASH_FLOW, FREE_CASH_FLOW, CAPITAL_EXPENDITURE
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
        for index, row in data_frame.iterrows():
            result.append(
                CashFlowDataClass(
                    asOfDate=Date.convert_date(Date.from_data_frame(row[AS_OF_DATE])),
                    periodType=Date.to_period_type(row[PERIOD_TYPE]),
                    cashDividendsPaid=row[CASH_DIVIDENDS_PAID] if CASH_DIVIDENDS_PAID in data_frame.columns else 0,
                    operatingCashFlow=row[OPERATING_CASH_FLOW] if OPERATING_CASH_FLOW in data_frame.columns else 0,
                    freeCashFlow=row[FREE_CASH_FLOW] if FREE_CASH_FLOW in data_frame.columns else 0,
                    capitalExpenditure=row[CAPITAL_EXPENDITURE] if CAPITAL_EXPENDITURE in data_frame.columns else 0,
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
                return entry.cashDividendsPaid
        return 0

    def get_most_recent_capital_expenditure(self):
        entry: CashFlowDataClass = YQDataFrameData.get_most_recent_entry(self.entries)
        return entry.capitalExpenditure

    def evaluate_growth_criteria(self, attribute: DictKey) -> bool:
        if attribute == DictKey.OPERATING_CASH_FLOW:
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=YQDataFrameData.sorted(self.entries),
                    attribute=GrowthCriteria.OPERATING_CASH_FLOW.__str__
                ),
                percentage_requirement=GrowthCriteria.OPERATING_CASH_FLOW.__percentage_criteria__
            )
        elif attribute == DictKey.FREE_CASH_FLOW:
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=YQDataFrameData.sorted(self.entries),
                    attribute=GrowthCriteria.FREE_CASH_FLOW.__str__
                ),
                percentage_requirement=GrowthCriteria.FREE_CASH_FLOW.__percentage_criteria__
            )
        raise TypeError(WRONG_TYPE_STRING.format(type=attribute))

    @classmethod
    def mockk(cls):
        return CashFlowData(entries=[])
