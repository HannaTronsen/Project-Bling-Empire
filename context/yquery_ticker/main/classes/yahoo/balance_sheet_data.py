from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.data_classes.date import Date, PeriodType
from context.yquery_ticker.main.data_classes.yq_data_frame_data.balance_sheet import (
    BalanceSheetDataClass,
    COMMON_STOCK_EQUITY, TOTAL_DEBT, ACCOUNTS_RECEIVABLE, ACCOUNTS_PAYABLE
)
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import (
    PERIOD_TYPE,
    AS_OF_DATE
)


class BalanceSheetData(TimeSeriesDataCollection):

    def __init__(self, entries):
        self.entries: list[BalanceSheetDataClass] = entries

    @classmethod
    def convert_data_frame_to_time_series_model(cls, data_frame):
        result = []
        data_columns = [
            ('commonStockEquity', COMMON_STOCK_EQUITY),
            ('totalDebt', TOTAL_DEBT),
            ('accountsReceivable', ACCOUNTS_RECEIVABLE),
            ('accountsPayable', ACCOUNTS_PAYABLE),
        ]
        for index, row in data_frame.iterrows():
            result.append(
                BalanceSheetDataClass(
                    asOfDate=Date.convert_date(Date.from_data_frame(row[AS_OF_DATE])),
                    periodType=Date.to_period_type(row[PERIOD_TYPE]),
                    **{key: row[column] if column in data_frame.columns else 0 for key, column in data_columns}
                )
            )
        return result

    def get_entry_of(self, as_of_date: Date, period_type: PeriodType):
        for entry in self.entries:
            if entry.asOfDate == as_of_date and entry.periodType == period_type:
                return entry
        return BalanceSheetDataClass.mockk(
            asOfDate=as_of_date,
            periodType=period_type,
        )

    @classmethod
    def extract_date_time_information(cls, entries: list[BalanceSheetDataClass]):
        result = []
        for entry in entries:
            result.append(
                BalanceSheetDataClass.mockk(
                    asOfDate=entry.asOfDate,
                    periodType=entry.periodType
                ),
            )
        return result

    @classmethod
    def mockk(cls):
        return BalanceSheetData(entries=[])
