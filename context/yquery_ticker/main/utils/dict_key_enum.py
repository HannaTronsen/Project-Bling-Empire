from enum import Enum


class DictKey(Enum):
    TOTAl_REVENUE = 'total_revenue'
    REVENUE_PER_SHARE = 'revenue_per_share'
    REVENUE_GROWTH = 'revenue_growth'
    TOTAL_DEBT = 'total_debt'
    DEBT_TO_EQUIT = 'debt_to_equity'
    PROFIT_MARGINS = 'profit_margins'
    GROSS_PROFIT_MARGINS = 'gross_profit_margins'
    OPERATING_MARGINS = 'operating_margins'
    DIVIDEND_RATE = 'dividend_rate'
    DIVIDEND_YIELD = 'dividend_yield'
    FIVE_YEAR_AVG_DIVIDEND_YIELD = 'five_year_avg_dividend_yield'
    TRAILING_ANNUAL_DIVIDEND_RATE = 'trailing_annual_dividend_rate'
    TRAILING_ANNUAL_DIVIDEND_YIELD = 'trailing_annual_dividend_yield'