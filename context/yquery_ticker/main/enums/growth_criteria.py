from enum import Enum


class GrowthCriteria(Enum):
    EARNINGS = ("earnings", 1)  # TODO(Hanna): Find out what this requirement should be
    REVENUE = ("revenue", 1)  # TODO(Hanna): Find out what this requirement should be
    NET_INCOME = ("netIncome", 10)
    BOOK_VALUE_AND_DIVIDENDS = ("Book Value + Dividends", 10)
    SALES = ("totalRevenue", 10)
    OPERATING_CASH_FLOW = ("operatingCashFlow", 10)

    @property
    def __str__(self):
        return self.value[0]

    @property
    def __percentage_criteria__(self):
        return self.value[1]
