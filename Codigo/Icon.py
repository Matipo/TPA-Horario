import datetime as dt
import requests
import flet as ft
#esta clase la usaremos para que me retorne el icono del url.
#creamos la clase imag y su constructor 
class imag:
    def __init__(self):
        pass

    # El método debe estar correctamente indentado dentro de la clase
    def getIcon(self):
        ciudad = "Puerto Montt"
        API_key = "a66802356fd01b8ac009b3b3b3a075f2"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&APPID={API_key}"
        response = requests.get(url).json()

        temp = response["weather"][0]["icon"] #especificamos los datos que queremos que nos devuelve el url, en este caso el icono.

        return temp # Devuelve el icono.
