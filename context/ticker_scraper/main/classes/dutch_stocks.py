from .stock_collection import StockCollectionClass


class DutchStocksClass(StockCollectionClass):

    def __init__(self, stock_index_name, source, column, table_index, stock_ticker_suffixes):
        """
        :param stock_ticker_suffixes: The possible stock ticker endings required by yquery
        """
        super().__init__(stock_index_name, source, column, table_index)
        self.stock_ticker_suffixes = stock_ticker_suffixes

    def save_stock_tickers_data_frame_to_csv(self, data_frame):
        self._data_frame_to_csv(data_frame=self.modify_tickers(data_frame))

    def get_default_currency(self):
        return None

    def modify_tickers(self, df):
        AS = self.stock_ticker_suffixes[0]
        return df[self.column] + AS
