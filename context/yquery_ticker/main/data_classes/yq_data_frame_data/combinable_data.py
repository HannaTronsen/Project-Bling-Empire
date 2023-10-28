from dataclasses import dataclass
from typing import Optional
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData


@dataclass
class CombinableDataClass(YQDataFrameData):
    value: Optional[int | float]
