from abc import ABC
from dataclasses import dataclass
from typing import Optional
from context.yquery_ticker.main.data_classes.date import Date, PeriodType
from context.yquery_ticker.main.interfaces.castable_data import CastableDataInterface

AS_OF_DATE = 'asOfDate'
PERIOD_TYPE = 'periodType'


@dataclass
class YQDataFrameData(ABC, CastableDataInterface):
    asOfDate: Optional[Date]
    periodType: Optional[PeriodType]
