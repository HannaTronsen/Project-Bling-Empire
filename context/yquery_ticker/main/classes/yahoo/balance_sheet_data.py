from context.yquery_ticker.main.classes.iterable_data import IterableDataInterface
from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.balance_sheet import (
    BalanceSheetDataClass,
    COMMON_STOCK_EQUITY, TOTAL_DEBT
)
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import (
    PERIOD_TYPE,
    AS_OF_DATE
)


class BalanceSheetData(IterableDataInterface, TimeSeriesDataCollection):

    @classmethod
    def convert_data_frame_to_time_series_model(cls, data_frame):
        result = []
        for index, row in data_frame.iterrows():
            result.append(
                BalanceSheetDataClass(
                    asOfDate=Date.convert_date(Date.from_data_frame(row[AS_OF_DATE])),
                    periodType=Date.to_period_type(row[PERIOD_TYPE]),
                    commonStockEquity=row[COMMON_STOCK_EQUITY],
                    totalDebt=row[TOTAL_DEBT]
                )
            )
        return result

    @classmethod
    def mockk(cls):
        return BalanceSheetData()
