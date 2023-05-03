import pandas as pd

from classes.stock_collection import StockCollectionClass

class FrenchStocksClass(StockCollectionClass):

    def __init__(
        self,
        name,
        country,
        source,
        column,
        table_index,
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
        pa = self.stock_ticker_suffixes[0]
        nx = self.stock_ticker_suffixes[1]

        df1 = df[self.column] + pa
        df2 = df.copy()[self.column] + nx

        return pd.concat([df1, df2])
