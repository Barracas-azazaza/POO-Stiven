from Person import Person
import datetime

class Trabajador(Person):
    __cargo: str
    def __init__(self, name_: str, lastName_: str, cargo_: str, fechaNac:datetime):
        Person.__init__(self, name_, lastName_, fechaNac)
        self.__cargo = cargo_
    def getCargo(self) -> None:
        return self.__cargo