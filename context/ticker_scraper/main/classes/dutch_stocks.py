from .stock_collection import StockCollectionClass

class DutchStocksClass(StockCollectionClass):
    
    def __init__(
        self,
        stock_index_name,
        source,
        column,
        table_index,
        stock_ticker_suffixes
    ):
        """
        :param table_index: The index of the stock data table.
        :param stock_ticker_suffixes: The possible stock ticker endings required by yquery
        """
        self.set_attributes(stock_index_name, source, column)
        self.table_index = table_index
        self.stock_ticker_suffixes = stock_ticker_suffixes

    def fetch_stock_tickers(self):
        df = self.get_data_frame(table_index=self.table_index)
        self.data_frame_to_csv(df=self.modify_tickers(df))

    def modify_tickers(self, df):
        as_suffix = self.stock_ticker_suffixes[0]
        return df[self.column] + as_suffix