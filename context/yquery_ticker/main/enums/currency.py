from enum import Enum
from .country import Country


class Currency(Enum):
    NOK = "NOK"
    USD = "USD"

    @classmethod
    def from_str(cls, currency_str):
        try:
            return cls(currency_str)
        except ValueError:
            return None
