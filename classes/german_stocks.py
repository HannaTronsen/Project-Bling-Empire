from classes.stock_collection import StockCollectionClass

class GermanStocksClass(StockCollectionClass):

    def __init__(
        self,
        name,
        country,
        source,
        column,
        table_index,
    ):
        #:param table_index: The index of the stock data table.  
        self.set_attributes(name, country, source, column)
        self.table_index = table_index

    def fetch_stock_tickers(self):
        df = self.get_data_frame(table_index=self.table_index)
        self.data_frame_to_csv(df=df)
