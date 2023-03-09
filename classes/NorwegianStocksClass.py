from classes.StockCollectionClass import StockCollection


class NorwegianStocksClass(StockCollection):
    """A class representing the Norwegian stocks collection."""

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
        OL = self.stockTickerSuffixes[0]
        return df[self.column].str.replace('OSE: ', '') + OL
