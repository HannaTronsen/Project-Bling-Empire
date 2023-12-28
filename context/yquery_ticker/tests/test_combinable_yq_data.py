import unittest

from context.yquery_ticker.main.classes.combinable_yq_data import CombinableYQData
from context.yquery_ticker.main.classes.yahoo.balance_sheet_data import BalanceSheetData
from context.yquery_ticker.main.classes.yahoo.cash_flow_data import CashFlowData
from context.yquery_ticker.main.classes.yahoo.income_statement_data import IncomeStatementData
from context.yquery_ticker.main.data_classes.date import Date, PeriodType
from context.yquery_ticker.main.data_classes.yq_data_frame_data.balance_sheet import BalanceSheetDataClass
from context.yquery_ticker.main.data_classes.yq_data_frame_data.cash_flow import CashFlowDataClass
from context.yquery_ticker.main.data_classes.yq_data_frame_data.income_statement import IncomeStatementDataClass
from context.yquery_ticker.main.enums.growth_criteria import GrowthCriteria
from context.yquery_ticker.main.enums.quarter import Quarter


class test_combinable_yq_data(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_combinable_yq_data, self).__init__(*args, **kwargs)

    def test_evaluate_growth_criteria_for_book_value_and_dividends(self):
        self.balance_sheet_three_entries = BalanceSheetData(
            entries=[
                BalanceSheetDataClass(
                    asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    commonStockEquity=1000,
                    totalDebt=0,
                    accountsReceivable=0,
                    accountsPayable=0,
                ),
                BalanceSheetDataClass(
                    asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    commonStockEquity=1100,
                    totalDebt=0,
                    accountsReceivable=0,
                    accountsPayable=0,
                ),
                BalanceSheetDataClass(
                    asOfDate=Date(year=2024, quarter=Quarter.THIRD_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    commonStockEquity=1300,
                    totalDebt=0,
                    accountsReceivable=0,
                    accountsPayable=0,
                )
            ]
        )
        self.cash_flow_three_entries = CashFlowData(
            entries=[
                CashFlowDataClass(
                    asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    cashDividendsPaid=50,
                    operatingCashFlow=0,
                    freeCashFlow=0,
                    capitalExpenditure=0,
                    depreciationAndAmortization=0,
                ),
                CashFlowDataClass(
                    asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    cashDividendsPaid=45,
                    operatingCashFlow=0,
                    freeCashFlow=0,
                    capitalExpenditure=0,
                    depreciationAndAmortization=0,
                ),
                CashFlowDataClass(
                    asOfDate=Date(year=2024, quarter=Quarter.THIRD_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    cashDividendsPaid=50,
                    operatingCashFlow=0,
                    freeCashFlow=0,
                    capitalExpenditure=0,
                    depreciationAndAmortization=0,
                )
            ]
        )

        self.assertFalse(
            CombinableYQData(
                combination=GrowthCriteria.BOOK_VALUE_AND_DIVIDENDS,
                balance_sheet=self.balance_sheet_three_entries,
                cash_flow=self.cash_flow_three_entries,
            ).combine_process_and_evaluate_growth_criteria()
        )

        self.balance_sheet_three_entries = BalanceSheetData(
            entries=[
                BalanceSheetDataClass(
                    asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    commonStockEquity=1000,
                    totalDebt=0,
                    accountsReceivable=0,
                    accountsPayable=0,
                ),
                BalanceSheetDataClass(
                    asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    commonStockEquity=1155,  # Adjusted to ensure a 10% increase
                    totalDebt=0,
                    accountsReceivable=0,
                    accountsPayable=0,
                ),
                BalanceSheetDataClass(
                    asOfDate=Date(year=2024, quarter=Quarter.THIRD_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    commonStockEquity=1270,  # Adjusted to ensure a 10% increase
                    totalDebt=0,
                    accountsReceivable=0,
                    accountsPayable=0,
                )
            ]
        )

        self.assertTrue(
            CombinableYQData(
                combination=GrowthCriteria.BOOK_VALUE_AND_DIVIDENDS,
                balance_sheet=self.balance_sheet_three_entries,
                cash_flow=self.cash_flow_three_entries,
            ).combine_process_and_evaluate_growth_criteria()
        )

        self.balance_sheet_two_entries = BalanceSheetData(
            entries=[
                BalanceSheetDataClass(
                    asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    commonStockEquity=1000,
                    totalDebt=0,
                    accountsReceivable=0,
                    accountsPayable=0,
                ),
                BalanceSheetDataClass(
                    asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    commonStockEquity=1155,  # Adjusted to ensure a 10% increase
                    totalDebt=0,
                    accountsReceivable=0,
                    accountsPayable=0,
                ),
            ]
        )

        self.assertFalse(
            CombinableYQData(
                combination=GrowthCriteria.BOOK_VALUE_AND_DIVIDENDS,
                balance_sheet=self.balance_sheet_two_entries,
                cash_flow=self.cash_flow_three_entries,
            ).combine_process_and_evaluate_growth_criteria()
        )

        self.cash_flow_three_entries.entries[-1].cashDividendsPaid = 1370
        self.assertTrue(
            CombinableYQData(
                combination=GrowthCriteria.BOOK_VALUE_AND_DIVIDENDS,
                balance_sheet=self.balance_sheet_two_entries,
                cash_flow=self.cash_flow_three_entries,
            ).combine_process_and_evaluate_growth_criteria()
        )

        self.cash_flow_two_entries = CashFlowData(
            entries=[
                CashFlowDataClass(
                    asOfDate=Date(year=2022, quarter=Quarter.THIRD_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    cashDividendsPaid=50,
                    operatingCashFlow=0,
                    freeCashFlow=0,
                    capitalExpenditure=0,
                    depreciationAndAmortization=0,
                ),
                CashFlowDataClass(
                    asOfDate=Date(year=2023, quarter=Quarter.SECOND_QUARTER),
                    periodType=PeriodType.MONTH_12,
                    cashDividendsPaid=45,
                    operatingCashFlow=0,
                    freeCashFlow=0,
                    capitalExpenditure=0,
                    depreciationAndAmortization=0,
                ),
            ]
        )

        self.assertTrue(
            CombinableYQData(
                combination=GrowthCriteria.BOOK_VALUE_AND_DIVIDENDS,
                balance_sheet=self.balance_sheet_three_entries,
                cash_flow=self.cash_flow_two_entries,
            ).combine_process_and_evaluate_growth_criteria()
        )

    def test_evaluate_growth_criteria_for_owner_earnings(self):

        self.assertTrue(
            CombinableYQData(
                combination=GrowthCriteria.OWNER_EARNINGS,
                balance_sheet=BalanceSheetData(
                    entries=[
                        BalanceSheetDataClass(
                            asOfDate=Date(year=2022, quarter=Quarter.FIRST_QUARTER),
                            periodType=PeriodType.MONTH_12,
                            accountsReceivable=5,
                            accountsPayable=7,
                            commonStockEquity=0,
                            totalDebt=0,
                        ),
                        BalanceSheetDataClass(
                            asOfDate=Date(year=2022, quarter=Quarter.FIRST_QUARTER),
                            periodType=PeriodType.MONTH_12,
                            accountsReceivable=7,
                            accountsPayable=9,
                            commonStockEquity=0,
                            totalDebt=0,
                        )
                    ]
                ),
                income_statement=IncomeStatementData(
                    entries=[
                        IncomeStatementDataClass(
                            asOfDate=Date(year=2022, quarter=Quarter.FIRST_QUARTER),
                            periodType=PeriodType.MONTH_12,
                            netIncome=100,
                            taxProvision=10,
                            interest_expense=0,
                            interest_expense_non_operating=0,
                            totalRevenue=0,
                            total_other_finance_cost=0,
                        ),
                        IncomeStatementDataClass(
                            asOfDate=Date(year=2022, quarter=Quarter.FIRST_QUARTER),
                            periodType=PeriodType.MONTH_12,
                            netIncome=120,
                            taxProvision=12,
                            interest_expense=0,
                            interest_expense_non_operating=0,
                            totalRevenue=0,
                            total_other_finance_cost=0,
                        )
                    ]
                ),
                cash_flow=CashFlowData(
                    entries=[
                        CashFlowDataClass(
                            asOfDate=Date(year=2022, quarter=Quarter.FIRST_QUARTER),
                            periodType=PeriodType.MONTH_12,
                            depreciationAndAmortization=20,
                            capitalExpenditure=30,
                            freeCashFlow=0,
                            operatingCashFlow=0,
                            cashDividendsPaid=0,
                        ),
                        CashFlowDataClass(
                            asOfDate=Date(year=2022, quarter=Quarter.FIRST_QUARTER),
                            periodType=PeriodType.MONTH_12,
                            depreciationAndAmortization=22,
                            capitalExpenditure=32,
                            freeCashFlow=0,
                            operatingCashFlow=0,
                            cashDividendsPaid=0,
                        )
                    ]
                ),
            ).combine_process_and_evaluate_growth_criteria()
        )

        self.assertFalse(
            CombinableYQData(
                combination=GrowthCriteria.OWNER_EARNINGS,
                balance_sheet=BalanceSheetData(
                    entries=[
                        BalanceSheetDataClass(
                            asOfDate=Date(year=2022, quarter=Quarter.FIRST_QUARTER),
                            periodType=PeriodType.MONTH_12,
                            accountsReceivable=5,
                            accountsPayable=7,
                            commonStockEquity=0,
                            totalDebt=0,
                        ),
                        BalanceSheetDataClass(
                            asOfDate=Date(year=2022, quarter=Quarter.FIRST_QUARTER),
                            periodType=PeriodType.MONTH_12,
                            accountsReceivable=6,
                            accountsPayable=8,
                            commonStockEquity=0,
                            totalDebt=0,
                        )
                    ]
                ),
                income_statement=IncomeStatementData(
                    entries=[
                        IncomeStatementDataClass(
                            asOfDate=Date(year=2022, quarter=Quarter.FIRST_QUARTER),
                            periodType=PeriodType.MONTH_12,
                            netIncome=100,
                            taxProvision=10,
                            interest_expense=0,
                            interest_expense_non_operating=0,
                            totalRevenue=0,
                            total_other_finance_cost=0,
                        ),
                        IncomeStatementDataClass(
                            asOfDate=Date(year=2022, quarter=Quarter.FIRST_QUARTER),
                            periodType=PeriodType.MONTH_12,
                            netIncome=101,  # Decrease net income
                            taxProvision=11,
                            interest_expense=0,
                            interest_expense_non_operating=0,
                            totalRevenue=0,
                            total_other_finance_cost=0,
                        )
                    ]
                ),
                cash_flow=CashFlowData(
                    entries=[
                        CashFlowDataClass(
                            asOfDate=Date(year=2022, quarter=Quarter.FIRST_QUARTER),
                            periodType=PeriodType.MONTH_12,
                            depreciationAndAmortization=21,
                            capitalExpenditure=31,
                            freeCashFlow=0,
                            operatingCashFlow=0,
                            cashDividendsPaid=0,
                        ),
                        CashFlowDataClass(
                            asOfDate=Date(year=2022, quarter=Quarter.FIRST_QUARTER),
                            periodType=PeriodType.MONTH_12,
                            depreciationAndAmortization=23,
                            capitalExpenditure=33,
                            freeCashFlow=0,
                            operatingCashFlow=0,
                            cashDividendsPaid=0,
                        )
                    ]
                ),
            ).combine_process_and_evaluate_growth_criteria()
        )
