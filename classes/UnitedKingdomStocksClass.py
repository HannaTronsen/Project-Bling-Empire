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
    ):  # Initialize a new instance of a `UnitedKingdomStocks` class.

        super().__init__(
            name=name,
            country=country,
            source=source,
            column=column
        )

        # :param tableIndex: The index of the stock data table.
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