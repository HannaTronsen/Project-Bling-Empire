from .stock_collection import StockCollectionClass


class StandardAndPoor500StocksClass(StockCollectionClass):

    def __init__(self, stock_index_name, source, column, table_index):
        super().__init__(stock_index_name, source, column, table_index)
