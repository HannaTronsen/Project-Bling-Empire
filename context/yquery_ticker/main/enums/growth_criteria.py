from enum import Enum
from typing import Optional


def percentage_of(value: int): return value
def attribute_of(value: Optional[str]): return value


class GrowthCriteria(Enum):
    EARNINGS = ("Earnings", attribute_of("earnings"), percentage_of(10))
    REVENUE = ("Revenue", attribute_of("revenue"), percentage_of(10))
    NET_INCOME = ("Net Income", attribute_of("netIncome"), percentage_of(10))
    BOOK_VALUE_AND_DIVIDENDS = ("Book Value + Dividends", attribute_of(None), percentage_of(10))
    SALES = ("Total Revenue", attribute_of("totalRevenue"), percentage_of(10))
    OPERATING_CASH_FLOW = ("Operating Cash Flow", attribute_of("operatingCashFlow"), percentage_of(10))
    FREE_CASH_FLOW = ("Free Cash Flow", attribute_of("freeCashFlow"), percentage_of(10))
    ROIC = ("Return On Income Capital", attribute_of(None), percentage_of(15))
    ROE = ("Return On Equity", attribute_of(None), percentage_of(15))
    OWNER_EARNINGS = ("Owner Earnings", attribute_of(None), percentage_of(10))

    @property
    def __str__(self):
        return self.value[0]

    @property
    def attribute(self):
        return self.value[1]

    @property
    def percentage_criteria(self):
        return self.value[2]
