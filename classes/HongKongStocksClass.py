from classes.StockCollectionClass import StockCollection
import pandas as pd

class HongKongStocksClass(StockCollection):
    """A class representing the Hong Kong stocks collection."""

    def __init__(
        self,
        name,
        country,
        source,
        tableIndexRange,
        column,
        stockTickerSignature
    ):  
        # :param tableIndex: The index of the stock data table.
        # :param stockTickerSignature: The Stock ticker ending required by yfinance 
        self.set_attributes(name, country, source, column)
        self.tableIndexRange = tableIndexRange
        self.stockTickerSignature = stockTickerSignature

    def getDataFrame(
        self,
        source,
        tableIndexRange
    ):
        tables = pd.read_html(source)
        firstTableIndex = tableIndexRange[0]
        lastTableIndex = tableIndexRange[-1]

        df = pd.DataFrame()
        for tableIndex in range(firstTableIndex, lastTableIndex):
            df = pd.concat([df, tables[tableIndex]], axis=0)
        return df

    def convertDataFrameToCsv(self):
        df = self.getDataFrame(
            source=self.source,
            tableIndexRange=self.tableIndexRange
        )
        self.dataFrameToCsv(
            df=self.modifyTickers(df),
            fileName=self.csvSymbols,
            column=self.column
        )

    def modifyTickers(self, df):
        # Limit posibility of getting digit in company name
        df[0] = df[0].str[:10]
        df[0] = df[0].str.replace(r'(\D+)', '', regex=True)
        return df[0].str.zfill(4) + self.stockTickerSignature
