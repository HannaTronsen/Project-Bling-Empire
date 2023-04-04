from classes.french_stocks_class import french_stocks_class
from classes.german_stocks_class import german_stocks_class
from classes.hong_kong_stocks_class import hong_kong_stocks_class
from classes.norwegian_stocks_class import norwegian_stocks_class
from classes.united_kingdom_stocks_class import united_kingdom_stocks_class
from classes.s_and_p500_stocks_class import standard_and_poor500_stocks_class
from classes.dutch_stocks_class import dutch_stocks_class

STANDARD_AND_POOR_500 = standard_and_poor500_stocks_class(
    name='S&P500',
    country='US',
    source='https://en.wikipedia.org/wiki/List_of_S%26P_500_companies',
    tableIndex=0,
    column='Symbol'
)
NORWAY = norwegian_stocks_class(
    name='OBEX',
    country='NO',
    source='https://en.wikipedia.org/wiki/List_of_companies_listed_on_the_Oslo_Stock_Exchange',
    tableIndex=1,
    column='Ticker',
    stockTickerSuffixes=['.OL'])
GERMANY = german_stocks_class(
    name='DAX',
    country='GE',
    source='https://en.wikipedia.org/wiki/DAX',
    tableIndex=4,
    column='Ticker'
)
HONG_KONG = hong_kong_stocks_class(
    name='HKSE',
    country='HK',
    source='https://en.wikipedia.org/wiki/List_of_companies_listed_on_the_Hong_Kong_Stock_Exchange',
    tableIndexRange=[
        1,
        27],
    column=0,
    stockTickerSuffixes=['.HK'])
UNITED_KINGDOM = united_kingdom_stocks_class(
    name="FTSE350",
    country='UK',
    source='https://www.fidelity.co.uk/shares/ftse-350/',
    tableIndex=0,
    column='EPIC',
    stockTickerSuffixes=['.L', '.IL']
)
NETHERLAND = dutch_stocks_class(
    name="AEX",
    country='NE',
    source='https://topforeignstocks.com/listed-companies-lists/the-complete-list-of-listed-companies-in-the-netherlands/',
    tableIndex=0,
    column='Ticker',
    stockTickerSuffixes=['.AS'])
FRANCE = french_stocks_class(
    name="PEX",
    country='FR',
    source='https://topforeignstocks.com/listed-companies-lists/the-complete-list-of-listed-companies-in-france/',
    tableIndex=0,
    column='Ticker',
    stockTickerSuffixes=[
        '.PA',
         '.NX'])

stock_collection_classsList = [
    STANDARD_AND_POOR_500,
    NORWAY,
    GERMANY,
    HONG_KONG,
    UNITED_KINGDOM,
    NETHERLAND,
    FRANCE
]
