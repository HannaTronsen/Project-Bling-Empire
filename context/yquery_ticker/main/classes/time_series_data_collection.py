from abc import ABC
from ..data_classes.charts import Chart
from ..const import (
    ATTRIBUTE_ERROR_STRING,
    INVALID_LIST_LENGTH_STRING,
    INVALID_VALUE_COMPARISON
)


class TimeSeriesDataCollection(ABC):
    @classmethod
    def _is_invalid_comparison(cls, earlier, later):
        return earlier is None or later is None or type(earlier) != type(later)

    @classmethod
    def _not_up_trending(cls, earlier, later):
        return earlier > later

    @classmethod
    def _is_down_trending(cls, earlier, later):
        return cls._not_up_trending(earlier, later)

    @classmethod
    def _passes_percentage_increase_requirements(cls, series, percentage_requirement) -> bool:
        return all(percent >= percentage_requirement for percent in series)

    @classmethod
    def _get_attribute_values(cls, index, chart_list, attribute):
        try:
            earlier = getattr(chart_list[index], attribute)
            later = getattr(chart_list[index + 1], attribute)
        except AttributeError:
            raise AttributeError(ATTRIBUTE_ERROR_STRING.format(attribute=attribute, index=index))
        return earlier, later

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
    def _get_consecutive_down_trending_interval_from_reversed_series(
            cls,
            series: list[float | int],
    ) -> int:
        reversed_series = list(reversed(series))
        interval = 1
        for index in range(len(reversed_series) - 1):
            earlier, later = reversed_series[index], reversed_series[index + 1]

            if cls._is_down_trending(earlier, later):
                interval += 1
            else:
                return interval

    @classmethod
    def _get_consecutive_down_trending_interval_from_reversed_list(
            cls,
            chart_list: list[Chart],
            attribute: str
    ) -> int:
        reversed_chart_list = list(reversed(chart_list))
        interval = 1
        for index in range(len(reversed_chart_list) - 1):
            earlier, later = cls._get_attribute_values(index, reversed_chart_list, attribute)

            if cls._is_down_trending(earlier, later):
                interval += 1
            else:
                return interval

    @classmethod
    def _calculate_percentage_increase_for_series(cls, series: list[int | float]) -> list:
        result = []
        for index in range(len(series) - 1):
            earlier, later = series[index], series[index + 1]

            if earlier != 0:
                percentage_increase = round(number=(later - earlier) / abs(earlier) * 100, ndigits=2)
                result.append(percentage_increase)
            else:
                result.append(0)
        return result

    @classmethod
    def _calculate_percentage_increase_for_chart_list(cls, chart_list: list[Chart], attribute: str) -> list:
        result = []
        for index in range(len(chart_list) - 1):
            earlier, later = cls._get_attribute_values(index, chart_list, attribute)

            if earlier != 0:
                percentage_increase = round(number=(later - earlier) / abs(earlier) * 100, ndigits=2)
                result.append(percentage_increase)
            else:
                result.append(0)
        return result

    """
   If the function 'is_consistently_up_trending()' returns False,
   then a private call to 'cls._get_consecutive_down_trending_interval_from_reversed_series/list()' 
   will be made to determine the most recent time interval that exhibited an upward trend.

   This ensures only valid lists will be passed to the _get_consecutive_down_trending_interval_from_reversed_list()
   function, meaning we don't need to have the same error handling right again.
   """

    @classmethod
    def is_consistently_up_trending_series(cls, series: list[int | float]) -> [bool, list[int | float]]:
        if len(series) < 2:
            raise ValueError(INVALID_LIST_LENGTH_STRING.format(chart_list=series))

        for index in range(len(series) - 1):
            earlier, later = series[index], series[index + 1]

            if cls._is_invalid_comparison(earlier, later):
                raise ValueError(INVALID_VALUE_COMPARISON.format(value1=type(earlier), value2=type(later)))
            elif cls._not_up_trending(earlier, later):
                return False, cls._get_consecutive_down_trending_interval_from_reversed_series(
                    series=series,
                )
        return True, series

    @classmethod
    def is_consistently_up_trending_chart_list(cls, chart_list: list[Chart], attribute: str) -> [bool, list[Chart]]:
        if len(chart_list) < 2:
            raise ValueError(INVALID_LIST_LENGTH_STRING.format(chart_list=chart_list))

        for index in range(len(chart_list) - 1):
            earlier, later = cls._get_attribute_values(index, chart_list, attribute)

            if cls._is_invalid_comparison(earlier, later):
                raise ValueError(INVALID_VALUE_COMPARISON.format(value1=type(earlier), value2=type(later)))
            elif cls._not_up_trending(earlier, later):
                return False, cls._get_consecutive_down_trending_interval_from_reversed_list(
                    chart_list=chart_list,
                    attribute=attribute
                )
        return True, chart_list
