from classes.StockCollectionClass import StockCollection

class FrenchStocksClass(StockCollection):
    """A class representing the French stocks collection."""

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
        df = self.getDataFrame(
            source=self.source,
            tableIndex=self.tableIndex
        )
        self.dataFrameToCsv(
            df=self.modifyTickers(df),
            fileName=self.csvSymbols,
            column=self.column
        )

    def modifyTickers(self, df):
        return df[self.column] + self.stockTickerSignature