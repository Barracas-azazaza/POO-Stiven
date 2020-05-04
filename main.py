from Trabajador import Trabajador
from ValidadorEdad import ValidadorEdad
import datetime

validador:ValidadorEdad=ValidadorEdad()
stiven: Trabajador = Trabajador("Stiven Ortlando", "Rojas", "Ing desarrollo", datetime.datetime(1985, 11, 19))
stiven.setEdad(validador.calcularEdad(stiven.getFechaNaci()))
print(stiven.getEdad())