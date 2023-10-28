from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from ..data_classes.date import Date
from ..enums.quarter import Quarter


@dataclass
class Chart(ABC):
    date: Date

    def convert_date(self):
        self.date = Date.convert_date(date_input=self.date)
        return self

    @abstractmethod
    def get_section_from_json_path(self):
        pass

    def __getitem__(self, key):
        if key in self.date:
            return getattr(self, key, None)
        else:
            raise KeyError(f"Key '{key}' not found in data container")

    @classmethod
    def sorted(cls, unsorted_model_list: list['Chart']):
        def date_sort_key(item):
            if item.date is None or item.date.quarter is None:
                return 0, Quarter.FIRST_QUARTER
            return item.date.year or 0, item.date.quarter.__int__ or Quarter.FIRST_QUARTER.__int__
        return sorted(unsorted_model_list, key=date_sort_key)


@dataclass
class QuarterlyEarningsDataChart(Chart):
    actual: Optional[float]
    estimate: Optional[float]  # Just to map to model for now

    def get_section_from_json_path(self): return self['earningsChart']['quarterly']


@dataclass
class FinancialsDataChart(Chart, ABC):
    revenue: Optional[float]
    earnings: Optional[float]


@dataclass
class QuarterlyFinancialsDataChart(FinancialsDataChart):
    def get_section_from_json_path(self): return self['financialsChart']['quarterly']


@dataclass
class YearlyFinancialsDataChart(FinancialsDataChart):
    def get_section_from_json_path(self): return self['financialsChart']['yearly']
