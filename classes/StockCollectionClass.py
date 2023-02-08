from abc import ABC, abstractmethod

import pandas as pd

from const import CSV_SYMBOL_FILE_NAME, TICKERS_PATH

class StockCollection(ABC):

    def __init__(self, name, country, source, column):
        """
        Initialize a new instance of a `StockCollection` class.

        :param name: The name of the stock collection.
        :param country: The country of the stock collection.
        :param source: The source of the stock data.
        :param column: The column where the Tickers are located.
        """
        self.name = name
        self.country = country
        self.source = source
        self.csvSymbols = self.name + CSV_SYMBOL_FILE_NAME
        self.column = column

    def dataFrameToCsv(
        self,
        df,
        fileName,
        column,
        header=False,
        index=False
    ):
        df.to_csv(
            TICKERS_PATH+fileName,
            columns=column,
            header=header,
            index=index
        )

    @abstractmethod
    def convertDataFrameToCsv(self):
        pass

    def getDataFrame(
        self,
        source,
        tableIndex
    ):
        tables = pd.read_html(source)
        return tables[tableIndex]

    def __str__(self):
        return self.name