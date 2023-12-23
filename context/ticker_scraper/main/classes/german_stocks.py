from .stock_collection import StockCollectionClass


class GermanStocksClass(StockCollectionClass):

    def __init__(self, stock_index_name, source, column, table_index):
        super().__init__(stock_index_name, source, column, table_index)

    def get_default_currency(self):
        return None
