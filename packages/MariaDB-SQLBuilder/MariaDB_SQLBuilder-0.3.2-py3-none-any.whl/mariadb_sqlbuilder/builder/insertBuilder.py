import abc
from typing import Union

from ..execution import executeFunctions
from .baseBuilder import BaseBuilder


# get the name of a table column
def _getTCN(table: str, column: str) -> str:
    return table + "." + column


class InsertBuilder(BaseBuilder):

    def __init__(self, tb):
        super().__init__(tb)
        self.__ignore = False
        self.__toSet = {}

    def set(self, column, value: Union[str, int, None]):
        if isinstance(value, int):
            self.__toSet[column] = f"{str(value)}"
        elif value is None:
            self.__toSet[column] = f"NULL"
        else:
            self.__toSet[column] = f"'{str(value)}'"
        return self

    def ignore(self, _ignore: bool = True):
        self.__ignore = _ignore
        return self

    def execute(self) -> bool:
        cursor = self.tb.connect.getAvailableCursor()
        result = executeFunctions.execute(
            cursor,
            self.get_sql()
        )
        self.tb.connect.makeCursorAvailable(cursor)
        return result

    def where(self, **kwargs):
        raise NameError("Function 'where' is not in use here")

    def get_sql(self) -> str:
        return f"INSERT {'IGNORE ' if self.__ignore else ''}INTO " \
            f"{self.tb.table} ({', '.join(self.__toSet.keys())}) VALUES ({', '.join(self.__toSet.values())})"

