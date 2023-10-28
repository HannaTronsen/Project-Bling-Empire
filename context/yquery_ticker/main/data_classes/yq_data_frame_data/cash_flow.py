from dataclasses import dataclass
from typing import Optional

from context.yquery_ticker.main.classes.iterable_data import IterableDataInterface
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData

CASH_DIVIDENDS_PAID = 'CashDividendsPaid'
OPERATING_CASH_FLOW = 'OperatingCashFlow'
FREE_CASH_FLOW = 'FreeCashFlow'
CAPITAL_EXPENDITURE = 'CapitalExpenditure'


@dataclass
class CashFlowDataClass(IterableDataInterface, YQDataFrameData):
    cashDividendsPaid: Optional[float]
    operatingCashFlow: Optional[float]
    freeCashFlow: Optional[float]
    capitalExpenditure: Optional[float]

    @classmethod
    def mockk(cls, asOfDate, periodType):
        return CashFlowDataClass(
            asOfDate=asOfDate,
            periodType=periodType,
            cashDividendsPaid=None,
            operatingCashFlow=None,
            freeCashFlow=None,
            capitalExpenditure=None
        )
