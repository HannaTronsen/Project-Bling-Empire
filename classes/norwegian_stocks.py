from classes.stock_collection import StockCollectionClass

class NorwegianStocksClass(StockCollectionClass):

    def __init__(
        self,
        name,
        country,
        source,
        table_index,
        column,
        stock_ticker_suffixes
    ):
        """
        :param table_index: The index of the stock data table.
        :param stock_ticker_suffixes: The possible stock ticker endings required by yfinance.
        """
        self.set_attributes(name, country, source, column)
        self.table_index = table_index
        self.stock_ticker_suffixes = stock_ticker_suffixes

    def fetch_stock_tickers(self):
        df = self.get_data_frame(table_index=self.table_index)
        self.data_frame_to_csv(df=self.modify_tickers(df))

    def modify_tickers(self, df):
        ol = self.stock_ticker_suffixes[0]
        return df[self.column].str.replace('OSE: ', '') + ol
