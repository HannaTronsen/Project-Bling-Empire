from abc import ABC
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

from context.yquery_ticker.main.classes.castable_data import CastableDataInterface
from context.yquery_ticker.main.data_classes.date import Date


class PeriodType(Enum):
    MONTH_3 = auto()
    MONTH_12 = auto()
    TTM = auto()


def to_period_type(period_type) -> PeriodType:
    if period_type == "12M":
        return PeriodType.MONTH_12
    elif period_type == "3M":
        return PeriodType.MONTH_3
    elif period_type == "TTM":
        return PeriodType.TTM
    else:
        raise ValueError(f"asOfDate value was either null or not an expected value. period_type: {period_type}")


AS_OF_DATE = 'asOfDate'
PERIOD_TYPE = 'periodType'


@dataclass
class YQDataFrameData(ABC, CastableDataInterface):
    asOfDate: Optional[Date]
    periodType: Optional[PeriodType]

