import pandas as pd
from classes.stock_collection_class import stock_collection_class


class united_kingdom_stocks_class(stock_collection_class):
    """
    A class representing the United Kingdom stocks collection.
    """

    def __init__(
        self,
        name,
        country,
        source,
        tableIndex,
        column,
        stockTickerSuffixes
    ):
        # :param tableIndex: The index of the stock data table.
        # :param stockTickerSuffixes: The possibble stock ticker endings required by yfinance
        self.set_attributes(name, country, source, column)
        self.tableIndex = tableIndex
        self.stockTickerSuffixes = stockTickerSuffixes

    # @override
    def fetchStockTickers(self):
        df = self.getDataFrame(tableIndex=self.tableIndex)
        self.dataFrameToCsv(df=self.modifyTickers(df))

    def modifyTickers(self, df):

        L = self.stockTickerSuffixes[0]
        IL = self.stockTickerSuffixes[1]

        df1 = df[self.column]
        df2 = df.copy()[self.column] + L
        df3 = df.copy()[self.column] + IL

        return pd.concat([df1, df2, df3])
