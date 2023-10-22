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


class GlobalStockDataClass:

    def __init__(self, ticker_symbol: str, ticker: Optional[Ticker] = None):
        YQTicker = ticker if ticker is not None else Ticker(ticker_symbol)
        financial_data = YQTicker.financial_data.get(ticker_symbol)
        asset_profile = YQTicker.asset_profile.get(ticker_symbol)
        summary_detail = YQTicker.summary_detail.get(ticker_symbol)
        key_stats = YQTicker.key_stats.get(ticker_symbol)

        self.general_stock_info: GeneralStockInfo = GeneralStockInfo(
            ticker=ticker_symbol,
            company=YQTicker.quote_type.get(ticker_symbol).get("longName"),
            country=asset_profile.get("country"),
            industry=asset_profile.get("industry"),
            sector=asset_profile.get("sector"),
            website=asset_profile.get("website"),
            long_business_summary=asset_profile.get("longBusinessSummary"),
            financial_summary=FinancialSummary(
                previous_close=summary_detail.get("previousClose"),
                open=summary_detail.get("open"),
                dividend_rate=summary_detail.get("dividendRate"),
                beta=summary_detail.get("beta"),
                price_to_earnings=PriceToEarnings(
                    trailing_pe=summary_detail.get("trailingPE"),
                    forward_pe=summary_detail.get("forwardPE")
                ),
                market_cap=summary_detail.get("marketCap"),
                currency=summary_detail.get("currency"),
            )
        ).normalize_values()

        self.financial_data: FinancialData = FinancialData(
            price=financial_data.get("currentPrice"),
            total_revenue=financial_data.get("totalRevenue"),
            revenue_per_share=financial_data.get("revenuePerShare"),
            revenue_growth=financial_data.get("revenueGrowth"),
            total_debt=financial_data.get("totalDebt"),
            debt_to_equity=financial_data.get("debtToEquity"),
            gross_profit_margins=financial_data.get("grossMargins"),
            operating_margins=financial_data.get("operatingMargins"),
            profit_margins=financial_data.get("profitMargins"),
            free_cash_flow=financial_data.get("freeCashflow"),
            operating_cash_flow=financial_data.get("operatingCashflow"),
            return_on_equity=financial_data.get("returnOnEquity"),
            return_on_assets=financial_data.get("returnOnAssets"),
            earnings_growth=financial_data.get("earningsGrowth"),
            dividend_rate=summary_detail.get("dividendRate"),
            dividend_yield=summary_detail.get("dividendYield"),
            five_year_avg_dividend_yield=summary_detail.get("fiveYearAvgDividendYield"),
            trailing_annual_dividend_rate=summary_detail.get("trailingAnnualDividendRate"),
            trailing_annual_dividend_yield=summary_detail.get("trailingAnnualDividendYield"),
            price_to_earnings=PriceToEarnings(
                trailing_pe=summary_detail.get("trailingPE"),
                forward_pe=summary_detail.get("forwardPE")
            ),
            earnings_per_share=EarningsPerShare(
                trailing_eps=key_stats.get("trailingEps"),
                forward_eps=key_stats.get("forwardEps")
            ),
            net_income_to_common=key_stats.get("netIncomeToCommon"),
            # net earnings
            book_value=key_stats.get("bookValue"),
            enterprise_to_ebitda=key_stats.get("enterpriseToEbitda"),
            enterprise_to_revenue=key_stats.get("enterpriseToRevenue"),
            price_to_book=key_stats.get("priceToBook"),
            expenses=None  # TODO (Hanna): These values come from dataframes
        ).normalize_values()

        self.earnings_and_earnings_history = HistoricalEarningsData.convert_json_to_time_series_model(
            ticker_symbol=ticker_symbol,
            data=YQTicker.earnings,
            model=YearlyFinancialsDataChart
        )

        self.income_statement = IncomeStatementData(
            entries=IncomeStatementData.convert_data_frame_to_time_series_model(
                data_frame=YQTicker.income_statement(frequency=Frequency.ANNUALLY.value, trailing=True)
            )
        )

        self.balance_sheet = BalanceSheetData.convert_data_frame_to_time_series_model(
            data_frame=YQTicker.balance_sheet(frequency=Frequency.ANNUALLY.value, trailing=True)
        )

        self.cash_flow = CashFlowData(
            entries=CashFlowData.convert_data_frame_to_time_series_model(
                data_frame=YQTicker.cash_flow(frequency=Frequency.ANNUALLY.value, trailing=True)
            )
        )

        self._evaluated_growth_criteria = self.get_evaluated_growth_criteria()
        self.criteria_pass_count = sum(1 for value in self._evaluated_growth_criteria.values() if value is True)

    def _get_revenue_data(self):
        return {
            DictKey.TOTAL_REVENUE: self.financial_data.total_revenue,
            DictKey.REVENUE_PER_SHARE: self.financial_data.revenue_per_share,
            DictKey.REVENUE_GROWTH: self.financial_data.revenue_growth
        }

    def _get_earnings_data(self):
        return {
            DictKey.EARNINGS_PER_SHARE: self.financial_data.earnings_per_share,
            DictKey.NET_EARNINGS: self.financial_data.net_income_to_common,
            DictKey.EARNINGS_GROWTH: self.financial_data.earnings_growth
        }

    def _get_debt_data(self):
        return {
            DictKey.TOTAL_DEBT: self.financial_data.total_debt,
            DictKey.DEBT_TO_EQUITY: self.financial_data.debt_to_equity
        }

    def _get_margins_data(self):
        return {
            DictKey.PROFIT_MARGINS: self.financial_data.profit_margins,
            DictKey.GROSS_PROFIT_MARGINS: self.financial_data.gross_profit_margins,
            DictKey.OPERATING_MARGINS: self.financial_data.operating_margins
        }

    def _get_dividend_data(self):
        return {
            DictKey.DIVIDEND_RATE: self.financial_data.dividend_rate,
            DictKey.DIVIDEND_YIELD: self.financial_data.dividend_yield,
            DictKey.FIVE_YEAR_AVG_DIVIDEND_YIELD: self.financial_data.five_year_avg_dividend_yield,
            DictKey.TRAILING_ANNUAL_DIVIDEND_RATE: self.financial_data.trailing_annual_dividend_rate,
            DictKey.TRAILING_ANNUAL_DIVIDEND_YIELD: self.financial_data.trailing_annual_dividend_yield,
        }

    def _get_financial_ratio_data(self):
        return {
            DictKey.DEBT_TO_EQUITY: self.financial_data.debt_to_equity,
            DictKey.PRICE_TO_CASH_FLOW: self.financial_data.calculate_price_to_cashflow(),
            DictKey.ENTERPRISE_TO_EBITDA: self.financial_data.enterprise_to_ebitda,
            DictKey.PRICE_TO_BOOK: self.financial_data.price_to_book,
            DictKey.PRICE_TO_EARNINGS: self.financial_data.price_to_earnings,
            DictKey.EARNINGS_PER_SHARE: self.financial_data.earnings_per_share,
            DictKey.ENTERPRISE_TO_REVENUE: self.financial_data.enterprise_to_revenue
        }

    def _get_cash_flow_data(self):
        return {
            DictKey.FREE_CASH_FLOW: self.financial_data.free_cash_flow,
            DictKey.OPERATING_CASH_FLOW: self.financial_data.operating_cash_flow,
        }

    def _get_profitability_data(self):
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
                income_statement=self.income_statement,
                attribute=DictKey.NET_INCOME
            ),
            DictKey.SALES: IncomeStatementData.evaluate_growth_criteria(
                income_statement=self.income_statement,
                attribute=DictKey.SALES
            ),
            DictKey.OPERATING_CASH_FLOW: self.cash_flow.evaluate_growth_criteria(
                attribute=DictKey.OPERATING_CASH_FLOW
            ),
            DictKey.FREE_CASH_FLOW: self.cash_flow.evaluate_growth_criteria(
                attribute=DictKey.FREE_CASH_FLOW
            ),
            DictKey.BOOK_VALUE_AND_DIVIDENDS: CombinableYQData(
                combination=DictKey.BOOK_VALUE_AND_DIVIDENDS,
                balance_sheet=self.balance_sheet,
                cash_flow=self.cash_flow,
            ).combine_process_and_evaluate_growth_criteria(),
            DictKey.ROIC: CombinableYQData(
                combination=DictKey.ROIC,
                balance_sheet=self.balance_sheet,
                income_statement=self.income_statement,
            ).combine_process_and_evaluate_growth_criteria(),
        }

    def map_section_headers_with_data(self):
        return {
            Section.REVENUE: lambda: self._get_revenue_data(),
            Section.EARNINGS: lambda: self._get_earnings_data(),
            Section.DEBT: lambda: self._get_debt_data(),
            Section.MARGINS: lambda: self._get_margins_data(),
            Section.DIVIDEND: lambda: self._get_dividend_data(),
            Section.FINANCIAL_RATIO: lambda: self._get_financial_ratio_data(),
            Section.CASH_FLOW: lambda: self._get_cash_flow_data(),
            Section.PROFITABILITY: lambda: self._get_profitability_data(),
            Section.GROWTH_CRITERIA: lambda: self._evaluated_growth_criteria
        }
