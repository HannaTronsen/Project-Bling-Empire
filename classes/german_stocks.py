from classes.stock_collection import StockCollectionClass


class GermanStocksClass(StockCollectionClass):
    """
    A class representing German stocks collection.
    """

    def __init__(
        self,
        name,
        country,
        source,
        table_index,
        column,
    ):
        """
        Initialize a new instance of a `GermanStocksClass`.

        :param name: The name of the German stocks collection.
        :param country: The country of the German stocks collection.
        :param source: The source of the German stock data.
        :param table_index: The index of the stock data table.
        :param column: The column where the Tickers are located.
        """
        self.set_attributes(name, country, source, column)
        self.table_index = table_index

    def fetch_stock_tickers(self):
        """
        Fetches the stock tickers from the German stock data and writes them to a CSV file.

        :return: None
        """
        df = self.get_data_frame(table_index=self.table_index)
        self.data_frame_to_csv(df=df)
