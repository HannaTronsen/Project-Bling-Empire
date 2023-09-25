from enum import Enum


class DictKey(Enum):
    TOTAL_REVENUE = 'Total Revenue'
    REVENUE_PER_SHARE = 'Revenue Per Share'
    REVENUE_GROWTH = 'Revenue Growth'
    TOTAL_DEBT = 'Total Debt'
    DEBT_TO_EQUITY = 'Debt to Equity'
    PROFIT_MARGINS = 'Profit Margins'
    GROSS_PROFIT_MARGINS = 'Gross Profit Margins'
    OPERATING_MARGINS = 'Operating Margins'
    DIVIDEND_RATE = 'Dividend Rate'
    DIVIDEND_YIELD = 'Dividend Yield'
    FIVE_YEAR_AVG_DIVIDEND_YIELD = 'Five Year Avg Dividend Yield'
    TRAILING_ANNUAL_DIVIDEND_RATE = 'Trailing Annual Dividend Rate'
    TRAILING_ANNUAL_DIVIDEND_YIELD = 'Trailing Annual Dividend Yield'
    PRICE_TO_CASH_FLOW = 'Price to Cash Flow'
    FREE_CASH_FLOW = 'Free to Cash Flow'
    OPERATING_CASH_FLOW = 'Operating to Cash Flow'
    ENTERPRISE_TO_EBITDA = 'Enterprise to EBITDA'
    PRICE_TO_BOOK = 'Price to Book'
    PRICE_TO_EARNINGS = 'Price to Earnings'
    EARNINGS_PER_SHARE = 'Earnings Per Share'
    NET_EARNINGS = 'Net Earnings'
    EARNINGS_GROWTH = 'Earnings Growth'
    ENTERPRISE_TO_REVENUE = 'Enterprise to Revenue'
    RETURN_ON_EQUITY = 'Return on Equity'
    RETURN_ON_ASSETS = 'Return on Assets'
    RETURN_ON_INVESTED_CAPITAL = 'Return on Invested Capital'
    RETURN_ON_INVESTMENT = 'Return on Investment'

    # Growth Criteria
    EARNINGS_HISTORY = "Earnings History"
    REVENUE_HISTORY = "Revenue History"
    NET_INCOME = "Net Income"
