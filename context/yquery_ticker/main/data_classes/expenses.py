from dataclasses import dataclass
import dataclasses
from .iterable_data import IterableDataInterface
from enum import Enum, auto

class ExpensesFields(Enum):
    CAPITAL_EXPENDITURE = auto()
    INTEREST_EXPENSE = auto()
    INTEREST_EXPENSE_NON_OPERATING = auto()
    TOTAL_OTHER_FINANCE_COST = auto()

@dataclass
class Expenses(IterableDataInterface):
    capital_expenditure: float
    interest_expense: float
    interest_expense_non_operating: float
    total_other_finance_cost: float

    def check_has_invalid_value(self, values):
        for value in values:
            if value is None:
                return True
        return False
    
    # This function assumes that no values are None
    # and should be handled on another layer
    def sum(self, exclude: list[ExpensesFields] = []):
        total = 0
        for data_class_field in dataclasses.fields(self):
            if data_class_field.name not in [enum.name.lower() for enum in exclude]:
                total += getattr(self, data_class_field.name)

        return total