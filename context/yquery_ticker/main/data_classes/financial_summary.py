from dataclasses import dataclass
from typing import Optional

from .financial_data import PriceToEarnings
from context.yquery_ticker.main.interfaces.castable_data import CastableDataInterface
from ..classes.iterable_data import IterableDataInterface
from ..enums.currency import Currency


@dataclass
class FinancialSummary(IterableDataInterface, CastableDataInterface):
    previous_close: Optional[float]
    open: Optional[float]
    dividend_rate: Optional[float]
    beta: Optional[float]
    price_to_earnings: Optional[PriceToEarnings]
    market_cap: Optional[float]
    currency: Currency
