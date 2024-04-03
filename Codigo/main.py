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
    #Días de la semana
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    page.update()
    
    #Crear item

    semanainf = [
        ft.Container(
            content=ft.Text(f"Semana {dia1} - {dia2} {mes} {year}",color=ft.colors.WHITE),
                        alignment=ft.alignment.center,
                        width=300,
                        height=30,
                        bgcolor=ft.colors.DEEP_ORANGE_300,
                        border_radius=ft.border_radius.all(5),
        )
    ]
    rowinf = ft.Row(controls=[*semanainf],alignment=ft.MainAxisAlignment.CENTER)
  
    #Crea los container para los dias de la semana
    rowz = [
        ft.Container(
           content=ft.Text(i,color=ft.colors.WHITE),
            alignment=ft.alignment.center,
            width=100,
            height=50,
            bgcolor=ft.colors.BLUE_900,
            border_radius=ft.border_radius.all(5), 
        )for i in dias
    ]

    #-------------------- Boton ADD EVENT ----------------------
    #La funcion de cerrar tambien comprueba si la checkbox esta marcada y la devuelve a su estado de desmarcada
    def closesave_dlg(e):

        print(user_input.value)

        user_input.value = ""

        if c1.value == True:
            print("Lunes")
        if c2.value == True:
            print("Martes")
        if c3.value == True:
            print("Miercoles")
        if c4.value == True:
            print("Jueves")
        if c5.value == True:
            print("Viernes")
        if c6.value == True:
            print("Sabado")
        if c7.value == True:
            print("Domingo")
    
        c1.value = False
        c2.value = False
        c3.value = False
        c4.value = False
        c5.value = False
        c6.value = False
        c7.value = False

        dlg_modal.open = False
        page.update()
    
    def close_dlg(e):
        #Desmarca checkboxes
        c1.value = False
        c2.value = False
        c3.value = False
        c4.value = False
        c5.value = False
        c6.value = False
        c7.value = False

        dlg_modal.open = False
        page.update()

    #El input para ingresar nombre
    user_input = ft.TextField(label="Ingresa nombre de evento",autofocus=True)

    #Checkboxes
    c1 = ft.Checkbox(label=dias[0],value=False)
    c2 = ft.Checkbox(label=dias[1],value=False)
    c3 = ft.Checkbox(label=dias[2],value=False)
    c4 = ft.Checkbox(label=dias[3],value=False)
    c5 = ft.Checkbox(label=dias[4],value=False)
    c6 = ft.Checkbox(label=dias[5],value=False)
    c7 = ft.Checkbox(label=dias[6],value=False)

    #Propiedades de la ventana emergente y lo que muestra
    dlg_modal = ft.AlertDialog(
        modal=True,

        title=ft.Text("Add Element"),
        content=ft.Column(controls=[
            user_input,
            c1,c2,c3,c4,c5,c6,c7
        ]),
        actions=[
            ft.TextButton("Save",on_click=closesave_dlg,),
            ft.TextButton("Cancel", on_click=close_dlg),
        ],
        
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()


    row_dias = ft.Row(
        controls=[
            ft.ElevatedButton(
                "Evento", 
                on_click=open_dlg_modal,
                bgcolor=ft.colors.DEEP_ORANGE_300,
                width=117,
                height=40,
                icon="add_circle"
                ),
           *rowz
        ],
        alignment="center",
        spacing=10,
    )

    page.add(rowinf,row_dias)

    # Actualizar la página para mostrar los cambios
    page.update()

if __name__ == '__main__':
    ft.app(target=main)
