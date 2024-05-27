from os import path
import flet as ft
from flet_route import Routing
from views.Menup import Menup 
def main(page: ft.Page, bgcolors=ft.colors.BLUE_400):

    app_routes=[

        path(url="/", view=Menup),
    ]

    Routing(page=page, app_routes=app_routes)

    page.go(page.route)

ft.app(target=main)