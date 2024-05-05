
from temperatura import celsius  # importamos la clase del archivo temperatura para poder usar la funcion que me trasnforma los kelvin a Celsius.
import datetime as dt
import requests
import flet as ft

# declaramos la clase temperatura_ con su constructor.
class temperatura_:
    def __init__(self):
        pass

    #creamos el metodo getClima para que me pueda dar la información especifica del url.
    def getClima(self):
        ciudad = "Puerto Montt"
        API_key = "a66802356fd01b8ac009b3b3b3a075f2"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&APPID={API_key}"
        response = requests.get(url).json()
        
        temp = response["main"]["temp"] # llamamos los datos especificos que nos entrega el url
        temp_celsius = celsius(temp) #llamamos la funcion de celsius de la clase temperatura.

        return temp_celsius.celsius1()  # Devuelve la temperatura en Celsius

            


