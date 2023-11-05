from enum import Enum


class GrowthCriteria(Enum):
    EARNINGS = ("Earnings", "earnings", 10)
    REVENUE = ("Revenue", "revenue", 10)
    NET_INCOME = ("Net Income", "netIncome", 10)
    BOOK_VALUE_AND_DIVIDENDS = ("Book Value + Dividends", None, 10)
    SALES = ("Total Revenue", "totalRevenue", 10)
    OPERATING_CASH_FLOW = ("Operating Cash Flow", "operatingCashFlow", 10)
    FREE_CASH_FLOW = ("Free Cash Flow", "freeCashFlow", 1)
    ROIC = ("Return On Income Capital", None, 15)
    ROE = ("Return On Equity", None, 15)
    OWNER_EARNINGS = ("Owner Earnings", None, 10)

    @property
    def __str__(self):
        return self.value[0]

    @property
    def __attribute__(self):
        return self.value[1]

    @property
    def __percentage_criteria__(self):
        return self.value[2]
