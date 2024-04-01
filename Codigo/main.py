import flet as ft
from flet import *
from datetime import datetime

#Muestra semana de lunes a domingo
d = datetime.now()
dia = d.strftime("%A")
mes = d.strftime("%B")
year = d.strftime("%Y")

if dia == "Monday":
    dia = "Lunes"
    dia1 = d.day
    dia2 = d.day +6 
elif dia == "Tuesday":
    dia = "Martes"
    dia1 = d.day -1
    dia2 = d.day +5
elif dia == "Wednesday":
    dia = "Miércoles"
    dia1 = d.day -2
    dia2 = d.day +4
elif dia == "Thursday":
    dia = "Jueves"
    dia1 = d.day -3
    dia2 = d.day +3
elif dia == "Friday":
    dia = "Viernes"
    dia1 = d.day -4
    dia2 = d.day +2
elif dia == "Saturday":
    dia = "Sábado"
    dia1 = d.day -5
    dia2 = d.day +1
elif dia == "Sunday":
    dia = "Domingo"
    dia1 = d.day -6
    dia2 = d.day 



def main(page: ft.Page):
    #Nombre de ventana
    page.title = "TPA Horario"
    # Definir los días de la semana y las actividades diarias
    dias = ["","Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    
    #Crear item
    def ite(ite):
        ite = []
        ite.append(
            ft.Container(
                        content=ft.Text(value=str(f"Semana {dia1} - {dia2} {mes} {year}")),
                        alignment=ft.alignment.center,
                        width=300,
                        height=30,
                        bgcolor=ft.colors.ORANGE_800,
                        border_radius=ft.border_radius.all(5),
            )  
        )
        return ite
    #Para mostrar la fila
    row1 = ft.Row(controls=ite(0), alignment=ft.MainAxisAlignment.CENTER)
    page.add(row1)
    #Crea los cuadros para los dias de la semana
    def items(i):
        items = []
        
        for i in dias:
            
            if i=="":
                items.append(
                    ft.Container(
                        content=ft.Text(value=str(i)),
                        alignment=ft.alignment.center,
                        width=100,
                        height=50,
                        
                        border_radius=ft.border_radius.all(5),
                    )    )
            else:
                if i == dia:
                    items.append(
                    ft.Container(
                    
                        content=ft.Text(value=str(i)),
                        alignment=ft.alignment.center,
                        width=100,
                        height=50,
                        bgcolor=ft.colors.TEAL,
                        border_radius=ft.border_radius.all(5),
                    ))
                else:
                    items.append(
                    ft.Container(
                    
                        content=ft.Text(value=str(i)),
                        alignment=ft.alignment.center,
                        width=100,
                        height=50,
                        bgcolor=ft.colors.GREEN_700,
                        border_radius=ft.border_radius.all(5),
                    ))
                
                    
                    
        return items
    row = ft.Row(spacing=10, controls=items(10))
    page.add(row)
    
    

    # Actualizar la página para mostrar los cambios
    page.update()

if __name__ == '__main__':
    ft.app(target=main)
