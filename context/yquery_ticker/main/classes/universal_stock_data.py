
from typing import Type
from context.yquery_ticker.main.data_classes.financial_data import FinancialData
from context.yquery_ticker.main.data_classes.general_stock_info import GeneralStockInfo


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
            'total_revenue' : self.financial_data.total_revenue,
            'revenue_per_share': self.financial_data.revenue_per_share,
            'revenue_growth': self.financial_data.revenue_growth
        }
    
    def get_debt_data(self):
        return {
            'total_debt': self.financial_data.total_debt,
            'debt_to_equity': self.financial_data.debt_to_equity
        }
