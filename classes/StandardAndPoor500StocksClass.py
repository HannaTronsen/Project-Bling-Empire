from classes.StockCollectionClass import StockCollection

class StandardAndPoor500StocksClass(StockCollection):
    """A class representing the Standard and Poor 500 stocks collection."""

    def __init__(
        self,
        name,
        country,
        source,
        tableIndex,
        column,
    ):  # Initialize a new instance of a `StandardAndPoor500` class.

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