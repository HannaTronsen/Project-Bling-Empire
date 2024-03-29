from dataclasses import dataclass
from typing import Optional

from .financial_data import PriceToEarnings
from context.yquery_ticker.main.interfaces.castable_data import CastableDataInterface
from context.yquery_ticker.main.interfaces.iterable_data import IterableDataInterface
from ..enums.currency import Currency


@dataclass
class FinancialSummary(IterableDataInterface, CastableDataInterface):
    previous_close: Optional[float]
    open: Optional[float]
    payout_ratio: Optional[float]
    ex_dividend_date: Optional[str]
    dividend_rate: Optional[float]
    beta: Optional[float]
    price_to_earnings: Optional[PriceToEarnings]
    market_cap: Optional[float]
    currency: Optional[Currency]
