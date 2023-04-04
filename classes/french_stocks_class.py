import pandas as pd

from classes.stock_collection_class import stock_collection_class

class french_stocks_class(stock_collection_class):
    """
    A class representing the French stocks collection.
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

        PA = self.stockTickerSuffixes[0]
        NX = self.stockTickerSuffixes[1]

        df1 = df[self.column] + PA
        df2 = df.copy()[self.column] + NX

        return pd.concat([df1, df2])
