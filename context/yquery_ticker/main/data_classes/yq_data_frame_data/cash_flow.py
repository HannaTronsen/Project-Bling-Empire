from dataclasses import dataclass
from typing import Optional

from context.yquery_ticker.main.classes.iterable_data import IterableDataInterface
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData

CASH_DIVIDENDS_PAID = 'CashDividendsPaid'


@dataclass
class CashFlowDataClass(IterableDataInterface, YQDataFrameData):
    cashDividendsPaid: Optional[float]
