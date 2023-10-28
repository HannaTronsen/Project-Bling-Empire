from abc import ABC
from dataclasses import dataclass
from typing import Optional
from context.yquery_ticker.main.data_classes.date import Date, PeriodType
from context.yquery_ticker.main.enums.quarter import Quarter
from context.yquery_ticker.main.interfaces.castable_data import CastableDataInterface

AS_OF_DATE = 'asOfDate'
PERIOD_TYPE = 'periodType'


@dataclass
class YQDataFrameData(ABC, CastableDataInterface):
    asOfDate: Optional[Date]
    periodType: Optional[PeriodType]

    @classmethod
    def sorted(cls, unsorted_model_list: list['YQDataFrameData']):
        def date_sort_key(item):
            if item.asOfDate is None:
                return 0, Quarter.FIRST_QUARTER
            return item.asOfDate.year or 0, item.asOfDate.quarter.__int__ or Quarter.FIRST_QUARTER.__int__
        return sorted(unsorted_model_list, key=date_sort_key)

    @classmethod
    def get_most_recent_entry(cls, sorted_list: list['YQDataFrameData']):
        return sorted_list[-1]

    @classmethod
    def get_oldest_entry(cls, sorted_list: list['YQDataFrameData']):
        return sorted_list[0]
