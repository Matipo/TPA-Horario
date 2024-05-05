import flet as ft
from datetime import datetime 
from Clima import temperatura_
from Icon import imag

class MainPage:
    def __init__(self):
          pass             

    def build(self, page: ft.Page):
        page.title = "Horario TPA"
        page.padding = 0
        page.window_width = 1200
        page.window_height = 1000
        page.window_resizable = True


    
        page.appbar = ft.AppBar(
        title=ft.Text("Horario", color=ft.colors.WHITE),
        center_title=True,
        automatically_imply_leading=False,
        )

        page.vertical_alignment = "start"

        temp_celsius = temperatura_()
        clima = temp_celsius.getClima()

        d = datetime.now()
        diasem = d.strftime("%A")
        mes = d.strftime("%B")
        year = d.strftime("%Y")

        if diasem == "Monday":
            diasem = "Lunes"
            dia1 = d.day
            dia2 = d.day +6 
        elif diasem == "Tuesday":
            diasem = "Martes"
            dia1 = d.day -1
            dia2 = d.day +5
        elif diasem == "Wednesday":
            diasem = "Miércoles"
            dia1 = d.day -2
            dia2 = d.day +4
        elif diasem == "Thursday":
            diasem = "Jueves"
            dia1 = d.day -3
            dia2 = d.day +3
        elif diasem == "Friday":
            diasem = "Viernes"
            dia1 = d.day -4
            dia2 = d.day +2
        elif diasem == "Saturday":
            iasem = "Sábado"
            dia1 = d.day -5
            dia2 = d.day +1
        elif diasem == "Sunday":
            diasem = "Domingo"
            dia1 = d.day -6
            dia2 = d.day 

        dias = ["Hora","Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
          
        user_input = ft.TextField(label="Ingresa nombre de evento", autofocus=True)
    
        semanainfo = ft.Container(width=500,height=40,
                     content=ft.Text(f"Semana {dia1} - {dia2} de {mes} {year}",color=ft.colors.TEAL_ACCENT_400,weight=ft.FontWeight.W_500),
                     border_radius=10,
                     bgcolor=ft.colors.TEAL_900,
                     alignment=ft.alignment.center,
                )
    
    #llamamos a la clase Icon para que nos devuelva el icono del clima de la ciudad.
        icon_clima = imag()
        icon = icon_clima.getIcon()

        if temp_celsius is not None:
        

            temp_clima = ft.Text(
                f"Puerto Montt  {clima:.2f}°C",
                color=ft.colors.TEAL_ACCENT_400,
                weight=ft.FontWeight.W_500,
                size=18,
            )
            icon_clima =ft.Image(
                src=f"http://openweathermap.org/img/wn/{icon}.png",  # Usa la URL para el icono
                width=30,
                height=30,
            )
            clima_contenedor = ft.Container(
                content=ft.Row([temp_clima, icon_clima], alignment=ft.MainAxisAlignment.CENTER ),  # Agrega ambos en un Row
                alignment=ft.alignment.top_right,
                border_radius=10,
                bgcolor=ft.colors.TEAL_900,
                padding=10,
                width = 400,
                height=60,
            )
            
        # Agregar el contenedor para el clima
            page.add(clima_contenedor)
            
            superior = ft.Container(content=semanainfo,alignment=ft.alignment.center,margin=ft.margin.only(top=10))
            page.add(superior)
            # Estructura para almacenar los eventos
            eventos_semana = {dia: [] for dia in dias}

            def actualizar_eventos():
                for dia in dias:
                    columnas_dia[dia].controls = [crear_contenedor_evento(evento) for evento in eventos_semana[dia]]
                    columnas_dia[dia].update()


            def crear_contenedor_evento(evento):
                return ft.Container(
                width=127,
                height=30,
                content=ft.Text(evento, size=10,color=ft.colors.WHITE),
            # Establece el color de fondo como transparente
                bgcolor=ft.colors.TRANSPARENT,
                border=ft.border.all(2,ft.colors.AMBER),
                alignment=ft.alignment.center,
                border_radius=5,
                margin=ft.margin.only(top=5)
            )
            def closesave_dlg(e):
                evento = user_input.value
                if evento != "":
                    if c1.value:
                        eventos_semana["Lunes"].append(evento)
                        actualizar_eventos()
                    if c2.value:
                        eventos_semana["Martes"].append(evento)
                        actualizar_eventos()
                    if c3.value:
                        eventos_semana["Miércoles"].append(evento)
                        actualizar_eventos()
                    if c4.value:
                        eventos_semana["Jueves"].append(evento)
                        actualizar_eventos()
                    if c5.value:
                        eventos_semana["Viernes"].append(evento)
                        actualizar_eventos()
                    if c6.value:
                        eventos_semana["Sábado"].append(evento)
                        actualizar_eventos()
                    if c7.value:
                        eventos_semana["Domingo"].append(evento)
                        actualizar_eventos()

                user_input.value = ""
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
        # Desmarca checkboxes
                c1.value = False
                dlg_modal.open = False
                page.update()
    
    # Checkboxes para los días
            c1 = ft.Checkbox(label=dias[1], value=False)
            c2 = ft.Checkbox(label=dias[2], value=False)
            c3 = ft.Checkbox(label=dias[3], value=False)
            c4 = ft.Checkbox(label=dias[4], value=False)
            c5 = ft.Checkbox(label=dias[5], value=False)
            c6 = ft.Checkbox(label=dias[6], value=False)
            c7 = ft.Checkbox(label=dias[7], value=False)

            dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Crear Evento"),
            content=ft.Column(controls=[
                user_input,
                c1,c2,c3,c4,c5,c6,c7,
            ]), 
            actions=[
                ft.TextButton("Guardar", on_click=closesave_dlg),
                ft.TextButton("Cancelar", on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
    
            def open_dlg_modal(e):
                page.dialog = dlg_modal
                dlg_modal.open = True
                page.update()
            
    # Creación de la columna hora y sus horas
            horas = [f"{hora:01d}:00" for hora in range(7, 24)]  # Desde las 7:00 hasta las 20:00
            def crear_contenedor_hora(hora):
                return ft.Container(
                    width=127,
                    height=30,
                    content=ft.Text(hora, size=10, color=ft.colors.WHITE),
                    bgcolor=ft.colors.TRANSPARENT,
                    border=ft.border.all(2, ft.colors.AMBER),
                    alignment=ft.alignment.center,
                    border_radius=5,
                    margin=ft.margin.only(top=5)
                )
            columna_horas = ft.Column(
                controls=[crear_contenedor_hora(hora) for hora in horas],
                spacing=5
            )


            columnas_dia = {dia: ft.Column() for dia in dias}
    
    # Función para crear la columna de cada día
            def crear_columna_dia(nombre_dia):
                return ft.Column(
                    controls=[
                        ft.Container(
                            width=127,
                            height=55,
                            content=ft.Text(nombre_dia, size=15),
                            bgcolor=ft.colors.BROWN_900,
                            alignment=ft.alignment.center,
                            border_radius=10,
                        ),
                        columnas_dia[nombre_dia],
                    ] + ([columna_horas] if nombre_dia == "Hora" else []),
                    spacing=5
                )
    
    # Crea las columnas de los días
            diassemana = [crear_columna_dia(dia) for dia in dias]
    
    # Contenedor central con los días y sus eventos
            centro = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Evento",
                            color=ft.colors.TEAL_ACCENT_400,
                            on_click=open_dlg_modal,
                            bgcolor=ft.colors.TEAL_900,
                            width=120,
                            height=50,
                            icon="add_circle",
                        ),
                        *diassemana
                    ]
                ),
                width=1100,
                height=75,
                alignment=ft.alignment.center
            )
    
    
            contenedor = ft.Container(centro,alignment=ft.alignment.top_center)
    
            page.update()
            page.add(contenedor)

          
       