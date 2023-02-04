
class StockCollection():

    def __init__(self, name, country, source):
        self.name = name
        self.country = country
        self.source = source
        self.csvInfo = self.name + '-info.csv'
        self.csvSymbols = self.name + '-symbols.csv'

    def __str__(self):
        return self.collection

# constants
STANDARD_AND_POOR_500 = StockCollection(
    name='S&P500',
    country='US',
    source='https://en.wikipedia.org/wiki/List_of_S%26P_500_companies',
    
)

NORWAY = StockCollection(
    name='OBEX',
    country='NO',
    source='https://en.wikipedia.org/wiki/List_of_companies_listed_on_the_Oslo_Stock_Exchange',
)