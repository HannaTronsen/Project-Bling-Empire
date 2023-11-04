from dataclasses import dataclass
from typing import Optional
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData

NET_INCOME = 'NetIncome'
TOTAL_REVENUE = 'TotalRevenue'
INTEREST_EXPENSE = 'InterestExpense'
INTEREST_EXPENSE_NON_OPERATING = 'InterestExpenseNonOperating'
TOTAL_OTHER_FINANCE_COST = 'TotalOtherFinanceCost'
TAX_PROVISION = 'TaxProvision'


@dataclass
class IncomeStatementDataClass(YQDataFrameData):
    netIncome: Optional[float]
    totalRevenue: Optional[float]
    interest_expense: Optional[float]
    interest_expense_non_operating: Optional[float]
    total_other_finance_cost: Optional[float]
    taxProvision: Optional[float]

    @classmethod
    def mockk(cls, asOfDate, periodType):
        return IncomeStatementDataClass(
            asOfDate=asOfDate,
            periodType=periodType,
            netIncome=0,
            totalRevenue=0,
            interest_expense=0,
            interest_expense_non_operating=0,
            total_other_finance_cost=0,
            taxProvision=0,
        )
