
from context.yquery_ticker.main.data_classes.general_stock_info import GeneralStockInfo

class UniversalStockDataClass():

    def __init__(self, general_stock_info: GeneralStockInfo):
        self.general_stock_info = general_stock_info.handle_null_values()

        

            
