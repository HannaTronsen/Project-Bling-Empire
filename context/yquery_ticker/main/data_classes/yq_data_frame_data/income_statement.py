from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData


class PeriodType(Enum):
    MONTH_3 = auto()
    MONTH_12 = auto()
    TTM = auto()


AS_OF_DATE = 'asOfDate'
PERIOD_TYPE = 'periodType'
NET_INCOME = 'NetIncome'


@dataclass
class IncomeStatementDataClass(YQDataFrameData):
    asOfDate: Date
    periodType: PeriodType
    netIncome: Optional[float]
