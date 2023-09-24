from enum import Enum


class GrowthCriteria(Enum):
    EARNINGS = ("earnings", 1)  # TODO(Hanna): Find out what this requirement should be
    REVENUE = ("revenue", 1)  # TODO(Hanna): Find out what this requirement should be

    @property
    def __str__(self):
        return self.value[0]

    @property
    def __percentage_criteria__(self):
        return self.value[1]
