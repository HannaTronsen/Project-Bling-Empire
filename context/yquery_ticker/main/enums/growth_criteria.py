from enum import Enum


class GrowthCriteria(Enum):
    EARNINGS = ("Earnings", 10)
    REVENUE = ("Revenue", 10)
    NET_INCOME = ("Net Income", 10)
    BOOK_VALUE_AND_DIVIDENDS = ("Book Value + Dividends", 10)
    SALES = ("Total Revenue", 10)
    OPERATING_CASH_FLOW = ("Operating Cash Flow", 10)
    FREE_CASH_FLOW = ("Free Cash Flow", 1)
    ROIC = ("Return On Income Capital", 15)
    ROE = ("Return On Equity", 15)
    OWNER_EARNINGS = ("Owner Earnings", 10)

    @property
    def __str__(self):
        return self.value[0]

    @property
    def __percentage_criteria__(self):
        return self.value[1]
