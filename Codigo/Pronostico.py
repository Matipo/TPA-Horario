import datetime as dt
import requests


class pronostico:
    def __init__ (self):
        pass


    def getPronostico(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        pronost = response["daily"]["data"][0]["day"]
        pronost2 = response["daily"]["data"][0]["weather"]
        pronost3 = response["daily"]["data"][0]["summary"]
        pronost4 = response["daily"]["data"][0]["all_day"]["weather"]
        
        return f"Lunes\n{pronost}\n{pronost2}\n{pronost3}\n{pronost4}"
    
    def getTemperatura(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        temperatura = response["daily"]["data"][0]["all_day"]["temperature"]
        temperatura_min = response["daily"]["data"][0]["all_day"]["temperature_min"]
        temperatura_max = response["daily"]["data"][0]["all_day"]["temperature_max"]

        return f"La temperatura:\n{temperatura}\nla mínima:\n{temperatura_min}\nla máxima:\n{temperatura_max}"
    
    def getIconPronostico(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()

        iconPronost = response["daily"]["data"][0]["icon"]
        return iconPronost
    
    def getPronostico2(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        pronost = response["daily"]["data"][1]["day"]
        pronost2 = response["daily"]["data"][1]["weather"]
        pronost3 = response["daily"]["data"][1]["summary"]
        pronost4 = response["daily"]["data"][1]["all_day"]["weather"]
        
        return f"Martes\n{pronost}\n{pronost2}\n{pronost3}\n{pronost4}"
    
    def getTemperatura2(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        temperatura = response["daily"]["data"][1]["all_day"]["temperature"]
        temperatura_min = response["daily"]["data"][1]["all_day"]["temperature_min"]
        temperatura_max = response["daily"]["data"][1]["all_day"]["temperature_max"]

        return f"La temperatura:\n{temperatura}\nla mínima:\n{temperatura_min}\nla máxima:\n{temperatura_max}"
    
    def getPronostico3(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        pronost = response["daily"]["data"][2]["day"]
        pronost2 = response["daily"]["data"][2]["weather"]
        pronost3 = response["daily"]["data"][2]["summary"]
        pronost4 = response["daily"]["data"][2]["all_day"]["weather"]
        
        return f"Miercoles\n{pronost}\n{pronost2}\n{pronost3}\n{pronost4}"
    
    def getTemperatura3(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        temperatura = response["daily"]["data"][2]["all_day"]["temperature"]
        temperatura_min = response["daily"]["data"][2]["all_day"]["temperature_min"]
        temperatura_max = response["daily"]["data"][2]["all_day"]["temperature_max"]

        return f"La temperatura:\n{temperatura}\nla mínima:\n{temperatura_min}\nla máxima:\n{temperatura_max}"
    
    def getPronostico4(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        pronost = response["daily"]["data"][3]["day"]
        pronost2 = response["daily"]["data"][3]["weather"]
        pronost3 = response["daily"]["data"][3]["summary"]
        pronost4 = response["daily"]["data"][3]["all_day"]["weather"]
        
        return f"Jueves\n{pronost}\n{pronost2}\n{pronost3}\n{pronost4}"
    
    def getTemperatura4(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        temperatura = response["daily"]["data"][3]["all_day"]["temperature"]
        temperatura_min = response["daily"]["data"][3]["all_day"]["temperature_min"]
        temperatura_max = response["daily"]["data"][3]["all_day"]["temperature_max"]

        return f"La temperatura:\n{temperatura}\nla mínima:\n{temperatura_min}\nla máxima:\n{temperatura_max}"
    
    def getPronostico5(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        pronost = response["daily"]["data"][4]["day"]
        pronost2 = response["daily"]["data"][4]["weather"]
        pronost3 = response["daily"]["data"][4]["summary"]
        pronost4 = response["daily"]["data"][4]["all_day"]["weather"]
       
        return f"Viernes\n{pronost}\n{pronost2}\n{pronost3}\n{pronost4}"
    
    def getTemperatura5(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        temperatura = response["daily"]["data"][4]["all_day"]["temperature"]
        temperatura_min = response["daily"]["data"][4]["all_day"]["temperature_min"]
        temperatura_max = response["daily"]["data"][4]["all_day"]["temperature_max"]

        return f"La temperatura:\n{temperatura}\nla mínima:\n{temperatura_min}\nla máxima:\n{temperatura_max}" 
    
    def getPronostico6(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        pronost = response["daily"]["data"][5]["day"]
        pronost2 = response["daily"]["data"][5]["weather"]
        pronost3 = response["daily"]["data"][5]["summary"]
        pronost4 = response["daily"]["data"][5]["all_day"]["weather"]
       
        return f"Sabado\n{pronost}\n{pronost2}\n{pronost3}\n{pronost4}"
    
    def getTemperatura6(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        temperatura = response["daily"]["data"][5]["all_day"]["temperature"]
        temperatura_min = response["daily"]["data"][5]["all_day"]["temperature_min"]
        temperatura_max = response["daily"]["data"][5]["all_day"]["temperature_max"]

        return f"La temperatura:\n{temperatura}\nla mínima:\n{temperatura_min}\nla máxima:\n{temperatura_max}"
    
    def getPronostico7(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        pronost = response["daily"]["data"][6]["day"]
        pronost2 = response["daily"]["data"][6]["weather"]
        pronost3 = response["daily"]["data"][6]["summary"]
        pronost4 = response["daily"]["data"][6]["all_day"]["weather"]
       
        return f"Domingo\n{pronost}\n{pronost2}\n{pronost3}\n{pronost4}"
    
    def getTemperatura7(self):
        ciudad = "Puerto-Montt"
        API_key = "ta7h9vzcrny1rafc2u73ufzn592l64divhefox83"
        url = f"https://www.meteosource.com/api/v1/free/point?place_id={ciudad}&sections=all&timezone=UTC&language=en&units=metric&key={API_key}"
        response = requests.get(url).json()
        
        temperatura = response["daily"]["data"][6]["all_day"]["temperature"]
        temperatura_min = response["daily"]["data"][6]["all_day"]["temperature_min"]
        temperatura_max = response["daily"]["data"][6]["all_day"]["temperature_max"]

        return f"La temperatura:\n{temperatura}\nla mínima:\n{temperatura_min}\nla máxima:\n{temperatura_max}"