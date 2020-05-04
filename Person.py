from ValidadorEdad import ValidadorEdad
import datetime

class Person:
    __name: str  # atributo privado
    __lastName: str  # atributo privado
    __edad: float=None
    __fechaNacimiento:datetime
    def __init__(self, name_: str, lastName_: str, fechaNac:datetime):
        self.__name = name_
        self.__lastName = lastName_
        self.__fechaNacimiento=fechaNac
    def getName(self)->str:
        return self.__name
    def setName(self, newName: str) -> None:
        self.__name = newName
    def getFechaNaci(self)->datetime:
        return self.__fechaNacimiento
    def setEdad(self, edad:float)->None:
        self.__edad=edad
    def getEdad(self)->float:
        return self.__edad