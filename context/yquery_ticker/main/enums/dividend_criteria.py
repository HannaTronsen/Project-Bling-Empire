from datetime import datetime, timedelta
from enum import Enum
from typing import Optional


def evaluate_dividend_data_within_range(value: Optional[float], lower_bound: float, upper_bound: float) -> float:
    if value is not None:
        if lower_bound <= value <= upper_bound:
            return 1.0
    return 0.0


def evaluate_dividend_datetime_criteria(date: Optional[str]) -> float:
    if date is not None:
        ex_dividend_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

        time_difference = datetime.now() - ex_dividend_date

        is_within_one_year = time_difference <= timedelta(days=365)

        if is_within_one_year:
            return 1.0
    return 0.0


"""
Returns A score representing the evaluation result.
- 4 points: If present_value is greater than trailing_value.
- 3 points: If present_value is equal to trailing_value.
- 2 points: If present_value is not None, but trailing_value is None.
- 1 point: If present_value is less than trailing_value.
- 0.5 point: If present_value is None and trailing_value is not None.
- 0 points: If both present_value and trailing_value are None.
"""


def compare_and_evaluate_dividend_data(trailing_value: Optional[float], present_value: Optional[float]) -> float:
    if present_value is not None:
        if trailing_value is not None:
            if present_value > trailing_value:
                return 4.0
            elif present_value == trailing_value:
                return 3.0
            else:
                return 1.0
        else:
            return 2.0
    elif present_value is None and trailing_value is not None:
        return 0.5
    else:
        return 0.0


class DividendCriteria(Enum):
    PAYOUT_RATIO = "Payout Ratio"
    DIVIDEND_RATE = "Dividend  Rate"
    DIVIDEND_YIELD = "Dividend Yield"
    DIVIDEND_EX_DATE = "Dividend Ex Date"
    FIVE_YEAR_AVERAGE = "5 Year Average"

    @property
    def __str__(self):
        return self.value
