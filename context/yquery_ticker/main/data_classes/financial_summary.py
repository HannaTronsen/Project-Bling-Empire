from dataclasses import dataclass
from typing import Optional

from ..classes.castable_data import CastableDataInterface
from ..classes.iterable_data import IterableDataInterface
from ..enums.currency import Currency


@dataclass
class FinancialSummary(IterableDataInterface, CastableDataInterface):
    previous_close: Optional[float]
    open: Optional[float]
    dividend_rate: Optional[float]
    beta: Optional[float]
    trailing_PE: Optional[float]
    forward_PE: Optional[float]
    market_cap: Optional[float]
    currency: Currency
