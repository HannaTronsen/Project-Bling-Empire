from dataclasses import dataclass
from typing import Optional
from context.yquery_ticker.main.classes.castable_data import CastableDataInterface
from context.yquery_ticker.main.data_classes.date import Date


@dataclass
class EarningsHistory(CastableDataInterface):
    epsActual: Optional[float]
    epsEstimate: Optional[float]
    epsDifference: Optional[float]
    surprisePercent: Optional[float]
    quarter: Date
