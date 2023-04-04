from classes.stock_collection_class import stock_collection_class


class dutch_stocks_class(stock_collection_class):
    """
    A class representing the Ductch stocks collection.
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
        AS = self.stockTickerSuffixes[0]
        return df[self.column] + AS
