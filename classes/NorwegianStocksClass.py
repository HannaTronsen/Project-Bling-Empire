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
        stockTickerSignature
    ):  
        # :param tableIndex: The index of the stock data table.
        # :param stockTickerSignature: The Stock ticker ending required by yfinance 
        self.set_attributes(name, country, source, column)
        self.tableIndex = tableIndex
        self.stockTickerSignature = stockTickerSignature

    def convertDataFrameToCsv(self):
        df = self.getDataFrame(tableIndex=self.tableIndex)
        self.dataFrameToCsv(df=self.modifyTickers(df))

    def modifyTickers(self, df):
        return df[self.column].str.replace('OSE: ', '') + self.stockTickerSignature
