from enum import Enum

SHOW_PRINT = True

class QuarterId(Enum):
    Q1 = "1Q",
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
        if SHOW_PRINT:
            print(f"No matching enum member found for quarter date: {quarter_date}")
        
        return None
    
    @classmethod
    def from_id(cls, quarter_id: QuarterId):
        for enum in cls:
            if enum.__id__ == quarter_id:
                return enum
        if SHOW_PRINT:
            print(f"No matching enum member found for quarter id: {quarter_id}")
        
        return None