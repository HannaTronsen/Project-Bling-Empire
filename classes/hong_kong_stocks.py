import pandas as pd

from classes.stock_collection import StockCollectionClass


class HongKongStocksClass(StockCollectionClass):
    """
    A class representing the Hong Kong stocks collection.
    """

    def __init__(
        self,
        name,
        country,
        source,
        table_index_range,
        column,
        stock_ticker_suffixes
    ):
        """
        Initialize a new instance of a `HongKongStocksClass`.

        :param name: The name of the Hong Kong stocks collection.
        :param country: The country of the Hong Kong stocks collection.
        :param source: The source of the Hong Kong stock data.
        :param table_index_range: The range of indices of the stock data tables.
        :param column: The column where the Tickers are located.
        :param stock_ticker_suffixes: The possible stock ticker endings required by yfinance.
        """
        self.set_attributes(name, country, source, column)
        self.table_index_range = table_index_range
        self.stock_ticker_suffixes = stock_ticker_suffixes

    def get_data_frame(self, table_index_range):
        """
        Returns a DataFrame object containing the stock data.

        :param table_index_range: The range of indices of the stock data tables.
        :return: A pandas DataFrame object containing the stock data.
        """
        tables = pd.read_html(self.source)
        first_table_index = table_index_range[0]
        last_table_index = table_index_range[-1]

        df = pd.DataFrame()
        for table_index in range(first_table_index, last_table_index):
            df = pd.concat([df, tables[table_index]], axis=0)
        return df

    def fetch_stock_tickers(self):
        """
        Fetches the stock tickers from the Hong Kong stock data and modifies them according to the stock ticker suffixes.

        :return: None
        """
        df = self.get_data_frame(table_index_range=self.table_index_range)
        self.data_frame_to_csv(df=self.modify_tickers(df))

    def modify_tickers(self, df):
        """
        Modifies the stock tickers according to the stock ticker suffixes.

        :param df: The DataFrame containing the stock tickers.
        :return: A pandas Series object with the modified stock tickers.
        """
        hk = self.stock_ticker_suffixes[0]
        df[0] = df[0].str[:10]
        df[0] = df[0].str.replace(r'(\D+)', '', regex=True)
        return df[0].str.zfill(4) + hk
