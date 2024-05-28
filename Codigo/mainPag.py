import flet as ft
from Clima import temperatura_
from Icon import imag
import menu
from Fechas import fechas
import re

class MainPage:
    def __init__(self):
        pass

    def build(self, page: ft.Page):
        page.title = "Horario TPA"
        page.padding = 0
        page.window_width = 1200
        page.window_height = 1000
        page.window_resizable = True
        page.scroll = "auto"

        page.appbar = ft.AppBar(
            title=ft.Text("Horario", color=ft.colors.WHITE),
            center_title=True,
            automatically_imply_leading=False,
        )

        page.vertical_alignment = "start"

        temp_celsius = temperatura_()
        clima = temp_celsius.getClima()

        dia1, dia2 = fechas.obtenerSemana()
        mes = fechas.getMes()
        year = fechas.getAnio()

        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        
        user_input = ft.TextField(label="Ingresa nombre de evento", autofocus=True)
        hora_input = ft.TextField(label="Ingresa la hora (HH:MM)", autofocus=True)
        error_message = ft.Text(value="", color="red")

        semanainfo = ft.Container(
            width=500, height=40,
            content=ft.Text(f"Semana {dia1} - {dia2} de {mes} {year}", color='#E4C59E', weight=ft.FontWeight.W_500),
            border_radius=10,
            bgcolor='#AF8260',
            alignment=ft.alignment.center,
        )

        icon_clima = imag()
        icon = icon_clima.getIcon()

        if temp_celsius is not None:
            temp_clima = ft.Text(
                f"Puerto Montt  {clima:.2f}°C",
                color='#E4C59E',
                weight=ft.FontWeight.W_500,
                size=18,
            )
            icon_clima = ft.Image(
                src=f"http://openweathermap.org/img/wn/{icon}.png",  # Usa la URL para el icono
                width=30,
                height=30,
            )
            clima_contenedor = ft.Container(
                content=ft.Row([temp_clima, icon_clima], alignment=ft.MainAxisAlignment.CENTER),  # Agrega ambos en un Row
                alignment=ft.alignment.top_right,
                border_radius=10,
                bgcolor='#AF8260',
                padding=10,
                width=400,
                height=60,
            )
            page.add(clima_contenedor)
            
            superior = ft.Container(content=semanainfo, alignment=ft.alignment.center, margin=ft.margin.only(top=10))
            page.add(superior)

            def volver_al_menu(e):
                page.clean()
                menu.main(page)
                page.update()
                
            boton_volver = ft.ElevatedButton(
                text="volver al menu",
                on_click=volver_al_menu
            )
            page.add(boton_volver)

            eventos_semana = {dia: [] for dia in dias}

            def actualizar_eventos():
                for dia in dias:
                    columnas_dia[dia].controls = [crear_contenedor_evento(evento, dia) for evento in eventos_semana[dia]]
                    columnas_dia[dia].update()

            def crear_contenedor_evento(evento, dia):
                evento_button = ft.ElevatedButton(
                    f"{evento[1]} - {evento[0]}",
                    bgcolor='#ffffff',
                    on_click=lambda e: editar_evento(evento, dia)
                )
                return evento_button

            def editar_evento(evento, dia):
                dlg_modal.title = ft.Text("Editar Evento")  # Cambiar título del diálogo
                user_input.value = evento[1]  # Establecer el nombre del evento en el campo de entrada
                hora_input.value = evento[0]  # Establecer la hora del evento en el campo de entrada
                page.editing_event = evento
                page.editing_day = dia
                dlg_modal.open = True  # Abrir la ventana de edición de eventos al hacer clic en el evento
                page.update()

            def validar_hora(hora):
                patron = re.compile(r"^([01]\d|2[0-3]):([0-5]\d)$")
                return patron.match(hora) is not None

            def closesave_dlg(e):
                evento = user_input.value
                hora = hora_input.value  # Obtener la hora ingresada
                if not validar_hora(hora):
                    error_message.value = "Por favor, ingrese la hora en el formato HH:MM (24 horas)."
                    page.update()
                    return

                error_message.value = ""  # Limpiar el mensaje de error
                if evento != "":
                    # Eliminar el evento antiguo si estamos en modo de edición
                    if hasattr(page, 'editing_event') and hasattr(page, 'editing_day'):
                        eventos_semana[page.editing_day].remove(page.editing_event)
                        del page.editing_event
                        del page.editing_day

                    if cboxes[0].value:
                        eventos_semana["Lunes"].append((hora, evento))
                    if cboxes[1].value:
                        eventos_semana["Martes"].append((hora, evento))
                    if cboxes[2].value:
                        eventos_semana["Miércoles"].append((hora, evento))
                    if cboxes[3].value:
                        eventos_semana["Jueves"].append((hora, evento))
                    if cboxes[4].value:
                        eventos_semana["Viernes"].append((hora, evento))
                    if cboxes[5].value:
                        eventos_semana["Sábado"].append((hora, evento))
                    if cboxes[6].value:
                        eventos_semana["Domingo"].append((hora, evento))

                    # Ordenar los eventos por hora
                    for dia in dias:
                        eventos_semana[dia].sort(key=lambda x: x[0])  # Ordenar por la primera entrada (hora)

                    actualizar_eventos()

                user_input.value = ""
                hora_input.value = ""  # Limpiar el campo de entrada de hora
                # Desmarca checkboxes
                for cbox in cboxes:
                    cbox.value = False

                dlg_modal.open = False
                page.update()

            def close_dlg(e):
                hora_input.value = ""  # Limpiar el campo de entrada de hora
                user_input.value = ""
                # Desmarca checkboxes
                for cbox in cboxes:
                    cbox.value = False
                dlg_modal.open = False
                page.update()

            # Checkboxes para los días
            cboxes = []
            for i in dias:
                cbox = ft.Checkbox(label=i, value=False)
                cboxes.append(cbox)

            dlg_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text("Crear Evento"),
                content=ft.Column(controls=[
                    user_input,
                    hora_input,
                    error_message,  # Añadir el mensaje de error aquí
                    *cboxes  # Desempaquetar la lista de checkboxes
                ]), 
                actions=[
                    ft.TextButton("Guardar", on_click=closesave_dlg),
                    ft.TextButton("Cancelar", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )

            columnas_dia = {dia: ft.Column() for dia in dias}

            def open_dlg_modal(e):
                dlg_modal.title = ft.Text("Crear Evento")  # Cambiar título del diálogo
                page.dialog = dlg_modal
                dlg_modal.open = True
                page.update()

            def crear_columna_dia(nombre_dia):
                return ft.Column(
                    controls=[
                        ft.Container(
                            width=127,
                            height=55,
                            content=ft.Text(nombre_dia, size=15),
                            bgcolor='#803D3B',
                            alignment=ft.alignment.center,
                            border_radius=10,
                        ),
                        columnas_dia[nombre_dia],
                    ]
                )

            diassemana = [crear_columna_dia(dia) for dia in dias]

            centro = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Evento",
                            color='#E4C59E',
                            on_click=open_dlg_modal,
                            bgcolor='#AF8260',
                            width=120,
                            height=50,
                            icon="add_circle",
                        ),
                        *diassemana  # Desempaquetar la lista de columnas de días
                    ]
                ),
                width=1100,
                alignment=ft.alignment.center,
            )

            contenedor = ft.Container(centro, alignment=ft.alignment.top_center)

            page.add(contenedor)
            page.update()
            scroll = ft.ScrollMode

