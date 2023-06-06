from dataclasses import dataclass
from abc import ABC, abstractmethod
from context.yquery_ticker.main.data_classes.date import Date
    
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
    estimate: float #just to map to model for now
    
    def get_section_from_json_path(base): return base ['earningsChart'] ['quarterly']
    

@dataclass
class FinancialsDataChart(Chart):
    revenue: float
    earnings: float
    
@dataclass
class QuarterlyFinancialsDataChart(FinancialsDataChart):
    def get_section_from_json_path(base): return base ['financialsChart'] ['quarterly']

@dataclass
class YearlyFinancialsDataChart(FinancialsDataChart):
    def get_section_from_json_path(base): return base ['financialsChart'] ['yearly']
    
