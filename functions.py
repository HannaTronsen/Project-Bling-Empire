import os
import pandas as pd

from stockCollectionClass import StockCollection
from stockCollectionClass import STANDARD_AND_POOR_500
from stockCollectionClass import NORWAY

# Const
TICKERS_PATH = 'tickers/'


def initializeEnvironment():

    if not os.path.exists(TICKERS_PATH):
        os.makedirs(TICKERS_PATH)


def fetch_tickers(stockCollection: list[StockCollection]):

    for collection in stockCollection:
        match collection.name:
            case STANDARD_AND_POOR_500.name:
                df = getDataFrame(
                    source=STANDARD_AND_POOR_500.source,
                    tableIndex=0
                )

                dataFrameToCsv(
                    df=df,
                    fileName=STANDARD_AND_POOR_500.csvSymbols,
                    columns=['Symbol']
                )

            case NORWAY.name:
                df = getDataFrame(
                    source=NORWAY.source,
                    tableIndex=1
                )

                # The format that yfinance accepts for norwegian stocks
                df['Ticker'] = df['Ticker'].str.replace('OSE: ', '') + '.OL'

                dataFrameToCsv(
                    df=df,
                    fileName=NORWAY.csvSymbols,
                    columns=['Ticker']
                )


def getDataFrame(source, tableIndex):
    table = pd.read_html(source)
    df = table[tableIndex]
    return df


def dataFrameToCsv(df, fileName, columns, header=False, index=False):
    df.to_csv(TICKERS_PATH+fileName, columns=columns,
              header=header, index=index)
