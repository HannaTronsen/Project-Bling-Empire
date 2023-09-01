from abc import ABC, abstractmethod
from dataclasses import dataclass
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


@dataclass
class QuarterlyEarningsDataChart(Chart):
    actual: float
    estimate: float  # Just to map to model for now

    def get_section_from_json_path(self): return self['earningsChart']['quarterly']


@dataclass
class FinancialsDataChart(Chart, ABC):
    revenue: float
    earnings: float


@dataclass
class QuarterlyFinancialsDataChart(FinancialsDataChart):
    def get_section_from_json_path(self): return self['financialsChart']['quarterly']


@dataclass
class YearlyFinancialsDataChart(FinancialsDataChart):
    def get_section_from_json_path(self): return self['financialsChart']['yearly']
