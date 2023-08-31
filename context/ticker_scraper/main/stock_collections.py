from .classes.french_stocks import FrenchStocksClass
from .classes.german_stocks import GermanStocksClass
from .classes.hong_kong_stocks import HongKongStocksClass
from .classes.norwegian_stocks import NorwegianStocksClass
from .classes.united_kingdom_stocks import UnitedKingdomStocksClass
from .classes.s_and_p500_stocks import StandardAndPoor500StocksClass
from .classes.dutch_stocks import DutchStocksClass
from .const import WIKIPEDIA_BASE_URL, TOP_FOREIGN_STOCKS_BASE_URL

STANDARD_AND_POOR_500 = StandardAndPoor500StocksClass(
    stock_index_name='S&P500',
    source=WIKIPEDIA_BASE_URL + '/List_of_S%26P_500_companies',
    table_index=0,
    column='Symbol'
)
NORWAY = NorwegianStocksClass(
    stock_index_name='OBEX',
    source=WIKIPEDIA_BASE_URL + '/List_of_companies_listed_on_the_Oslo_Stock_Exchange',
    table_index=1,
    column='Ticker',
    stock_ticker_suffixes=['.OL']
)
GERMANY = GermanStocksClass(
    stock_index_name='DAX',
    source=WIKIPEDIA_BASE_URL + '/DAX',
    table_index=4,
    column='Ticker'
)
HONG_KONG = HongKongStocksClass(
    stock_index_name='HKSE',
    source=WIKIPEDIA_BASE_URL + '/List_of_companies_listed_on_the_Hong_Kong_Stock_Exchange',
    table_index_range=[1, 27],
    column=0,
    stock_ticker_suffixes=['.HK']
)
UNITED_KINGDOM = UnitedKingdomStocksClass(
    stock_index_name="FTSE350",
    source='https://www.fidelity.co.uk/shares/ftse-350/',
    table_index=0,
    column='EPIC',
    stock_ticker_suffixes=['.L', '.IL']
)
NETHERLANDS = DutchStocksClass(
    stock_index_name="AEX",
    source=TOP_FOREIGN_STOCKS_BASE_URL + '/the-complete-list-of-listed-companies-in-the-netherlands/',
    table_index=0,
    column='Ticker',
    stock_ticker_suffixes=['.AS']
)
FRANCE = FrenchStocksClass(
    stock_index_name="PEX",
    source=TOP_FOREIGN_STOCKS_BASE_URL + '/the-complete-list-of-listed-companies-in-france/',
    table_index=0,
    column='Ticker',
    stock_ticker_suffixes=['.PA', '.NX']
)
