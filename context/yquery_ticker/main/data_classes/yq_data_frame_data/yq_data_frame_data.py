from abc import ABC
from dataclasses import dataclass

from context.yquery_ticker.main.classes.castable_data import CastableDataInterface


@dataclass
class YQDataFrameData(ABC, CastableDataInterface):
    pass
