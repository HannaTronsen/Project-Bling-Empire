from enum import Enum

from yahooquery import Ticker

from ..data_classes.financial_data import FinancialData, PriceToEarnings, EarningsPerShare
from ..data_classes.financial_summary import FinancialSummary
from ..data_classes.general_stock_info import GeneralStockInfo
from ..utils.dict_key_enum import DictKey


# Enum for csv section headers
class Section(Enum):
    GENERAL_STOCK_INFO = "GENERAL STOCK INFO"
    REVENUE_DATA = "REVENUE DATA"
    EARNINGS_DATA = "EARNINGS DATA"
    DEBT_DATA = "DEBT DATA"
    MARGINS_DATA = "MARGINS DATA"
    DIVIDEND_DATA = "DIVIDEND DATA"
    FINANCIAL_RATIO_DATA = "FINANCIAL RATIO DATA"
    CASH_FLOW_DATA = "CASH FLOW DATA"
    PROFITABILITY_DATA = "PROFITABILITY DATA"


class GlobalStockDataClass:

    def __init__(self, ticker_symbol: str):
        # self.earnings_and_earnings_history: HistoricalEarningsData = earnings_and_earnings_history

        YQTicker = Ticker(ticker_symbol)
        financial_data = YQTicker.financial_data[ticker_symbol]
        asset_profile = YQTicker.asset_profile[ticker_symbol]
        summary_detail = YQTicker.summary_detail[ticker_symbol]
        key_stats = YQTicker.key_stats[ticker_symbol]

        self.general_stock_info: GeneralStockInfo = GeneralStockInfo(
            ticker=ticker_symbol,
            company=YQTicker.quote_type[ticker_symbol]["longName"],
            country=asset_profile["country"],
            industry=asset_profile["industry"],
            sector=asset_profile["sector"],
            website=asset_profile["website"],
            long_business_summary=asset_profile["longBusinessSummary"],
            financial_summary=FinancialSummary(
                previous_close=summary_detail["previousClose"],
                open=summary_detail["open"],
                dividend_rate=summary_detail["dividendRate"],
                beta=summary_detail["beta"],
                price_to_earnings=PriceToEarnings(
                    trailing_pe=summary_detail["trailingPE"],
                    forward_pe=summary_detail["forwardPE"]
                ),
                market_cap=summary_detail["marketCap"],
                currency=summary_detail["currency"],

            )
        ).normalize_values()

        self.financial_data: FinancialData = FinancialData(
            price=financial_data["currentPrice"],
            total_revenue=financial_data["totalRevenue"],
            revenue_per_share=financial_data["revenuePerShare"],
            revenue_growth=financial_data["revenueGrowth"],
            total_debt=financial_data["totalDebt"],
            debt_to_equity=financial_data["debtToEquity"],
            gross_profit_margins=financial_data["grossMargins"],
            operating_margins=financial_data["operatingMargins"],
            profit_margins=financial_data["profitMargins"],
            free_cash_flow=financial_data["freeCashflow"],
            operating_cash_flow=financial_data["operatingCashflow"],
            return_on_equity=financial_data["returnOnEquity"],
            return_on_assets=financial_data["returnOnAssets"],
            earnings_growth=financial_data["earningsGrowth"],
            dividend_rate=summary_detail["dividendRate"],
            dividend_yield=summary_detail["dividendYield"],
            five_year_avg_dividend_yield=summary_detail["fiveYearAvgDividendYield"],
            trailing_annual_dividend_rate=summary_detail["trailingAnnualDividendRate"],
            trailing_annual_dividend_yield=summary_detail["trailingAnnualDividendYield"],
            price_to_earnings=PriceToEarnings(
                trailing_pe=summary_detail["trailingPE"],
                forward_pe=summary_detail["forwardPE"]
            ),
            earnings_per_share=EarningsPerShare(
                trailing_eps=key_stats["trailingEps"],
                forward_eps=key_stats["forwardEps"]
            ),
            net_income_to_common=key_stats["netIncomeToCommon"],  # net earnings
            book_value=key_stats["bookValue"],
            enterprise_to_ebitda=key_stats["enterpriseToEbitda"],
            enterprise_to_revenue=key_stats["enterpriseToRevenue"],
            price_to_book=key_stats["priceToBook"],
            expenses=None  # TODO (Hanna): These values come from dataframes
        ).normalize_values()

    def get_revenue_data(self):
        return {
            DictKey.TOTAL_REVENUE: self.financial_data.total_revenue,
            DictKey.REVENUE_PER_SHARE: self.financial_data.revenue_per_share,
            DictKey.REVENUE_GROWTH: self.financial_data.revenue_growth
        }

    def get_earnings_data(self):
        return {
            DictKey.EARNINGS_PER_SHARE: self.financial_data.earnings_per_share,
            DictKey.NET_EARNINGS: self.financial_data.net_income_to_common,
            DictKey.EARNINGS_GROWTH: self.financial_data.earnings_growth
        }

    def get_debt_data(self):
        return {
            DictKey.TOTAL_DEBT: self.financial_data.total_debt,
            DictKey.DEBT_TO_EQUITY: self.financial_data.debt_to_equity
        }

    def get_margins_data(self):
        return {
            DictKey.PROFIT_MARGINS: self.financial_data.profit_margins,
            DictKey.GROSS_PROFIT_MARGINS: self.financial_data.gross_profit_margins,
            DictKey.OPERATING_MARGINS: self.financial_data.operating_margins
        }

    def get_dividend_data(self):
        return {
            DictKey.DIVIDEND_RATE: self.financial_data.dividend_rate,
            DictKey.DIVIDEND_YIELD: self.financial_data.dividend_yield,
            DictKey.FIVE_YEAR_AVG_DIVIDEND_YIELD: self.financial_data.five_year_avg_dividend_yield,
            DictKey.TRAILING_ANNUAL_DIVIDEND_RATE: self.financial_data.trailing_annual_dividend_rate,
            DictKey.TRAILING_ANNUAL_DIVIDEND_YIELD: self.financial_data.trailing_annual_dividend_yield,
        }

    def get_financial_ratio_data(self):
        return {
            DictKey.DEBT_TO_EQUITY: self.financial_data.debt_to_equity,
            DictKey.PRICE_TO_CASH_FLOW: self.financial_data.calculate_price_to_cashflow(),
            DictKey.ENTERPRISE_TO_EBITDA: self.financial_data.enterprise_to_ebitda,
            DictKey.PRICE_TO_BOOK: self.financial_data.price_to_book,
            DictKey.PRICE_TO_EARNINGS: self.financial_data.price_to_earnings,
            DictKey.EARNINGS_PER_SHARE: self.financial_data.earnings_per_share,
            DictKey.ENTERPRISE_TO_REVENUE: self.financial_data.enterprise_to_revenue
        }

    def get_cash_flow_data(self):
        return {
            DictKey.FREE_CASH_FLOW: self.financial_data.free_cash_flow,
            DictKey.OPERATING_CASH_FLOW: self.financial_data.operating_cash_flow,
        }

    def get_profitability_data(self):
        return {
            DictKey.RETURN_ON_EQUITY: self.financial_data.return_on_equity,
            DictKey.RETURN_ON_ASSETS: self.financial_data.return_on_assets,
            DictKey.RETURN_ON_INVESTED_CAPITAL: self.financial_data.calculate_return_on_invested_capital(),
            DictKey.RETURN_ON_INVESTMENT: self.financial_data.calculate_return_on_investment()
        }

    def map_section_headers_with_data(self):
        return {
            Section.REVENUE_DATA: lambda: self.get_revenue_data(),
            Section.EARNINGS_DATA: lambda: self.get_earnings_data(),
            Section.DEBT_DATA: lambda: self.get_debt_data(),
            Section.MARGINS_DATA: lambda: self.get_margins_data(),
            Section.DIVIDEND_DATA: lambda: self.get_dividend_data(),
            Section.FINANCIAL_RATIO_DATA: lambda: self.get_financial_ratio_data(),
            Section.CASH_FLOW_DATA: lambda: self.get_cash_flow_data(),
            Section.PROFITABILITY_DATA: lambda: self.get_profitability_data(),
        }
