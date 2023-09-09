from dataclasses import dataclass
from typing import Optional
from context.yquery_ticker.main.classes.castable_data import CastableDataInterface
from context.yquery_ticker.main.data_classes.date import Date

EPS_ACTUAL = 'epsActual'
EPS_ESTIMATE = 'epsEstimate'
EPS_DIFFERENCE = 'epsDifference'
EPS_QUARTER = 'quarter'


@dataclass
class EarningsHistoryDataClass(CastableDataInterface):
    epsActual: Optional[float]
    epsEstimate: Optional[float]
    epsDifference: Optional[float]
    quarter: Date
