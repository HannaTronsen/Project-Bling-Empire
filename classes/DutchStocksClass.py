from classes.StockCollectionClass import StockCollection

class DutchStocksClass(StockCollection):
    """A class representing the Ductch stocks collection."""

    def __init__(
        self,
        name,
        country,
        source,
        tableIndex,
        column,
        tickerSignature
    ):  
        # :param tableIndex: The index of the stock data table.
        # :param ticketSignature: The Stock ticker ending required by yfinance 
        self.set_attributes(name, country, source, column)
        self.tableIndex = tableIndex
        self.tickerSignature = tickerSignature

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
        return df[self.column] + self.tickerSignature
