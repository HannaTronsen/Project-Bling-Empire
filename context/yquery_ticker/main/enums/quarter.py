from enum import Enum

from config import QUARTER_SHOW_DEBUG_PRINT
from ..const import NO_MATCHING_ENUM_MEMBER_STRING


class QuarterId(Enum):
    Q1 = "1Q"
    Q2 = "2Q"
    Q3 = "3Q"
    Q4 = "4Q"


class Quarter(Enum):
    FIRST_QUARTER = (QuarterId.Q1, 1)
    SECOND_QUARTER = (QuarterId.Q2, 2)
    THIRD_QUARTER = (QuarterId.Q3, 3)
    FOURTH_QUARTER = (QuarterId.Q4, 4)

    @property
    def __id__(self):
        return self.value[0]

    @property
    def __int__(self):
        return self.value[1]

    @classmethod
    def from_quarter_date(cls, quarter_date: str):
        for enum in cls:
            if enum.__id__.value == quarter_date:
                return enum
        if QUARTER_SHOW_DEBUG_PRINT:
            print(NO_MATCHING_ENUM_MEMBER_STRING.format(identifier="quarter date", value=quarter_date))
        return None

    @classmethod
    def from_id(cls, quarter_id: QuarterId):
        for enum in cls:
            if enum.__id__ == quarter_id:
                return enum
        if QUARTER_SHOW_DEBUG_PRINT:
            print(NO_MATCHING_ENUM_MEMBER_STRING.format(identifier="quarter id", value=quarter_id))
        return None


class Month(Enum):
    JAN = (Quarter.FIRST_QUARTER, "01")
    FEB = (Quarter.FIRST_QUARTER, "02")
    MAR = (Quarter.FIRST_QUARTER, "03")
    APR = (Quarter.SECOND_QUARTER, "04")
    MAY = (Quarter.SECOND_QUARTER, "05")
    JUN = (Quarter.SECOND_QUARTER, "06")
    JUL = (Quarter.THIRD_QUARTER, "07")
    AUG = (Quarter.THIRD_QUARTER, "08")
    SEP = (Quarter.THIRD_QUARTER, "09")
    OCT = (Quarter.FOURTH_QUARTER, "10")
    NOV = (Quarter.FOURTH_QUARTER, "11")
    DEC = (Quarter.FOURTH_QUARTER, "12")

    @property
    def __quarter__(self) -> Quarter:
        return self.value[0]

    @property
    def __month_str__(self):
        return self.value[1]

    @classmethod
    def from_month(cls, month: str):
        for enum in cls:
            if enum.__month_str__ == month:
                return enum
        if QUARTER_SHOW_DEBUG_PRINT:
            print(NO_MATCHING_ENUM_MEMBER_STRING.format(identifier="month", value=month))
        return None
