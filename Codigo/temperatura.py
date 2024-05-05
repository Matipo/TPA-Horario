
#creamos esta clase para poder convertir la temperatura que nos entrega en Kelvin a Celsius
#creamos la clase celsius y su constructor
class celsius:
    def __init__(self, x):
        self.x = x

    #En este metodo retornamos el valor que pedimos - 275,15 para transformarlo a Celsius
    def celsius1(self):
        return self.x - 273.15  