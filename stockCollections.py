from classes.DutchStocksClass import DutchStocksClass
from classes.FrenchStocksClass import FrenchStocksClass
from classes.GermanStocksClass import GermanStocksClass
from classes.HongKongStocksClass import HongKongStocksClass
from classes.NorwegianStocksClass import NorwegianStocksClass
from classes.UnitedKingdomStocksClass import UnitedKingdomStocksClass
from classes.StandardAndPoor500StocksClass import StandardAndPoor500StocksClass

STANDARD_AND_POOR_500 = StandardAndPoor500StocksClass(
    name='S&P500',
    country='US',
    source='https://en.wikipedia.org/wiki/List_of_S%26P_500_companies',
    tableIndex=0,
    column='Symbol'
)
NORWAY = NorwegianStocksClass(
    name='OBEX',
    country='NO',
    source='https://en.wikipedia.org/wiki/List_of_companies_listed_on_the_Oslo_Stock_Exchange',
    tableIndex=1,
    column='Ticker',
    stockTickerSuffixes=['.OL']
)
GERMANY = GermanStocksClass(
    name='DAX',
    country='GE',
    source='https://en.wikipedia.org/wiki/DAX',
    tableIndex=4,
    column='Ticker'
)
HONG_KONG = HongKongStocksClass(
    name='HKSE',
    country='HK',
    source='https://en.wikipedia.org/wiki/List_of_companies_listed_on_the_Hong_Kong_Stock_Exchange',
    tableIndexRange=[1, 27],
    column=0,
    stockTickerSuffixes=['.HK']
)
UNITED_KINGDOM = UnitedKingdomStocksClass(
    name="FTSE350",
    country='UK',
    source='https://www.fidelity.co.uk/shares/ftse-350/',
    tableIndex=0,
    column='EPIC',
    stockTickerSuffixes=['.L', '.IL']
)
NETHERLAND = DutchStocksClass(
    name="AEX",
    country='NE',
    source='https://topforeignstocks.com/listed-companies-lists/the-complete-list-of-listed-companies-in-the-netherlands/',
    tableIndex=0,
    column='Ticker',
    stockTickerSuffixes=['.AS']
)
FRANCE = FrenchStocksClass(
    name="PEX",
    country='FR',
    source='https://topforeignstocks.com/listed-companies-lists/the-complete-list-of-listed-companies-in-france/',
    tableIndex=0,
    column='Ticker',
    stockTickerSuffixes=['.PA', '.NX']
)

stockCollectionsList = [
    STANDARD_AND_POOR_500,
    NORWAY,
    GERMANY,
    HONG_KONG,
    UNITED_KINGDOM,
    NETHERLAND,
    FRANCE
]