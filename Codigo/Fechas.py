from datetime import datetime

class fechas:
    def obtenerSemana():
        # Obtener el día y el mes
        fecha = datetime.now()
        diaSemana = fecha.strftime("%A")
        mes = fecha.strftime("%B")
        anio = fecha.strftime("%Y")

        # Determinar la cantidad de días en el mes
        if mes in [4, 6, 9, 11]:
            dias = 30
        elif mes == 2:
            # Verificar si el año es bisiesto
            if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
                dias = 29
            else:
                dias = 28
        else:
            dias = 31
        

        if fecha.month-1 in [4, 6, 9, 11]:
            diasMesAnterior = 30
        elif fecha.month-1 == 2:
            # Verificar si el año es bisiesto
            if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
                diasMesAnterior = 29
            else:
                diasMesAnterior = 28
        else:
            diasMesAnterior = 31


        if  diaSemana == "Monday":
            dia1 = fecha.day
            dia2 = fecha.day +6
            if dia2 > dias:
                dia2 = dia2-dias
        elif diaSemana == "Tuesday":
            dia1 = fecha.day-1
            dia2 = fecha.day+5
    
            if dia2> dias:
                dia2 = dia2-dias

        elif diaSemana == "Wednesday" :
            dia1 = fecha.day -2
            dia2 = fecha.day +4
            if dia1 < 1:
                dia1 = diasMesAnterior+dia1
        elif diaSemana == "Thursday" :
            dia1 = fecha.day -3
            dia2 = fecha.day +3
            if dia1 < 1:
                dia1 = diasMesAnterior+dia1
            
        elif diaSemana == "Friday":
            dia1 = fecha.day -4
            dia2 = fecha.day +2
            if dia1 < 1:
                dia1 = diasMesAnterior+dia1
            
        elif diaSemana == "Saturday":
            dia1 = fecha.day -5
            dia2 = fecha.day +1
            if dia1 < 1:
                dia1 = diasMesAnterior+dia1
        elif diaSemana == "Sunday":
            dia1 = fecha.day -6
            dia2 = fecha.day
            if dia1 < 1:
                dia1 = diasMesAnterior+dia1
        return dia1,dia2
    
    def getMes():
        fecha = datetime.now()
        return fecha.strftime("%B")
    def getAnio():
        fecha = datetime.now()
        return fecha.strftime("%Y")
    