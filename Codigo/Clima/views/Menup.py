import flet as ft
from flet_route import Params, Basket
from views.Calendario import Calendario



def Menup(page: ft.Page, params: Params, basket: Basket):
    page.window_width = 720
    page.window_height = 1280 
    page.window_resizable = False
    page.padding = 0

    print(params)

    send_your_params="menu"

    # Definición correcta de la vista
    return ft.View(
        "/",
        controls=[
            ft.FilledButton(text="Crear Agenda", on_click=lambda _: page.go("/Calendario/10")), 
            ft.FilledButton(text="Ver clima", url="https://www.meteored.cl/tiempo-en_Puerto+Montt-America+Sur-Chile-Los+Lagos-SCTE-1-18567.html")
        ]
    )

ft.app(target=Menup)
