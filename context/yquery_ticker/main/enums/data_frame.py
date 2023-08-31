from enum import Enum


class DataFrame(Enum):
    AS_OF_DATE = ('asOfDate', str)

    @property
    def __name__(self):
        return self.value[0]

    @property
    def __type__(self):
        return self.value[1]
