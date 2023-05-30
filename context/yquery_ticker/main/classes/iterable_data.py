from abc import ABC
from dataclasses import is_dataclass
from context.yquery_ticker.main.const import INVALID_FIELD_STRING

from context.yquery_ticker.main.classes.castable_data import CastableDataInterface

"""
    This 'IterableDataInterface' makes it possible to more easily control the values
    being given to a data class and check for invalid values. Since data classes can 
    indefinetily nested inside other data classes, we need to make checking all the nested fields recursively. 
"""
SHOW_PRINT = False

class IterableDataInterface(ABC):

    def apply_local_rules(self):
        pass

    def cast_check(self: CastableDataInterface, field, value):
        field_type = self.__annotations__.get(field)
        if field_type is not isinstance(value, field_type):
            value = self.try_to_cast(field_type_name=field_type.__name__, value=value)
        return value

    def normalize_values(self):
        self.apply_local_rules()
        for field, value in self.__iter__():
            value:IterableDataInterface
            # This check for nested data classes and will perform
            # a recursive handling of null_values
            if is_dataclass(type(value)):
                value.normalize_values()
            else:     
                # Check for wrong types and cast if possible
                value = self.cast_check(field=field, value=value)

            # If any type of invalid values are given, we set a universal `None` value
            if value is None or value == "" or value == 'N/A':
                if SHOW_PRINT:
                    print(INVALID_FIELD_STRING.format(**{"%$FIELD%":field}))
                setattr(self, field, None)
            else:
                setattr(self, field, value)
        return self

    def __iter__(self):
        fields = [field for field in self.__dataclass_fields__.keys()]
        values = [getattr(self, field) for field in fields]
        return iter(zip(fields, values))