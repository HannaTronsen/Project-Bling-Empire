import dataclasses
import math
from abc import ABC
from dataclasses import is_dataclass
from config import ITERABLE_DATA_SHOW_DEBUG_PRINT
from context.yquery_ticker.main.interfaces.castable_data import CastableDataInterface
from context.yquery_ticker.main.const import INVALID_FIELD_STRING

"""
    This 'IterableDataInterface' makes it possible to more easily control the values
    being given to a data class and check for invalid values. Since data classes can 
    indefinitely nested inside other data classes, we need to make checking all the nested fields recursively. 
"""


@dataclasses.dataclass
class IterableDataInterface(ABC):

    def __init__(self):
        self.__dataclass_fields__ = None

    def apply_local_rules(self):
        pass

    def cast_check(self: CastableDataInterface, field, value):
        field_type = self.__annotations__.get(field)
        if field_type is not isinstance(value, field_type):
            # Only relevant if we deal with Optional type
            underlying_type = None
            if hasattr(field_type, '__args__') and field_type.__args__:
                underlying_type = field_type.__args__[0].__name__
            return self.try_to_cast(
                field_type_name=field_type.__name__,
                underlying_type=underlying_type,
                value=value,
            )

    def normalize_values(self):
        self.apply_local_rules()
        for field, value in self.__iter__():
            value: IterableDataInterface
            # This check for nested data classes and will perform
            # a recursive handling of null_values
            if is_dataclass(type(value)):
                value.normalize_values()
            else:
                if type(value) in {int, float, str, bool, type(None)}:
                    # Check for wrong types and cast if possible
                    value = self.cast_check(field=field, value=value)

            # If any type of invalid values are given, we set a universal `None` value
            if value is None or value == "" or value == 'N/A' or isinstance(value, float | int) and math.isnan(value):  # type: ignore
                if ITERABLE_DATA_SHOW_DEBUG_PRINT:
                    print(INVALID_FIELD_STRING.format(field=field))
                setattr(self, field, None)
            else:
                setattr(self, field, value)
        return self

    def __iter__(self):
        fields = [field for field in self.__dataclass_fields__.keys()]
        values = [getattr(self, field) for field in fields]
        return iter(zip(fields, values))
