import flet as ft

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

async def main(page:ft.Page):
    # Propiedades de la página
    page.title = "Horario TPA"
    page.padding = 0
    page.window_width = 1200
    page.window_height = 1000
    page.window_resizable = True
    page.window_maximized = False
    page.window_maximizable = False

    user_input = ft.TextField(label="Ingresa nombre de evento", autofocus=True)
    
    semanainfo = ft.Container(width=500,height=40,
                     content=ft.Text("Semana",color=ft.colors.TEAL_ACCENT_400,weight=ft.FontWeight.W_500),
                     border_radius=10,
                     bgcolor=ft.colors.TEAL_900,
                     alignment=ft.alignment.center,
                )
    
    superior = ft.Container(content=semanainfo,alignment=ft.alignment.center,margin=ft.margin.only(top=10))
    page.add(superior)
    # Estructura para almacenar los eventos
    eventos_semana = {dia: [] for dia in dias}
    
    # Función para actualizar la visualización de los eventos
    def actualizar_eventos():
        for dia in dias:
            columnas_dia[dia].controls = [crear_contenedor_evento(evento) for evento in eventos_semana[dia]]
            columnas_dia[dia].update()
    
    # Función para crear el contenedor de un evento
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
    
    # Función que se llama cuando se guarda un evento
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
        

        # Resetea el valor al original
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
    c1 = ft.Checkbox(label=dias[0], value=False)
    c2 = ft.Checkbox(label=dias[1], value=False)
    c3 = ft.Checkbox(label=dias[2], value=False)
    c4 = ft.Checkbox(label=dias[3], value=False)
    c5 = ft.Checkbox(label=dias[4], value=False)
    c6 = ft.Checkbox(label=dias[5], value=False)
    c7 = ft.Checkbox(label=dias[6], value=False)
    
    # Ventana emergente para agregar eventos
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Add Evento"),
        content=ft.Column(controls=[
            user_input,
            c1,c2,c3,c4,c5,c6,c7,
        ]), 
        actions=[
            ft.TextButton("Save", on_click=closesave_dlg),
            ft.TextButton("Cancel", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
    
    # Diccionario para almacenar las columnas de cada día
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
                columnas_dia[nombre_dia]  # Agrega la columna de eventos para el día
            ],
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
    
ft.app(target=main)

#ft.app(port=8550, target=main)
