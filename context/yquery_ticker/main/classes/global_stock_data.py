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
from ..enums.growth_criteria import GrowthCriteria
from ..utils.csv_converter import CsvConverter
from ..utils.dict_key_enum import DictKey


class GlobalStockDataClass(CsvConverter):

    def __init__(self, ticker_symbol: str, ticker: Optional[Ticker] = None):
        YQTicker = ticker if ticker is not None else Ticker(ticker_symbol)
        financial_data = YQTicker.financial_data.get(ticker_symbol)
        asset_profile = YQTicker.asset_profile.get(ticker_symbol)
        summary_detail = YQTicker.summary_detail.get(ticker_symbol)
        key_stats = YQTicker.key_stats.get(ticker_symbol)

        self.income_statement = IncomeStatementData(
            entries=IncomeStatementData.convert_data_frame_to_time_series_model(
                data_frame=YQTicker.income_statement(frequency=Frequency.ANNUALLY.value, trailing=True)
            )
        )

        self.earnings_and_earnings_history = HistoricalEarningsData.convert_json_to_time_series_model(
            ticker_symbol=ticker_symbol,
            data=YQTicker.earnings,
            model=YearlyFinancialsDataChart
        )

        self.balance_sheet = BalanceSheetData(
            entries=BalanceSheetData.convert_data_frame_to_time_series_model(
                data_frame=YQTicker.balance_sheet(frequency=Frequency.ANNUALLY.value, trailing=True)
            )
        )

        self.cash_flow = CashFlowData(
            entries=CashFlowData.convert_data_frame_to_time_series_model(
                data_frame=YQTicker.cash_flow(frequency=Frequency.ANNUALLY.value, trailing=True)
            )
        )

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
            expenses=self.income_statement.get_most_recent_expenses(
                capital_expenditure=self.cash_flow.get_most_recent_capital_expenditure()
            ).normalize_values(),
        ).normalize_values()

        self._evaluated_growth_criteria = self.get_evaluated_growth_criteria()
        self.criteria_pass_count = sum(1 for value in self._evaluated_growth_criteria.values() if value is True)

    def _get_revenue_data(self):
        return {
            DictKey.TOTAL_REVENUE.__str__: self.financial_data.total_revenue,
            DictKey.REVENUE_PER_SHARE.__str__: self.financial_data.revenue_per_share,
            DictKey.REVENUE_GROWTH.__str__: self.financial_data.revenue_growth
        }

    def _get_earnings_data(self):
        return {
            DictKey.EARNINGS_PER_SHARE.__str__: self.financial_data.earnings_per_share,
            DictKey.NET_EARNINGS.__str__: self.financial_data.net_income_to_common,
            DictKey.EARNINGS_GROWTH.__str__: self.financial_data.earnings_growth
        }

    def _get_debt_data(self):
        return {
            DictKey.TOTAL_DEBT.__str__: self.financial_data.total_debt,
            DictKey.DEBT_TO_EQUITY.__str__: self.financial_data.debt_to_equity
        }

    def _get_margins_data(self):
        return {
            DictKey.PROFIT_MARGINS.__str__: self.financial_data.profit_margins,
            DictKey.GROSS_PROFIT_MARGINS.__str__: self.financial_data.gross_profit_margins,
            DictKey.OPERATING_MARGINS.__str__: self.financial_data.operating_margins
        }

    def _get_dividend_data(self):
        return {
            DictKey.DIVIDEND_RATE.__str__: self.financial_data.dividend_rate,
            DictKey.DIVIDEND_YIELD.__str__: self.financial_data.dividend_yield,
            DictKey.FIVE_YEAR_AVG_DIVIDEND_YIELD.__str__: self.financial_data.five_year_avg_dividend_yield,
            DictKey.TRAILING_ANNUAL_DIVIDEND_RATE.__str__: self.financial_data.trailing_annual_dividend_rate,
            DictKey.TRAILING_ANNUAL_DIVIDEND_YIELD.__str__: self.financial_data.trailing_annual_dividend_yield,
        }

    def _get_financial_ratio_data(self):
        return {
            DictKey.DEBT_TO_EQUITY.__str__: self.financial_data.debt_to_equity,
            DictKey.PRICE_TO_CASH_FLOW.__str__: self.financial_data.calculate_price_to_cashflow(),
            DictKey.ENTERPRISE_TO_EBITDA.__str__: self.financial_data.enterprise_to_ebitda,
            DictKey.PRICE_TO_BOOK.__str__: self.financial_data.price_to_book,
            DictKey.PRICE_TO_EARNINGS.__str__: self.financial_data.price_to_earnings,
            DictKey.EARNINGS_PER_SHARE.__str__: self.financial_data.earnings_per_share,
            DictKey.ENTERPRISE_TO_REVENUE.__str__: self.financial_data.enterprise_to_revenue
        }

    def _get_cash_flow_data(self):
        return {
            DictKey.FREE_CASH_FLOW.__str__: self.financial_data.free_cash_flow,
            DictKey.OPERATING_CASH_FLOW.__str__: self.financial_data.operating_cash_flow,
        }

    def _get_profitability_data(self):
        return {
            DictKey.RETURN_ON_EQUITY.__str__: self.financial_data.return_on_equity,
            DictKey.RETURN_ON_ASSETS.__str__: self.financial_data.return_on_assets,
            DictKey.RETURN_ON_INVESTED_CAPITAL.__str__: self.financial_data.calculate_return_on_invested_capital(),
            DictKey.RETURN_ON_INVESTMENT.__str__: self.financial_data.calculate_return_on_investment()
        }

    def get_evaluated_growth_criteria(self):
        return {
            GrowthCriteria.EARNINGS.__str__: HistoricalEarningsData.evaluate_growth_criteria(
                chart_list=self.earnings_and_earnings_history,
                percentage_criteria=GrowthCriteria.EARNINGS.percentage_criteria,
                attribute=GrowthCriteria.EARNINGS.attribute
            ),
            GrowthCriteria.REVENUE.__str__: HistoricalEarningsData.evaluate_growth_criteria(
                chart_list=self.earnings_and_earnings_history,
                percentage_criteria=GrowthCriteria.REVENUE.percentage_criteria,
                attribute=GrowthCriteria.REVENUE.attribute
            ),
            GrowthCriteria.NET_INCOME.__str__: self.income_statement.evaluate_growth_criteria(
                percentage_criteria=GrowthCriteria.NET_INCOME.percentage_criteria,
                attribute=GrowthCriteria.NET_INCOME.attribute
            ),
            GrowthCriteria.SALES.__str__: self.income_statement.evaluate_growth_criteria(
                percentage_criteria=GrowthCriteria.SALES.percentage_criteria,
                attribute=GrowthCriteria.SALES.attribute
            ),
            GrowthCriteria.OPERATING_CASH_FLOW.__str__: self.cash_flow.evaluate_growth_criteria(
                percentage_criteria=GrowthCriteria.OPERATING_CASH_FLOW.percentage_criteria,
                attribute=GrowthCriteria.OPERATING_CASH_FLOW.attribute
            ),
            GrowthCriteria.FREE_CASH_FLOW.__str__: self.cash_flow.evaluate_growth_criteria(
                percentage_criteria=GrowthCriteria.FREE_CASH_FLOW.percentage_criteria,
                attribute=GrowthCriteria.FREE_CASH_FLOW.attribute,
            ),
            GrowthCriteria.BOOK_VALUE_AND_DIVIDENDS.__str__: CombinableYQData(
                combination=GrowthCriteria.BOOK_VALUE_AND_DIVIDENDS,
                balance_sheet=self.balance_sheet,
                cash_flow=self.cash_flow,
            ).combine_process_and_evaluate_growth_criteria(),
            GrowthCriteria.ROIC.__str__: CombinableYQData(
                combination=GrowthCriteria.ROIC,
                balance_sheet=self.balance_sheet,
                income_statement=self.income_statement,
            ).combine_process_and_evaluate_growth_criteria(),
            GrowthCriteria.ROE.__str__: CombinableYQData(
                combination=GrowthCriteria.ROE,
                balance_sheet=self.balance_sheet,
                income_statement=self.income_statement,
            ).combine_process_and_evaluate_growth_criteria(),
            GrowthCriteria.OWNER_EARNINGS.__str__: CombinableYQData(
                combination=GrowthCriteria.OWNER_EARNINGS,
                balance_sheet=self.balance_sheet,
                income_statement=self.income_statement,
                cash_flow=self.cash_flow,
            ).combine_process_and_evaluate_growth_criteria(),
        }

    def to_csv(self):
        self._to_csv(
            ticker_symbol=self.general_stock_info.ticker,
            general_stock_info=self.general_stock_info,
            revenue_data=lambda: self._get_revenue_data(),
            earnings_data=lambda: self._get_earnings_data(),
            debt_data=lambda: self._get_debt_data(),
            margins_data=lambda: self._get_margins_data(),
            dividends_data=lambda: self._get_dividend_data(),
            financial_ratio_data=lambda: self._get_financial_ratio_data(),
            cash_flow_data=lambda: self._get_cash_flow_data(),
            profitability_data=lambda: self._get_profitability_data(),
            evaluated_growth_criteria=lambda: self._evaluated_growth_criteria,
            criteria_pass_count=self.criteria_pass_count
        )
