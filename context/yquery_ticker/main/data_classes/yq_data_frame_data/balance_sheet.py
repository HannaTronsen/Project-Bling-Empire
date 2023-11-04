from dataclasses import dataclass
from typing import Optional

from context.yquery_ticker.main.classes.iterable_data import IterableDataInterface
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData

COMMON_STOCK_EQUITY = 'CommonStockEquity'
TOTAL_DEBT = 'TotalDebt'
ACCOUNTS_RECEIVABLE = 'AccountsReceivable'
ACCOUNTS_PAYABLE = 'AccountsPayable'


@dataclass
class BalanceSheetDataClass(IterableDataInterface, YQDataFrameData):
    commonStockEquity: Optional[float]
    totalDebt: Optional[float]
    accountsReceivable: Optional[float]
    accountsPayable: Optional[float]

    @classmethod
    def mockk(cls, asOfDate, periodType):
        return BalanceSheetDataClass(
            asOfDate=asOfDate,
            periodType=periodType,
            commonStockEquity=0,
            totalDebt=0,
            accountsReceivable=0,
            accountsPayable=0,
        )
