from abc import ABC
from ..data_classes.charts import Chart
from ..const import (
    ATTRIBUTE_ERROR_STRING,
    INVALID_LIST_LENGTH_STRING,
    INVALID_VALUE_COMPARISON
)
from ..data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData


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
    def passes_percentage_increase_requirements(cls, percentages, percentage_requirement) -> bool:
        return all(percent >= percentage_requirement for percent in percentages)

    @classmethod
    def _get_attribute_values(cls, index, model_list, attribute):
        try:
            earlier = getattr(model_list[index], attribute)
            later = getattr(model_list[index + 1], attribute)
        except AttributeError:
            raise AttributeError(ATTRIBUTE_ERROR_STRING.format(attribute=attribute, index=index))
        return earlier, later

    """
    These two functions below are relevant only when the function 'is_consistently_up_trending()' returns False.
    They performs calculations in reverse chronological order by comparing earlier time points with 
    later time points. In this context, it is expected that the values at later time points are lower
    than the current time point, indicating a linear upward trend when the list is reversed to its
    original order. If the values at later time points are higher than the current value, reversing
    the list would result in a dip in the trajectory.

    Interval is set to 1 because a valid time interval can not be 0.
    Since the interval is inherently going to be returned inside the for loop, 
    there is no need to include a final return statement for it.
    """

    @classmethod
    def _get_consecutive_down_trending_interval_from_reversed_simple_list(
            cls,
            simple_list: list[float | int],
    ) -> int:
        reversed_series = list(reversed(simple_list))
        interval = 1
        for index in range(len(reversed_series) - 1):
            earlier, later = reversed_series[index], reversed_series[index + 1]

            if cls._is_down_trending(earlier, later):
                interval += 1
            else:
                return interval

    @classmethod
    def _get_consecutive_down_trending_interval_from_reversed_model_list(
            cls,
            model_list: list[Chart | YQDataFrameData],
            attribute: str
    ) -> int:
        reversed_model_list = list(reversed(model_list))
        interval = 1
        for index in range(len(reversed_model_list) - 1):
            earlier, later = cls._get_attribute_values(index, reversed_model_list, attribute)

            if cls._is_down_trending(earlier, later):
                interval += 1
            else:
                return interval

    @classmethod
    def _get_percentage_increase(cls, earlier, later) -> float | int:
        if earlier != 0:
            return round(number=(later - earlier) / abs(earlier) * 100, ndigits=2)
        else:
            if later != 0:
                return round(number=(later - earlier) / 1 * 100, ndigits=2)
            else:
                return 0

    @classmethod
    def calculate_percentage_increase_for_simple_list(cls, simple_list: list[int | float]) -> list:
        result = []
        for index in range(len(simple_list) - 1):
            earlier, later = simple_list[index], simple_list[index + 1]
            result.append(cls._get_percentage_increase(earlier=earlier, later=later))
        return result

    @classmethod
    def _calculate_percentage_increase_for_model_list(
            cls,
            model_list: list[Chart | YQDataFrameData],
            attribute: str
    ) -> list:
        result = []
        for index in range(len(model_list) - 1):
            earlier, later = cls._get_attribute_values(index, model_list, attribute)
            result.append(cls._get_percentage_increase(earlier=earlier, later=later))
        return result

    """
    If the function 'is_consistently_up_trending()' returns False,
    then a private call to 'cls._get_consecutive_down_trending_interval_from_reversed_series/list()' 
    will be made to determine the most recent time interval that exhibited an upward trend.

    This ensures only valid lists will be passed to the _get_consecutive_down_trending_interval_from_reversed_list()
    function, meaning we don't need to have the same error handling right again.
    """

    @classmethod
    def is_consistently_up_trending_simple_list(cls, simple_list: list[int | float]) -> [bool, list[int | float]]:
        if len(simple_list) < 2:
            raise ValueError(INVALID_LIST_LENGTH_STRING.format(list=simple_list))

        for index in range(len(simple_list) - 1):
            earlier, later = simple_list[index], simple_list[index + 1]

            if cls._is_invalid_comparison(earlier, later):
                raise ValueError(INVALID_VALUE_COMPARISON.format(value1=type(earlier), value2=type(later)))
            elif cls._not_up_trending(earlier, later):
                return False, cls._get_consecutive_down_trending_interval_from_reversed_simple_list(
                    simple_list=simple_list,
                )
        return True, simple_list

    @classmethod
    def is_consistently_up_trending_model_list(
            cls,
            model_list: list[Chart | YQDataFrameData],
            attribute: str
    ) -> [bool, list[Chart | YQDataFrameData]]:
        if len(model_list) < 2:
            raise ValueError(INVALID_LIST_LENGTH_STRING.format(list=model_list))

        for index in range(len(model_list) - 1):
            earlier, later = cls._get_attribute_values(index, model_list, attribute)

            if cls._is_invalid_comparison(earlier, later):
                raise ValueError(INVALID_VALUE_COMPARISON.format(value1=type(earlier), value2=type(later)))
            elif cls._not_up_trending(earlier, later):
                return False, cls._get_consecutive_down_trending_interval_from_reversed_model_list(
                    model_list=model_list,
                    attribute=attribute
                )
        return True, model_list
