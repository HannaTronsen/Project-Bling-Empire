from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from ..data_classes.date import Date


@dataclass
class Chart(ABC):
    date: Date

    def convert_date(self):
        self.date = Date.convert_date(value=self.date)
        return self

    @abstractmethod
    def get_section_from_json_path(self):
        pass

    def __getitem__(self, key):
        if key in self.date:
            return getattr(self, key, None)
        else:
            raise KeyError(f"Key '{key}' not found in data container")


@dataclass
class QuarterlyEarningsDataChart(Chart):
    actual: float
    estimate: float  # Just to map to model for now

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
