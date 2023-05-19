import unittest
from context.yquery_ticker.main.classes.universal_stock_data import UniversalStockDataClass
from context.yquery_ticker.main.data_classes.financial_data import EarningsPerShare, FinancialData, PriceToEarnings
from context.yquery_ticker.main.data_classes.financial_summary import FinancialSummary
from context.yquery_ticker.main.data_classes.general_stock_info import GeneralStockInfo
from context.yquery_ticker.main.enums.cash_flow_type import CashFlowType


class test_universal_stock_data(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_universal_stock_data, self).__init__(*args, **kwargs)

    def assert_price_to_cash_flow(
        self,
        stock: FinancialData,
        price: float,
        cash_flow: float,
        expected: float
    ):
        stock.price = price
        stock.set_cash_flow(cash_flow=cash_flow)
        assert stock.calculate_price_to_cashflow() == expected

    def assert_return_on_invested_capital(
        self,
        stock: FinancialData, 
        net_income_to_common: float,
        book_value: float,
        total_debt: float,
        expected: float  
    ) :
        stock.net_income_to_common = net_income_to_common
        stock.book_value = book_value
        stock.total_debt = total_debt
        result = stock.calculate_return_on_invested_capital()
       
        if result is not None:
            assert round(result, 2) == expected
        else: 
            assert result == expected

    def test_general_stock_info(self):
        stock = UniversalStockDataClass(
            general_stock_info=GeneralStockInfo(
                ticker='aapl',
                company_name='Apple Inc',
                country=None,
                industry='Consumer Electronics',
                sector='Technology',
                website='http://www.apple.com',
                long_business_summary='N/A',
                financial_summary=FinancialSummary(
                    previous_close=0.0,
                    open=0.0,
                    dividend_rate=0.0,
                    beta=0.0,
                    trailing_PE=0.0,
                    forward_PE=0.0,
                    market_cap=None,
                    currency=None
                )
            ),
            financial_data=FinancialData.mockk()
        ).general_stock_info

        self.assertIsNone(stock.country)
        self.assertIsNone(stock.long_business_summary)
        self.assertIsNone(stock.financial_summary.market_cap)
        self.assertIsNone(stock.financial_summary.currency)

    def test_financial_data(self):
        stock = UniversalStockDataClass(
            general_stock_info=GeneralStockInfo.mockk(),
            financial_data=FinancialData(
                price=10,
                total_revenue=0.00000,
                revenue_per_share="",
                revenue_growth="N/A",
                total_debt=-1,
                debt_to_equity=0,
                profit_margins=3,
                gross_profit_margins="N/A",
                operating_margins=None,
                dividend_rate=0,
                dividend_yield=0,
                five_year_avg_dividend_yield=0,
                trailing_annual_dividend_rate=0,
                trailing_annual_dividend_yield=0,
                free_cash_flow=0,
                operating_cash_flow=0,
                enterprise_to_ebitda=0,
                price_to_book=0,
                return_on_assets=0,
                return_on_equity=0,
                net_income_to_common=0, 
                book_value=0,
                price_to_earnings=PriceToEarnings(
                    trailing_pe=None,
                    forward_pe=2
                ),
                earnings_per_share=EarningsPerShare(
                    trailing_eps=2,
                    forward_eps=None
                ),
                enterprise_to_revenue=0

            )
        ).financial_data
        self.assertIsNone(stock.revenue_per_share)
        self.assertIsNone(stock.revenue_growth)
        self.assertIsNone(stock.total_debt)
        self.assertIsNone(stock.total_debt)
        self.assertIsNone(stock.gross_profit_margins)
        self.assertIsNone(stock.operating_margins)
        self.assertIsNone(stock.price_to_earnings.trailing_pe)
        self.assertIsNone(stock.earnings_per_share.forward_eps)

    def test_calculate_price_to_cashflow(self):
        stock = UniversalStockDataClass(
            general_stock_info=GeneralStockInfo.mockk(),
            financial_data=FinancialData.mockk()
        ).financial_data

        self.assert_price_to_cash_flow(stock=stock, price=None, cash_flow=10, expected=None)
        self.assert_price_to_cash_flow(stock=stock, price=10, cash_flow=None, expected=None)
        self.assert_price_to_cash_flow(stock=stock, price=100.0, cash_flow=10.0, expected=10.0)
        self.assert_price_to_cash_flow(stock=stock, price=0.0, cash_flow=10.0, expected=0.0)
        self.assert_price_to_cash_flow(stock=stock, price=0.0, cash_flow=0.0, expected=None)
        self.assert_price_to_cash_flow(stock=stock, price=100.0, cash_flow=-10.0, expected=-10)
        self.assert_price_to_cash_flow(stock=stock, price=-100.0, cash_flow=10.0, expected=-10)
        self.assert_price_to_cash_flow(stock=stock, price=-100.0, cash_flow=-10.0, expected=10)
        self.assert_price_to_cash_flow(stock=stock, price=100.0, cash_flow=10.0, expected=10.0)

    def test_get_and_set_cash_flow(self):
        stock = UniversalStockDataClass(
            general_stock_info=GeneralStockInfo.mockk(),
            financial_data=FinancialData.mockk()
        ).financial_data

        stock.free_cash_flow = 10
        cash_flow_type = CashFlowType.OPERATING_CASH_FLOW
        stock.set_cash_flow(cash_flow=100, cash_flow_type=cash_flow_type)
        assert stock.get_cash_flow(cash_flow_type=cash_flow_type) == stock.operating_cash_flow 

        
        stock.operating_cash_flow = 100
        cash_flow_type = CashFlowType.FREE_CASH_FLOW
        stock.set_cash_flow(cash_flow=100, cash_flow_type=CashFlowType.FREE_CASH_FLOW)
        assert stock.get_cash_flow(cash_flow_type=CashFlowType.FREE_CASH_FLOW) == stock.free_cash_flow

    
    def test_calculate_return_on_investments(self):
        stock = UniversalStockDataClass(
            general_stock_info=GeneralStockInfo.mockk(),
            financial_data=FinancialData.mockk()
        ).financial_data

        self.assert_return_on_invested_capital(
            stock=stock, 
            net_income_to_common=1000, 
            book_value=2000,
            total_debt=1000,
            expected=0.33
        )
        self.assert_return_on_invested_capital(
            stock=stock, 
            net_income_to_common=0, 
            book_value=2000,
            total_debt=1000,
            expected=0.0
        )
        self.assert_return_on_invested_capital(
            stock=stock, 
            net_income_to_common=1000, 
            book_value=0,
            total_debt=0,
            expected=None
        )
        self.assert_return_on_invested_capital(
            stock=stock, 
            net_income_to_common=0, 
            book_value=0,
            total_debt=0,
            expected=None
        )
        self.assert_return_on_invested_capital(
            stock=stock, 
            net_income_to_common=None, 
            book_value=None,
            total_debt=None,
            expected=None
        )
        self.assert_return_on_invested_capital(
            stock=stock, 
            net_income_to_common=-1000, 
            book_value=2000,
            total_debt=1000,
            expected=-0.33
        )
        self.assert_return_on_invested_capital(
            stock=stock, 
            net_income_to_common=1000, 
            book_value=2000,
            total_debt=-1000,
            expected=1.00
        ) 