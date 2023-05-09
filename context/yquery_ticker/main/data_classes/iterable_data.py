from abc import ABC
from dataclasses import is_dataclass

"""
    This 'IterableDataInterface' makes it possible to more easily control the values
    being given to a data class and check for invalid values. Since data classes can 
    indefinetily nested inside other data classes, we need to make checking all the nested fields recursively. 
"""
SHOW_PRINT = True
class IterableDataInterface(ABC):
    
    def handle_null_values(self):
        controlled_values = {}
        for field, value in self.__iter__():
            #This check for nested data classes and will perform
            #a recursive handling of null_values
            if is_dataclass(value):
                value.handle_null_values()

            #If any type of invalid values are given, we set a universal `None` value
            if value is None or value == "" or value == 'N/A':
                if SHOW_PRINT:
                    print(f'\n {field} has invalid or null value and will be handled')
                controlled_values[field] = None
            else:
                controlled_values[field] = value
        return self.__class__(**controlled_values)
   
    def __iter__(self):
        fields = [field for field in self.__dataclass_fields__.keys()]
        values = [getattr(self, field) for field in fields]
        return iter(zip(fields, values))