from classes.StockCollectionClass import StockCollection

class UnitedKingdomStocksClass(StockCollection):
    """A class representing the United Kingdom stocks collection."""

    def __init__(
        self,
        name,
        country,
        source,
        tableIndex,
        column,
    ):  
        # :param tableIndex: The index of the stock data table.
        self.set_attributes(name, country, source, column)
        self.tableIndex = tableIndex

    def convertDataFrameToCsv(self):
        df = self.getDataFrame(
            source=self.source,
            tableIndex=self.tableIndex
        )
        self.dataFrameToCsv(
            df=df,
            fileName=self.csvSymbols,
            column=self.column
        )