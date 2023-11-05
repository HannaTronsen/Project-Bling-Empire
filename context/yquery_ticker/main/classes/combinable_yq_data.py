from typing import Optional

from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.classes.yahoo.balance_sheet_data import BalanceSheetData
from context.yquery_ticker.main.classes.yahoo.cash_flow_data import CashFlowData
from context.yquery_ticker.main.classes.yahoo.income_statement_data import IncomeStatementData
from context.yquery_ticker.main.const import WRONG_TYPE_STRING
from context.yquery_ticker.main.data_classes.yq_data_frame_data.combinable_data import CombinableDataClass
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData
from context.yquery_ticker.main.enums.growth_criteria import GrowthCriteria


def _get_divided_value_or_zero(numerator, denominator):
    if denominator is None or denominator == 0:
        return 0
    return numerator / denominator


class CombinableYQData(TimeSeriesDataCollection):
    def __init__(
            self,
            combination: GrowthCriteria,
            balance_sheet: Optional[BalanceSheetData] = None,
            cash_flow: Optional[CashFlowData] = None,
            income_statement: Optional[IncomeStatementData] = None
    ):
        self.combination = combination
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow
        self.income_statement = income_statement

    def get_book_value_and_dividends_list(self) -> list[CombinableDataClass]:
        result = []
        for cash_flow_entry in self.cash_flow.entries:
            balance_sheet_entry = self.balance_sheet.get_entry_of(
                as_of_date=cash_flow_entry.asOfDate,
                period_type=cash_flow_entry.periodType,
            )
            result.append(
                CombinableDataClass(
                    asOfDate=cash_flow_entry.asOfDate,
                    periodType=cash_flow_entry.periodType,
                    value=balance_sheet_entry.commonStockEquity + abs(cash_flow_entry.cashDividendsPaid)
                )
            )
        return result

    def get_return_on_income_capital_list(self) -> list[CombinableDataClass]:
        result = []
        for income_statement_entry in self.income_statement.entries:
            balance_sheet_entry = self.balance_sheet.get_entry_of(
                as_of_date=income_statement_entry.asOfDate,
                period_type=income_statement_entry.periodType
            )
            result.append(
                CombinableDataClass(
                    asOfDate=income_statement_entry.asOfDate,
                    periodType=income_statement_entry.periodType,
                    value=_get_divided_value_or_zero(
                        numerator=income_statement_entry.netIncome,
                        denominator=balance_sheet_entry.commonStockEquity + balance_sheet_entry.totalDebt
                    )
                )
            )
        return result

    def get_return_on_equity_list(self) -> list[CombinableDataClass]:
        result = []
        for income_statement_entry in self.income_statement.entries:
            balance_sheet_entry = self.balance_sheet.get_entry_of(
                as_of_date=income_statement_entry.asOfDate,
                period_type=income_statement_entry.periodType
            )
            result.append(
                CombinableDataClass(
                    asOfDate=income_statement_entry.asOfDate,
                    periodType=income_statement_entry.periodType,
                    value=_get_divided_value_or_zero(
                        numerator=income_statement_entry.netIncome,
                        denominator=balance_sheet_entry.commonStockEquity
                    )
                )
            )
        return result

    def get_owner_earnings_list(self) -> list[CombinableDataClass]:
        result = []
        for income_statement_entry in self.income_statement.entries:
            cash_flow_entry = self.cash_flow.get_entry_of(
                as_of_date=income_statement_entry.asOfDate,
                period_type=income_statement_entry.periodType,
            )
            balance_sheet_entry = self.balance_sheet.get_entry_of(
                as_of_date=income_statement_entry.asOfDate,
                period_type=income_statement_entry.periodType
            )
            result.append(
                CombinableDataClass(
                    asOfDate=income_statement_entry.asOfDate,
                    periodType=income_statement_entry.periodType,
                    value=(abs(income_statement_entry.netIncome) +
                           abs(cash_flow_entry.depreciationAndAmortization) +
                           abs(balance_sheet_entry.accountsReceivable) +
                           abs(balance_sheet_entry.accountsPayable) +
                           abs(income_statement_entry.taxProvision) +
                           abs(cash_flow_entry.capitalExpenditure)
                           )
                )
            )
        return result

    def combine_process_and_evaluate_growth_criteria(self):
        if self.combination == GrowthCriteria.BOOK_VALUE_AND_DIVIDENDS:
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=YQDataFrameData.sorted(self.get_book_value_and_dividends_list()),
                    attribute="value"
                ),
                percentage_requirement=GrowthCriteria.BOOK_VALUE_AND_DIVIDENDS.__percentage_criteria__
            )
        elif self.combination == GrowthCriteria.ROIC:
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=YQDataFrameData.sorted(self.get_return_on_income_capital_list()),
                    attribute="value"
                ),
                percentage_requirement=GrowthCriteria.ROIC.__percentage_criteria__
            )
        elif self.combination == GrowthCriteria.ROE:
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=YQDataFrameData.sorted(self.get_return_on_equity_list()),
                    attribute="value"
                ),
                percentage_requirement=GrowthCriteria.ROE.__percentage_criteria__
            )
        elif self.combination == GrowthCriteria.OWNER_EARNINGS:
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=YQDataFrameData.sorted(self.get_owner_earnings_list()),
                    attribute="value"
                ),
                percentage_requirement=GrowthCriteria.OWNER_EARNINGS.__percentage_criteria__
            )
        else:
            raise TypeError(WRONG_TYPE_STRING.format(type=self.combination))
