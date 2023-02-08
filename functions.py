from classes.StockCollectionClass import StockCollection
from const import TICKERS_PATH
import os

from stockCollections import FRANCE, GERMANY, HONG_KONG, NETHERLAND, NORWAY, STANDARD_AND_POOR_500, UNITED_KINGDOM

def initializeEnvironment():

    if not os.path.exists(TICKERS_PATH):
        os.makedirs(TICKERS_PATH)


def fetch_tickers(stockCollection: list[StockCollection]):
    for collection in stockCollection:
        match collection.name:
            case STANDARD_AND_POOR_500.name:
                STANDARD_AND_POOR_500.convertDataFrameToCsv()
            case NORWAY.name:
                NORWAY.convertDataFrameToCsv()
            case  GERMANY.name:
                GERMANY.convertDataFrameToCsv()
            case HONG_KONG.name:
                HONG_KONG.convertDataFrameToCsv()
            case UNITED_KINGDOM.name:
                UNITED_KINGDOM.convertDataFrameToCsv()
            case NETHERLAND.name:
                NETHERLAND.convertDataFrameToCsv()
            case FRANCE.name:
                FRANCE.convertDataFrameToCsv()