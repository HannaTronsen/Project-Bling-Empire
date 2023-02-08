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
    ):  # Initialize a new instance of a `FrenchStocks` class.

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
            df=self.modifyTickers(df),
            fileName=self.csvSymbols,
            column=self.column
        )

    def modifyTickers(self, df):
        return df['Ticker'] + '.PA'