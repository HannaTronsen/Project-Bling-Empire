import pandas as pd

from classes.stock_collection_class import stock_collection_class


class hong_kong_stocks_class(stock_collection_class):
    """
    A class representing the Hong Kong stocks collection.
    """

    def __init__(
        self,
        name,
        country,
        source,
        tableIndexRange,
        column,
        stockTickerSuffixes
    ):
        # :param tableIndex: The index of the stock data table.
        # :param stockTickerSuffixes: The possibble stock ticker endings required by yfinance
        self.set_attributes(name, country, source, column)
        self.tableIndexRange = tableIndexRange
        self.stockTickerSuffixes = stockTickerSuffixes

    # @override
    def getDataFrame(
        self,
        tableIndexRange
    ):
        tables = pd.read_html(self.source)
        firstTableIndex = tableIndexRange[0]
        lastTableIndex = tableIndexRange[-1]

        df = pd.DataFrame()
        for tableIndex in range(firstTableIndex, lastTableIndex):
            df = pd.concat([df, tables[tableIndex]], axis=0)
        return df

    # @override
    def fetchStockTickers(self):
        df = self.getDataFrame(tableIndexRange=self.tableIndexRange)
        self.dataFrameToCsv(df=self.modifyTickers(df))

    def modifyTickers(self, df):
        # Limit posibility of getting digit in company name
        HK = self.stockTickerSuffixes[0]
        df[0] = df[0].str[:10]
        df[0] = df[0].str.replace(r'(\D+)', '', regex=True)
        return df[0].str.zfill(4) + HK
