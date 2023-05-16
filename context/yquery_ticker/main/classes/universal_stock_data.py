
from typing import Type
from context.yquery_ticker.main.data_classes.financial_data import FinancialData
from context.yquery_ticker.main.data_classes.general_stock_info import GeneralStockInfo
from context.yquery_ticker.main.utils.dict_key_enum import DictKey


class UniversalStockDataClass():

    def __init__(
        self,
        general_stock_info: GeneralStockInfo,
        financial_data: FinancialData
    ):
        self.general_stock_info: Type[GeneralStockInfo] = general_stock_info.handle_null_values()
        self.financial_data: Type[FinancialData] = financial_data.handle_null_values()

    def get_revenue_data(self):
        return {
            DictKey.TOTAl_REVENUE : self.financial_data.total_revenue,
            DictKey.REVENUE_PER_SHARE: self.financial_data.revenue_per_share,
            DictKey.REVENUE_GROWTH: self.financial_data.revenue_growth
        }
    
    def get_debt_data(self):
        return {
            DictKey.TOTAL_DEBT: self.financial_data.total_debt,
            DictKey.DEBT_TO_EQUIT: self.financial_data.debt_to_equity
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
