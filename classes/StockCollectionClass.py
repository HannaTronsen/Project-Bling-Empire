import pandas as pd
from abc import ABC, abstractmethod
from const import FILE_NAME_SUFFIX, STOCK_COLLECTIONS_PATH


class StockCollection(ABC):

    def __init__(self, name, country, source, column):
        """
        Initialize a new instance of a `StockCollection` class.

        :param name: The name of the stock collection.
        :param country: The country of the stock collection.
        :param source: The source of the stock data.
        :param column: The column where the Tickers are located.

        :def set_attributes: Results in less code for each subclass of this class
        """
        self.set_attributes(name, country, source, column)

    def set_attributes(self, name, country, source, column):
        self.name = name
        self.country = country
        self.source = source
        self.fileName = self.name + FILE_NAME_SUFFIX
        self.filePath = f"{STOCK_COLLECTIONS_PATH}{self.fileName}"
        self.column = column

    def dataFrameToCsv(
        self,
        df,
        header=False,
        index=False
    ):
        df.to_csv(
            self.filePath,
            columns=[self.column],
            header=header,
            index=index
        )

    @abstractmethod
    def fetchStockTickers(self):
        pass

    def getDataFrame(
        self,
        tableIndex
    ):
        tables = pd.read_html(self.source)
        return tables[tableIndex]

    def __str__(self):
        return self.name
