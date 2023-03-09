from classes.StockCollectionClass import StockCollection


class GermanStocksClass(StockCollection):
    """A class representing German stocks collection."""

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

    # @override
    def fetchStockTickers(self):
        df = self.getDataFrame(tableIndex=self.tableIndex)
        self.dataFrameToCsv(df=df)
