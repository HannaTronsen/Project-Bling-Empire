import unittest

from context.yquery_ticker.main.data_classes.expenses import Expenses
from context.yquery_ticker.main.enums.expenses import ExpensesFields


class test_expenses(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_expenses, self).__init__(*args, **kwargs)

    def test_sum_expenses(self):
        assert Expenses(
            capital_expenditure=1,
            interest_expense=0,
            interest_expense_non_operating=0,
            total_other_finance_cost=0
        ).sum() == 1
        assert Expenses(
            capital_expenditure=1,
            interest_expense=-2,
            interest_expense_non_operating=0,
            total_other_finance_cost=0
        ).sum() == -1
        assert Expenses(
            capital_expenditure=1,
            interest_expense=1,
            interest_expense_non_operating=2,
            total_other_finance_cost=0
        ).sum(exclude=[ExpensesFields.INTEREST_EXPENSE_NON_OPERATING]) == 2
        assert Expenses(
            capital_expenditure=1,
            interest_expense=1,
            interest_expense_non_operating=3,
            total_other_finance_cost=2
        ).sum(exclude=[ExpensesFields.TOTAL_OTHER_FINANCE_COST]) == 5
