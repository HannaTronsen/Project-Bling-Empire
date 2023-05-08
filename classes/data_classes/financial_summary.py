from dataclasses import dataclass
from classes.data_classes.iterable_data import IterableDataInterface

from enums.currency import Currency

@dataclass
class FinancialSummary(IterableDataInterface):
   previousClose: float
   open: float
   dividend_rate: float
   beta: float
   trailing_PE: float
   forward_PE: float
   market_cap: float
   currency: Currency   
   