"""
    This 'CastableDataInterface' makes it possible to check if it is possible to
    cast values when needed. It is handy if we use data that don't entirely conform to the class types
    from a JSON object to populate the class fields.
      
    If a class field takes a 'float' and a JSON object provides a an 'int', by casting it to the 
    correct type, we might avoid unexpected bugs related to wrong types when executing the software.

    If the value is not castable, it will return None
"""
from config import CASTABLE_DATA_SHOW_DEBUG_PRINT
from context.yquery_ticker.main.const import (
    CASTABLE_ERROR_STRING,
    NO_CASTABLE_DEFINITION_ERROR_STRING
)


class CastableDataInterface:

    @staticmethod
    def _cast(field_type_name, value, cast):
        try:
            return cast(value)
        except (ValueError, TypeError) as e:
            if CASTABLE_DATA_SHOW_DEBUG_PRINT:
                print(f'_cast with cast value {cast} threw an exception: {e}')
                print(CASTABLE_ERROR_STRING.format(value=value, field_type=field_type_name))

    def try_to_cast(self, field_type_name, underlying_type, value):
        if field_type_name == "float" or underlying_type == "float":
            return self._cast(field_type_name=field_type_name, value=value, cast=float)
        elif field_type_name == 'int':
            return self._cast(field_type_name=field_type_name, value=value, cast=int)
        elif field_type_name == 'str':
            return self._cast(field_type_name=field_type_name, value=value, cast=str)
        else:
            if CASTABLE_DATA_SHOW_DEBUG_PRINT:
                print(NO_CASTABLE_DEFINITION_ERROR_STRING.format(field_type=field_type_name))
