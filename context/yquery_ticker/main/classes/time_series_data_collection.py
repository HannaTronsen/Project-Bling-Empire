from abc import ABC
from context.yquery_ticker.main.const import ATTRIBUTE_ERROR_STRING, INVALID_LIST_LENGTH_STRING, INVALID_VALUE_COMPARISON
from context.yquery_ticker.main.data_classes.charts import Chart


class TimeSeriesDataCollection(ABC):

    def _is_invalid_comparison( self, i, j): return i is None or j is None or type(i) != type(j)

    def _not_up_trending(self, i, j): return i > j

    def _is_down_trending(self, i, j): return self._not_up_trending(i, j)

    def _get_attribute_values(self, index, chart_list, attribute): 
        try:
            i = getattr(chart_list[index], attribute)
            j = getattr(chart_list[index + 1], attribute)
        except AttributeError:
            raise AttributeError(ATTRIBUTE_ERROR_STRING.format(attribute=attribute, index=index))
        return i, j

    def is_consistently_up_trending(self, chart_list: list[Chart], attribute: str = None) -> bool:
        """
        If the function 'is_consistently_up_trending()' returns False,
        then a private call to 'self._get_consecutive_down_trending_interval_from_reversed_list()' 
        will be made to determine the most recent time interval that exhibited an upward trend.

        This ensures only valid lists will be passed to the _get_consecutive_down_trending_interval_from_reversed_list() function,
        meaning we don't need to have the same error handling right again.
        """
        if len(chart_list) < 2:
            raise ValueError(INVALID_LIST_LENGTH_STRING.format(chart_list=chart_list))
        
        for index in range(len(chart_list) - 1):
            i, j = self._get_attribute_values(index, chart_list, attribute) if attribute != None else (chart_list[index], chart_list[index + 1])

            if self._is_invalid_comparison(i, j): 
                raise ValueError(INVALID_VALUE_COMPARISON.format(value1=type(i), value2=type(j)))
            elif self._not_up_trending(i, j):
                return (False, self._get_consecutive_down_trending_interval_from_reversed_list(chart_list=chart_list, attribute=attribute))
        return (True, len(chart_list))
    
    def _get_consecutive_down_trending_interval_from_reversed_list(self, chart_list: list[Chart], attribute: str = None) -> int:
        """
        This function is relevant only when the function 'is_consistently_up_trending()' returns False.
        It performs calculations in reverse chronological order by comparing earlier time points with later time points.
        In this context, it is expected that the values at later time points are lower than the current time point, indicating a linear upward trend when the list is reversed to its original order.
        If the values at later time points are higher than the current value, reversing the list would result in a dip in the trajectory.

        interval is set to 1 because a valid time interval can not be 0.
        """
        reversed_chart_list = list(reversed(chart_list))
        interval = 1
        for index in range(len(reversed_chart_list) - 1):
            i, j = self._get_attribute_values(index, reversed_chart_list, attribute) if attribute != None else (reversed_chart_list[index], reversed_chart_list[index + 1])
          
            if self._is_down_trending(i, j):
                interval += 1
            else:
                return interval
        return interval
    

    