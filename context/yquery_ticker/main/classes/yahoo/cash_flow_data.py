from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.data_classes.date import Date, PeriodType
from context.yquery_ticker.main.data_classes.yq_data_frame_data.cash_flow import (
    CashFlowDataClass,
    CASH_DIVIDENDS_PAID
)
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import (
    PERIOD_TYPE,
    AS_OF_DATE,
)


class CashFlowData(TimeSeriesDataCollection):
    def __init__(self, entries):
        self.entries: CashFlowDataClass = entries

    @classmethod
    def convert_data_frame_to_time_series_model(cls, data_frame):
        result = []
        for index, row in data_frame.iterrows():
            result.append(
                CashFlowDataClass(
                    asOfDate=Date.convert_date(Date.from_data_frame(row[AS_OF_DATE])),
                    periodType=Date.to_period_type(row[PERIOD_TYPE]),
                    cashDividendsPaid=row[CASH_DIVIDENDS_PAID],
                )
            )
        return result

    def get_entry_of(self, as_of_date: Date, period_type: PeriodType):
        for entry in self.entries:
            if entry.asOfDate == as_of_date and entry.periodType == period_type:
                return abs(entry.cashDividendsPaid)
        return 0

    @classmethod
    def mockk(cls):
        return CashFlowData(entries=[])
