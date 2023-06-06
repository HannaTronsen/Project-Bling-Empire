import pandas as pd
from abc import ABC, abstractmethod


from context.ticker_scraper.main.const import FILE_NAME_SUFFIX, STOCK_COLLECTIONS_PATH


class StockCollectionClass(ABC):

    def __init__(self, stock_index_name, source, column):
        """
        :param stock_index_name: The name of the stock collection.
        :param source: The source of the stock data.
        :param column: The column where the tickers are located.

        :def set_attributes: Results in less code for each subclass of this class
        """
        self.set_attributes(stock_index_name, source, column)

    def set_attributes(self, stock_index_name, source, column):
        self.stock_index_name = stock_index_name
        self.source = source
        self.file_name = self.stock_index_name + FILE_NAME_SUFFIX
        self.file_path = f"{STOCK_COLLECTIONS_PATH}{self.file_name}"
        self.column = column

    def data_frame_to_csv(self, df: pd.DataFrame, header=False, index=False):
        """
        Save a dataframe as a CSV file.

        :param df: The dataframe to save.
        :param header: Whether to include the column names in the CSV file.
        :param index: Whether to include the row index in the CSV file.
        """
        df.to_csv(
            self.file_path,
            columns=[self.column],
            header=header,
            index=index
        )

    @abstractmethod
    def fetch_stock_tickers(self):
        """
        Abstract method to fetch the stock tickers.
        """
        pass

    def get_data_frame(self, table_index):
        """
        Get the dataframe at the specified table index.

        :param table_index: The index of the table.
        """
        tables = pd.read_html(self.source)
        return tables[table_index]

    def __str__(self):
        return self.stock_index_name
