from enum import Enum


# Might change later
class IncomeStatement(Enum):
    AS_OF_DATE = ('asOfDate', str)

    @property
    def __name__(self):
        return self.value[0]

    @property
    def __type__(self):
        return self.value[1]
