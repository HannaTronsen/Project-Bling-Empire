from enum import Enum
from typing import Optional

from yahooquery import Ticker
from context.yquery_ticker.main.classes.yahoo.balance_sheet_data import BalanceSheetData
from context.yquery_ticker.main.classes.yahoo.cash_flow_data import CashFlowData
from context.yquery_ticker.main.classes.yahoo.historical_earnings_data import HistoricalEarningsData
from context.yquery_ticker.main.classes.yahoo.income_statement_data import IncomeStatementData
from .combinable_yq_data import CombinableYQData
from ..data_classes.charts import YearlyFinancialsDataChart
from ..data_classes.date import Frequency
from ..data_classes.financial_data import FinancialData, PriceToEarnings, EarningsPerShare
from ..data_classes.financial_summary import FinancialSummary
from ..data_classes.general_stock_info import GeneralStockInfo
from ..utils.dict_key_enum import DictKey


# Enum for csv section headers
class Section(Enum):
    GENERAL_STOCK_INFO = "GENERAL STOCK INFO"
    REVENUE = "REVENUE"
    EARNINGS = "EARNINGS"
    DEBT = "DEBT"
    MARGINS = "MARGINS"
    DIVIDEND = "DIVIDEND"
    FINANCIAL_RATIO = "FINANCIAL RATIO"
    CASH_FLOW = "CASH FLOW"
    PROFITABILITY = "PROFITABILITY"
    GROWTH_CRITERIA = "PASSES GROWTH CRITERIA"


def get_asset_profile_or_null(ticker_symbol: str, ticker: Ticker) -> Optional[dict]:
    try:
        return ticker.asset_profile[ticker_symbol]
    except Exception as e:
        print(f"An error occurred when fetching asset_profile for ticker {ticker_symbol}- {e}")
        return None


def get_key_stats_or_null(ticker_symbol: str, ticker: Ticker) -> Optional[dict]:
    try:
        return ticker.key_stats[ticker_symbol]
    except Exception as e:
        print(f"An error occurred when fetching key_stats for ticker {ticker_symbol}- {e}")
        return None


class GlobalStockDataClass:

    def __init__(self, ticker_symbol: str, ticker: Optional[Ticker] = None):
        YQTicker = ticker if ticker is not None else Ticker(ticker_symbol)
        financial_data = YQTicker.financial_data[ticker_symbol]
        asset_profile = get_asset_profile_or_null(ticker_symbol=ticker_symbol, ticker=ticker)
        summary_detail = YQTicker.summary_detail[ticker_symbol]
        key_stats = get_key_stats_or_null(ticker_symbol=ticker_symbol, ticker=ticker)

        self.general_stock_info: GeneralStockInfo = GeneralStockInfo(
            ticker=ticker_symbol,
            company=YQTicker.quote_type[ticker_symbol]["longName"],
            country=asset_profile["country"] if asset_profile is not None else "asset_profile missing",
            industry=asset_profile["industry"] if asset_profile is not None else "asset_profile missing",
            sector=asset_profile["sector"] if asset_profile is not None else "asset_profile missing",
            website=asset_profile["website"] if asset_profile is not None else "asset_profile missing",
            long_business_summary=asset_profile[
                "longBusinessSummary"] if asset_profile is not None else "asset_profile missing",
            financial_summary=None
            # financial_summary=FinancialSummary(
            #     previous_close=summary_detail["previousClose"],
            #     open=summary_detail["open"],
            #     dividend_rate=summary_detail["dividendRate"],
            #     beta=summary_detail["beta"],
            #     price_to_earnings=PriceToEarnings(
            #         trailing_pe=summary_detail["trailingPE"],
            #         forward_pe=summary_detail["forwardPE"]
            #     ),
            #     market_cap=summary_detail["marketCap"],
            #     currency=summary_detail["currency"],
            #
            # )
        )  # .normalize_values() TODO(Hanna): Fix for multi word strings

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
            price_to_earnings=None,
            # price_to_earnings=PriceToEarnings(
            #     trailing_pe=summary_detail["trailingPE"],
            #     forward_pe=summary_detail["forwardPE"]
            # ),
            earnings_per_share=EarningsPerShare(
                trailing_eps=key_stats["trailingEps"] if key_stats is not None else "key_stats is missing",
                forward_eps=key_stats["forwardEps"] if key_stats is not None else "key_stats is missing"
            ),
            net_income_to_common=key_stats["netIncomeToCommon"] if key_stats is not None else "key_stats is missing", # net earnings
            book_value=key_stats["bookValue"] if key_stats is not None else "key_stats is missing",
            enterprise_to_ebitda=key_stats["enterpriseToEbitda"] if key_stats is not None else "key_stats is missing",
            enterprise_to_revenue=key_stats["enterpriseToRevenue"] if key_stats is not None else "key_stats is missing",
            price_to_book=key_stats["priceToBook"] if key_stats is not None else "key_stats is missing",
            expenses=None  # TODO (Hanna): These values come from dataframes
        ).normalize_values()

        # self.earnings_and_earnings_history = HistoricalEarningsData.convert_json_to_time_series_model(
        #     ticker_symbol=ticker_symbol,
        #     data=YQTicker.earnings,
        #     model=YearlyFinancialsDataChart
        # )

        self.income_statement = IncomeStatementData.convert_data_frame_to_time_series_model(
            data_frame=YQTicker.income_statement(frequency=Frequency.ANNUALLY.value, trailing=True)
        )

        self.balance_sheet = BalanceSheetData.convert_data_frame_to_time_series_model(
            data_frame=YQTicker.balance_sheet(frequency=Frequency.ANNUALLY.value, trailing=True)
        )

        # self.cash_flow = CashFlowData(
        #     entries=CashFlowData.convert_data_frame_to_time_series_model(
        #         data_frame=YQTicker.cash_flow(frequency=Frequency.ANNUALLY.value, trailing=True)
        #     )
        # )

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

    def get_evaluated_growth_criteria(self):
        return {
            DictKey.EARNINGS_HISTORY: HistoricalEarningsData.evaluate_growth_criteria(
                chart_list=self.earnings_and_earnings_history,
                attribute=DictKey.EARNINGS_HISTORY
            ),
            DictKey.REVENUE_HISTORY: HistoricalEarningsData.evaluate_growth_criteria(
                chart_list=self.earnings_and_earnings_history,
                attribute=DictKey.REVENUE_HISTORY
            ),
            DictKey.NET_INCOME: IncomeStatementData.evaluate_growth_criteria(
                income_statement=self.income_statement
            ),
            DictKey.BOOK_VALUE_AND_DIVIDENDS: CombinableYQData(
                combination=DictKey.BOOK_VALUE_AND_DIVIDENDS,
                balance_sheet=self.balance_sheet,
                cash_flow=self.cash_flow,
            ).combine_process_and_evaluate_growth_criteria()
        }

    def map_section_headers_with_data(self):
        return {
            Section.REVENUE: lambda: self.get_revenue_data(),
            Section.EARNINGS: lambda: self.get_earnings_data(),
            Section.DEBT: lambda: self.get_debt_data(),
            Section.MARGINS: lambda: self.get_margins_data(),
            Section.DIVIDEND: lambda: self.get_dividend_data(),
            Section.FINANCIAL_RATIO: lambda: self.get_financial_ratio_data(),
            Section.CASH_FLOW: lambda: self.get_cash_flow_data(),
            Section.PROFITABILITY: lambda: self.get_profitability_data(),
            Section.GROWTH_CRITERIA: lambda: self.get_evaluated_growth_criteria()
        }
