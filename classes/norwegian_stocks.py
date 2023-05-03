from classes.stock_collection import StockCollectionClass


class NorwegianStocksClass(StockCollectionClass):
    """
    A class representing the Norwegian stocks collection.
    """

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
        Initialize a new instance of a `NorwegianStocksClass`.

        :param name: The name of the Norwegian stocks collection.
        :param country: The country of the Norwegian stocks collection.
        :param source: The source of the Norwegian stock data.
        :param table_index: The index of the stock data table.
        :param column: The column where the Tickers are located.
        :param stock_ticker_suffixes: The possible stock ticker endings required by yfinance.
        """
        self.set_attributes(name, country, source, column)
        self.table_index = table_index
        self.stock_ticker_suffixes = stock_ticker_suffixes

    def fetch_stock_tickers(self):
        """
        Fetches the stock tickers from the Norwegian stock data and modifies them according to the stock ticker suffixes.

        :return: None
        """
        df = self.get_data_frame(table_index=self.table_index)
        self.data_frame_to_csv(df=self.modify_tickers(df))

    def modify_tickers(self, df):
        """
        Modifies the stock tickers according to the stock ticker suffixes.

        :param df: The DataFrame containing the stock tickers.
        :return: A pandas Series object with the modified stock tickers.
        """
        ol = self.stock_ticker_suffixes[0]
        return df[self.column].str.replace('OSE: ', '') + ol
