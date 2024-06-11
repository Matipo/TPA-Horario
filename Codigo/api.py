import requests

class Tiempo:
    def __init__(self):
        self.API_KEY = '778bf151ef8594ccfef82a4423a4002c'
        self.city = 'Puerto Montt'

    def getImg(self):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&APPID={self.API_KEY}"
        response = requests.get(url).json()
        imagen = response["weather"][0]["main"]
        return imagen
    
    def getTemp(self):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.API_KEY}&units=metric"
        response = requests.get(url).json()
        temp = response["main"]["temp"]
        return temp

    def getHum(self):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.API_KEY}&units=metric"
        response = requests.get(url).json()
        humedad = response["main"]["humidity"]
        return humedad

    def getViento(self):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.API_KEY}&units=metric"
        response = requests.get(url).json()
        viento = response["wind"]["speed"]
        return viento