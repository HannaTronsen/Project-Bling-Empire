import os
import pandas as pd

from stockCollectionClass import FRANCE, NETHERLAND, UNITED_KINGDOM, StockCollection
from stockCollectionClass import GERMANY, HONG_KONG, NORWAY, STANDARD_AND_POOR_500

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
                    tableIndexRange=STANDARD_AND_POOR_500.tableIndexRange
                )
                dataFrameToCsv(
                    df=df,
                    fileName=STANDARD_AND_POOR_500.csvSymbols,
                    columns=STANDARD_AND_POOR_500.columns
                )
            case NORWAY.name:
                df = getDataFrame(
                    source=NORWAY.source,
                    tableIndexRange=NORWAY.tableIndexRange
                )
                dataFrameToCsv(
                    df=modifyTickers(NORWAY.name, df),
                    fileName=NORWAY.csvSymbols,
                    columns=NORWAY.columns
                )
            case  GERMANY.name:
                df = getDataFrame(
                    source=GERMANY.source,
                    tableIndexRange=GERMANY.tableIndexRange
                )
                dataFrameToCsv(
                    df=df,
                    fileName=GERMANY.csvSymbols,
                    columns=GERMANY.columns
                )
            case HONG_KONG.name:
                df = getDataFrame(
                    source=HONG_KONG.source,
                    tableIndexRange=HONG_KONG.tableIndexRange
                )
                dataFrameToCsv(
                    df=modifyTickers(HONG_KONG.name, df),
                    fileName=HONG_KONG.csvSymbols,
                    columns=HONG_KONG.columns
                )
            case UNITED_KINGDOM.name:
                df = getDataFrame(
                    source=UNITED_KINGDOM.source,
                    tableIndexRange=UNITED_KINGDOM.tableIndexRange
                )
                dataFrameToCsv(
                    df=df,
                    fileName=UNITED_KINGDOM.csvSymbols,
                    columns=UNITED_KINGDOM.columns
                )
            case NETHERLAND.name:
                df = getDataFrame(
                    source=NETHERLAND.source,
                    tableIndexRange=NETHERLAND.tableIndexRange
                )
                dataFrameToCsv(
                    df=modifyTickers(NETHERLAND.name, df),
                    fileName=NETHERLAND.csvSymbols,
                    columns=NETHERLAND.columns
                )
            
            case FRANCE.name:
                df = getDataFrame(
                    source=FRANCE.source,
                    tableIndexRange=FRANCE.tableIndexRange
                )
                dataFrameToCsv(
                    df=modifyTickers(FRANCE.name, df),
                    fileName=FRANCE.csvSymbols,
                    columns=FRANCE.columns
                )


def getDataFrame(
    source,
    tableIndexRange
):
    tables = pd.read_html(source)

    firstTableIndex = tableIndexRange[0]
    lastTableIndex = tableIndexRange[-1]

    if (firstTableIndex != lastTableIndex):
        df = pd.DataFrame()
        for tableIndex in range(firstTableIndex, lastTableIndex):
            df = pd.concat([df, tables[tableIndex]], axis=0)
        return df
    return tables[firstTableIndex]


def dataFrameToCsv(
    df,
    fileName,
    columns,
    header=False,
    index=False
):
    df.to_csv(
        TICKERS_PATH+fileName,
        columns=columns,
        header=header,
        index=index
    )


def modifyTickers(
    stockCollectionName,
    df
):
    match stockCollectionName:
        case NORWAY.name:
            return df['Ticker'].str.replace('OSE: ', '') + '.OL'

        case HONG_KONG.name:
            # Limit posibility of getting digit in company name
            df[0] = df[0].str[:10]
            df[0] = df[0].str.replace(r'(\D+)', '', regex=True)
            return df[0].str.zfill(4) + '.HK'

        case NETHERLAND.name:
            return df['Ticker'] +'.AS'

        case FRANCE.name:
            return df['Ticker'] +'.PA'
