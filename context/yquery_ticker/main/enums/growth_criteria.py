from enum import Enum


class GrowthCriteria(Enum):
    EARNINGS = ("earnings", 10)
    REVENUE = ("revenue", 10)
    NET_INCOME = ("netIncome", 10)
    BOOK_VALUE_AND_DIVIDENDS = ("Book Value + Dividends", 10)
    SALES = ("totalRevenue", 10)
    OPERATING_CASH_FLOW = ("operatingCashFlow", 10)
    FREE_CASH_FLOW = ("freeCashFlow", 1)
    ROIC = ("Return On Income Capital", 15)
    ROE = ("Return On Equity", 15)
    OWNER_EARNINGS = ("Owner Earnings", 10)

    @property
    def __str__(self):
        return self.value[0]

    @property
    def __percentage_criteria__(self):
        return self.value[1]
