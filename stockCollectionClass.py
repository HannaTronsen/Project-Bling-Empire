#https://stockmarketmba.com/listofstocksforanexchange.php -> Stock tickers from different stock exchanges

class StockCollection():

    def __init__(self, name, country, source, tableIndexRange, columns):
        self.name = name
        self.country = country
        self.source = source
        self.csvInfo = self.name + '-info.csv'
        self.csvSymbols = self.name + '-symbols.csv'
        self.tableIndexRange = tableIndexRange
        self.columns = columns

    def __str__(self):
        return self.collection

# constants
STANDARD_AND_POOR_500 = StockCollection(
    name='S&P500',
    country='US',
    source='https://en.wikipedia.org/wiki/List_of_S%26P_500_companies',
    tableIndexRange = [0,0],
    columns= ['Symbol']
    
)

NORWAY = StockCollection(
    name='OBEX',
    country='NO',
    source='https://en.wikipedia.org/wiki/List_of_companies_listed_on_the_Oslo_Stock_Exchange',
    tableIndexRange=[1,1],
    columns=['Ticker']
)

GERMANY = StockCollection(
    name='DAX',
    country='GE',
    source='https://en.wikipedia.org/wiki/DAX',
    tableIndexRange=[4,4],
    columns=['Ticker']
)

HONG_KONG = StockCollection(
    name='HKSE',
    country='HK',
    source='https://en.wikipedia.org/wiki/List_of_companies_listed_on_the_Hong_Kong_Stock_Exchange',
    tableIndexRange=[1,27],
    columns=[0]
)