import pandas as pd
from abc import ABC, abstractmethod
from const import FILE_NAME_SUFFIX, STOCK_COLLECTIONS_PATH


class StockCollectionClass(ABC):
    """
    A base abstract class for stock collections.
    """

    def __init__(self, name, country, source, column):
        """
        Initialize a new instance of a `StockCollectionClass`.

        :param name: The name of the stock collection.
        :param country: The country of the stock collection.
        :param source: The source of the stock data.
        :param column: The column where the tickers are located.

        :def set_attributes: Results in less code for each subclass of this class
        """
        self.set_attributes(name, country, source, column)

    def set_attributes(self, name, country, source, column):
        self.name = name
        self.country = country
        self.source = source
        self.file_name = self.name + FILE_NAME_SUFFIX
        self.file_path = f"{STOCK_COLLECTIONS_PATH}{self.file_name}"
        self.column = column

    def data_frame_to_csv(self, df, header=False, index=False):
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
        return self.name
