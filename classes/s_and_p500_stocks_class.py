from classes.stock_collection_class import stock_collection_class


class standard_and_poor500_stocks_class(stock_collection_class):
    """
    A class representing the Standard and Poor 500 stocks collection.
    """

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
