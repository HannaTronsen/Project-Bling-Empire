from .stock_collection import StockCollectionClass


class GermanStocksClass(StockCollectionClass):

    def __init__(self, stock_index_name, source, column, table_index):
        # :param table_index: The index of the stock data table.
        super().__init__(stock_index_name, source, column)
        self.table_index = table_index

    def fetch_stock_tickers(self):
        df = self.get_data_frame(table_index=self.table_index)
        self.data_frame_to_csv(df=df)
