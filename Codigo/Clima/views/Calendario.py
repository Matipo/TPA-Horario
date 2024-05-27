from flet import Page, Text, Button, Checkbox, Column, Container, colors, AlertDialog
from flet.utils import async_to_sync
from flet_route import Params, Basket, View

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

@async_to_sync
async def Calendario(page: Page, params=Params, basket=Basket):
    page.title = "Horario TPA"
    page.padding = 0
    page.window_width = 1200
    page.window_height = 1000
    page.window_resizable = False
    page.window_maximized = True

    eventos_semana = {dia: [] for dia in dias}

    def actualizar_eventos():
        for dia in dias:
            columnas_dia[dia].controls = [crear_contenedor_evento(evento) for evento in eventos_semana[dia]]
        page.update()

    def crear_contenedor_evento(evento):
        return Container(
            width=127,
            height=30,
            content=Text(evento, size=10, color=colors.WHITE),
            bgcolor=colors.TRANSPARENT,
            border="2px solid amber",
            alignment="center",
            border_radius=5,
            margin={"top": 5}
        )

    def closesave_dlg(e):
        evento = dlg_modal.content.controls[0].value  # Obtén el valor del input
        if c1.value:
            eventos_semana["Lunes"].append(evento)
            actualizar_eventos()
        dlg_modal.open = False

    def close_dlg(e):
        c1.value = False
        dlg_modal.open = False

    c1 = Checkbox(label=dias[0], value=False)

    dlg_modal = AlertDialog(
        title=Text("Add Evento"),
        content=Column(controls=[Text("Nombre del Evento:"), c1]),  # Agregar el input al diálogo
        actions=[
            Button("Save", on_click=closesave_dlg),
            Button("Cancel", on_click=close_dlg),
        ]
    )

    def open_dlg_modal(e):
        dlg_modal.open = True

    columnas_dia = {dia: Column() for dia in dias}

    def crear_columna_dia(nombre_dia):
        return Column(
            controls=[
                Container(
                    width=127,
                    height=55,
                    content=Text(nombre_dia, size=15),
                    bgcolor=colors.GREY_900,
                    alignment="center",
                    border_radius=10,
                ),
                columnas_dia[nombre_dia]
            ],
            spacing=5
        )

    diassemana = [crear_columna_dia(dia) for dia in dias]

    centro = Container(
        content=Column(
            controls=[
                Button(
                    "Evento",
                    color=colors.AMBER,
                    on_click=open_dlg_modal,
                    bgcolor=colors.GREY_800,
                    width=120,
                    height=40,
                    icon="add_circle"
                ),
                *diassemana
            ]
        ),
        width=1100,
        height=75,
        margin={"top": 10}
    )
    semanainfo = Container(
        content=Text("Semana", color=colors.AMBER, weight="500"),
        border_radius=10,
        bgcolor=colors.GREY_800,
        alignment="center"
    )
    superior = Container(content=semanainfo, width=1100, height=30, alignment="center", margin={"top": 10})
    objetos = Column(controls=[superior, centro])

    contenedor = Container(objetos, width=1200, height=1000, bgcolor=colors.GREEN, alignment="center")

    page.add(contenedor)
    
    # Aquí retornamos la vista que contiene todo el contenido que hemos creado
    return View(
        "/Calendario/:my_id"
    )


