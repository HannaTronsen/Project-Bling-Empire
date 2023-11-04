from typing import Optional

from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.classes.yahoo.balance_sheet_data import BalanceSheetData
from context.yquery_ticker.main.classes.yahoo.cash_flow_data import CashFlowData
from context.yquery_ticker.main.classes.yahoo.income_statement_data import IncomeStatementData
from context.yquery_ticker.main.const import WRONG_TYPE_STRING
from context.yquery_ticker.main.data_classes.yq_data_frame_data.combinable_data import CombinableDataClass
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData
from context.yquery_ticker.main.enums.growth_criteria import GrowthCriteria
from context.yquery_ticker.main.utils.dict_key_enum import DictKey


class CombinableYQData(TimeSeriesDataCollection):
    def __init__(
            self,
            combination: DictKey,
            balance_sheet: Optional[BalanceSheetData] = None,
            cash_flow: Optional[CashFlowData] = None,
            income_statement: Optional[IncomeStatementData] = None
    ):
        self.combination = combination
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow
        self.income_statement = income_statement

    def combine_process_and_evaluate_growth_criteria(self):
        result = []
        if self.combination == DictKey.BOOK_VALUE_AND_DIVIDENDS:
            for balance_sheet_entry in self.balance_sheet.entries:
                cashDividendsPaid = self.cash_flow.get_entry_of(
                    as_of_date=balance_sheet_entry.asOfDate,
                    period_type=balance_sheet_entry.periodType,
                ).cashDividendsPaid
                result.append(
                    CombinableDataClass(
                        asOfDate=balance_sheet_entry.asOfDate,
                        periodType=balance_sheet_entry.periodType,
                        value=balance_sheet_entry.commonStockEquity + abs(cashDividendsPaid)
                    )
                )
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=YQDataFrameData.sorted(result),
                    attribute="value"
                ),
                percentage_requirement=GrowthCriteria.BOOK_VALUE_AND_DIVIDENDS.__percentage_criteria__
            )
        elif self.combination == DictKey.ROIC:
            for balance_sheet_entry in self.balance_sheet.entries:
                net_income = self.income_statement.get_entry_of(
                    as_of_date=balance_sheet_entry.asOfDate,
                    period_type=balance_sheet_entry.periodType
                ).netIncome
                denominator = balance_sheet_entry.commonStockEquity + balance_sheet_entry.totalDebt
                if denominator != 0:
                    result.append(
                        CombinableDataClass(
                            asOfDate=balance_sheet_entry.asOfDate,
                            periodType=balance_sheet_entry.periodType,
                            value=net_income / denominator
                        )
                    )
                else:
                    result.append(
                        CombinableDataClass(
                            asOfDate=balance_sheet_entry.asOfDate,
                            periodType=balance_sheet_entry.periodType,
                            value=0
                        )
                    )
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=YQDataFrameData.sorted(result),
                    attribute="value"
                ),
                percentage_requirement=GrowthCriteria.ROIC.__percentage_criteria__
            )
        elif self.combination == DictKey.ROE:
            for balance_sheet_entry in self.balance_sheet.entries:
                net_income = self.income_statement.get_entry_of(
                    as_of_date=balance_sheet_entry.asOfDate,
                    period_type=balance_sheet_entry.periodType
                )
                denominator = balance_sheet_entry.commonStockEquity
                if denominator != 0:
                    result.append(
                        CombinableDataClass(
                            asOfDate=balance_sheet_entry.asOfDate,
                            periodType=balance_sheet_entry.periodType,
                            value=net_income / denominator
                        )
                    )
                else:
                    result.append(
                        CombinableDataClass(
                            asOfDate=balance_sheet_entry.asOfDate,
                            periodType=balance_sheet_entry.periodType,
                            value=0
                        )
                    )
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_model_list(
                    model_list=YQDataFrameData.sorted(result),
                    attribute="value"
                ),
                percentage_requirement=GrowthCriteria.ROIC.__percentage_criteria__
            )
        elif self.combination == DictKey.OWNER_EARNINGS:
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

        else:
            raise TypeError(WRONG_TYPE_STRING.format(type=self.combination))
