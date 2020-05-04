import datetime

class ValidadorEdad():
    def __init__(self):
        pass
    def adultoJoven(self, edad: float) -> bool:
        if edad >= 18 and edad <= 35:
            return True
        else:
            return False
    def calcularEdad(self, fechaNac_:datetime)->float:
            now:datetime = datetime.datetime.today()
            delta:datetime.timedelta=now-fechaNac_
            days:float=delta.days
            return days/365.25