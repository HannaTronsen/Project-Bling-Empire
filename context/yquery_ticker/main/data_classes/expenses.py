from dataclasses import dataclass
import dataclasses
from typing import Optional

from context.yquery_ticker.main.classes.castable_data import CastableDataInterface
from context.yquery_ticker.main.enums.expenses import ExpensesFields
from ..classes.iterable_data import IterableDataInterface


@dataclass
class Expenses(IterableDataInterface, CastableDataInterface):
    capital_expenditure: Optional[float]
    interest_expense: Optional[float]
    interest_expense_non_operating: Optional[float]
    total_other_finance_cost: Optional[float]

    @staticmethod
    def check_has_invalid_value(values):
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
