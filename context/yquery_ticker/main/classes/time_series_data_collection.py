from abc import ABC
from typing import Any
from ..data_classes.charts import Chart
from ..const import (
    ATTRIBUTE_ERROR_STRING,
    INVALID_LIST_LENGTH_STRING,
    INVALID_VALUE_COMPARISON
)


class TimeSeriesDataCollection(ABC):
    @classmethod
    def _is_invalid_comparison(cls, i, j):
        return i is None or j is None or type(i) != type(j)

    @classmethod
    def _not_up_trending(cls, i, j):
        return i > j

    @classmethod
    def _is_down_trending(cls, i, j):
        return cls._not_up_trending(i, j)

    @classmethod
    def _passes_percentage_increase_requirements(cls, series, percentage_requirement) -> bool:
        return all(percent >= percentage_requirement for percent in series)

    @classmethod
    def _get_attribute_values(cls, index, chart_list, attribute):
        try:
            i = getattr(chart_list[index], attribute)
            j = getattr(chart_list[index + 1], attribute)
        except AttributeError:
            raise AttributeError(ATTRIBUTE_ERROR_STRING.format(attribute=attribute, index=index))
        return i, j

    """
    This function is relevant only when the function 'is_consistently_up_trending()' returns False.
    It performs calculations in reverse chronological order by comparing earlier time points with 
    later time points. In this context, it is expected that the values at later time points are lower
    than the current time point, indicating a linear upward trend when the list is reversed to its
    original order. If the values at later time points are higher than the current value, reversing
    the list would result in a dip in the trajectory.

    Interval is set to 1 because a valid time interval can not be 0.
    Since the interval is inherently going to be returned inside the for loop, 
    there is no need to include a final return statement for it.
    """
    @classmethod
    def _get_consecutive_down_trending_interval_from_reversed_list(
            cls,
            chart_list: list[Chart],
            attribute: str = None
    ) -> int:
        reversed_chart_list = list(reversed(chart_list))
        interval = 1
        isValidAttribute = attribute is not None and type(attribute) == str
        for index in range(len(reversed_chart_list) - 1):
            i, j = cls._get_attribute_values(index, reversed_chart_list, attribute) if isValidAttribute else (
                reversed_chart_list[index], reversed_chart_list[index + 1]
            )
            if cls._is_down_trending(i, j):
                interval += 1
            else:
                return interval

    @classmethod
    def _calculate_percentage_increase_for_data_set(cls, chart_list: list[Chart], attribute: str = None) -> list:
        series = []
        isValidAttribute = attribute is not None and type(attribute) == str
        for index in range(len(chart_list) - 1):
            i, j = cls._get_attribute_values(index, chart_list, attribute) if isValidAttribute else (
                chart_list[index], chart_list[index + 1]
            )
            if i != 0:
                percentage_increase = round(number=(j - i) / abs(i) * 100, ndigits=2)
                series.append(percentage_increase)
            else:
                series.append(0)
        return series

    """
    If the function 'is_consistently_up_trending()' returns False,
    then a private call to 'cls._get_consecutive_down_trending_interval_from_reversed_list()' 
    will be made to determine the most recent time interval that exhibited an upward trend.

    This ensures only valid lists will be passed to the _get_consecutive_down_trending_interval_from_reversed_list()
    function, meaning we don't need to have the same error handling right again.
    """
    @classmethod
    def is_consistently_up_trending(cls, chart_list: list[Chart], attribute: str = None) -> Any:
        if len(chart_list) < 2:
            raise ValueError(INVALID_LIST_LENGTH_STRING.format(chart_list=chart_list))

        isValidAttribute = attribute is not None and type(attribute) == str
        for index in range(len(chart_list) - 1):
            i, j = cls._get_attribute_values(index, chart_list, attribute) if isValidAttribute else (
                chart_list[index], chart_list[index + 1]
            )
            if cls._is_invalid_comparison(i, j):
                raise ValueError(INVALID_VALUE_COMPARISON.format(value1=type(i), value2=type(j)))
            elif cls._not_up_trending(i, j):
                return (False, cls._get_consecutive_down_trending_interval_from_reversed_list(
                    chart_list=chart_list,
                    attribute=attribute)
                        )
        # TODO: Fix the return type
        return True, chart_list
