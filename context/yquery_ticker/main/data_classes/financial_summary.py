from dataclasses import dataclass

from context.yquery_ticker.main.data_classes.castable_data import CastableDataInterface
from .iterable_data import IterableDataInterface
from ..enums.currency import Currency

@dataclass
class FinancialSummary(IterableDataInterface, CastableDataInterface):
   previous_close: float
   open: float
   dividend_rate: float
   beta: float
   trailing_PE: float
   forward_PE: float
   market_cap: float
   currency: Currency   
   