from typing import Type
from context.yquery_ticker.main.classes.data_frame_data import DataFrameData
from context.yquery_ticker.main.classes.historical_earnings import HistoricalEarnings
from context.yquery_ticker.main.data_classes.financial_data import FinancialData
from context.yquery_ticker.main.data_classes.general_stock_info import GeneralStockInfo
from context.yquery_ticker.main.utils.dict_key_enum import DictKey


class UniversalStockDataClass:

    def __init__(
            self,
            general_stock_info: GeneralStockInfo,
            financial_data: FinancialData,
            historical_earnings: HistoricalEarnings,
            test_data_frame_data: DataFrameData
    ):
        self.general_stock_info: Type[GeneralStockInfo] = general_stock_info.normalize_values()
        self.financial_data: Type[FinancialData] = financial_data.normalize_values()
        self.historical_earnings: HistoricalEarnings = historical_earnings
        self.test_data_frame_data: DataFrameData = test_data_frame_data

    def get_revenue_data(self):
        return {
            DictKey.TOTAl_REVENUE: self.financial_data.total_revenue,
            DictKey.REVENUE_PER_SHARE: self.financial_data.revenue_per_share,
            DictKey.REVENUE_GROWTH: self.financial_data.revenue_growth
        }

    def get_earnings_data(self):
        return {
            DictKey.EARNINGS_PER_SHARE: self.financial_data.earnings_per_share,
            DictKey.NET_EARNINGS: self.financial_data.net_income_to_common,
            DictKey.EARNINGS_GROWTH: self.financial_data.earnings_growth
        }

    def get_debt_data(self):
        return {
            DictKey.TOTAL_DEBT: self.financial_data.total_debt,
            DictKey.DEBT_TO_EQUITY: self.financial_data.debt_to_equity
        }

    def get_margins_data(self):
        return {
            DictKey.PROFIT_MARGINS: self.financial_data.profit_margins,
            DictKey.GROSS_PROFIT_MARGINS: self.financial_data.gross_profit_margins,
            DictKey.OPERATING_MARGINS: self.financial_data.operating_margins
        }

    def get_dividend_data(self):
        return {
            DictKey.DIVIDEND_RATE: self.financial_data.dividend_rate,
            DictKey.DIVIDEND_YIELD: self.financial_data.dividend_yield,
            DictKey.FIVE_YEAR_AVG_DIVIDEND_YIELD: self.financial_data.five_year_avg_dividend_yield,
            DictKey.TRAILING_ANNUAL_DIVIDEND_RATE: self.financial_data.trailing_annual_dividend_rate,
            DictKey.TRAILING_ANNUAL_DIVIDEND_YIELD: self.financial_data.trailing_annual_dividend_yield,
        }

    def get_financial_ratio_data(self):
        return {
            DictKey.DEBT_TO_EQUITY: self.financial_data.debt_to_equity,
            DictKey.PRICE_TO_CASH_FLOW: self.financial_data.calculate_price_to_cashflow,
            DictKey.ENTERPRISE_TO_EBITDA: self.financial_data.enterprise_to_ebitda,
            DictKey.PRICE_TO_BOOK: self.financial_data.price_to_book,
            DictKey.PRICE_TO_EARNINGS: self.financial_data.price_to_earnings,
            DictKey.EARNINGS_PER_SHARE: self.financial_data.earnings_per_share,
            DictKey.ENTERPRISE_TO_REVENUE: self.financial_data.enterprise_to_revenue
        }

    def get_cash_flow_data(self):
        return {
            DictKey.FREE_CASH_FLOW: self.financial_data.free_cash_flow,
            DictKey.OPERATING_CASH_FLOW: self.financial_data.operating_cash_flow,
        }

    def get_profitability_and_return_data(self):
        return {
            DictKey.RETURN_ON_EQUITY: self.financial_data.return_on_equity,
            DictKey.RETURN_ON_ASSETS: self.financial_data.return_on_assets,
            DictKey.RETURN_ON_INVESTED_CAPITAL: self.financial_data.calculate_return_on_invested_capital,
            DictKey.RETURN_ON_INVESTMENT: self.financial_data.calculate_return_on_investment
        }
