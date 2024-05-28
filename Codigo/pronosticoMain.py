import flet as ft
from Pronostico import pronostico
import menu

class pronostMain:
    def __init__(self):
        pass

    def buildp(self, page: ft.Page):
        page.title = "Horario TPA"
        page.padding = 0
        page.window_width = 1200
        page.window_height = 1000
        page.window_resizable = True
        page.scroll = "auto"
        

        page.appbar = ft.AppBar(
            title=ft.Text("Pronostico de la semana", color=ft.colors.WHITE),
            center_title=True,
            automatically_imply_leading=False,
        )

        page.vertical_alignment = "start"

        # Crear el constructor para llamar la fecha
        pronost_tiempo = pronostico()
        pronost = pronost_tiempo.getPronostico()
        pronost2 = pronost_tiempo.getPronostico2()
        pronost3 = pronost_tiempo.getPronostico3()
        pronost4 = pronost_tiempo.getPronostico4()
        pronost5 = pronost_tiempo.getPronostico5()
        pronost6 = pronost_tiempo.getPronostico6()
        pronost7 = pronost_tiempo.getPronostico7()
        temperatura1 = pronost_tiempo.getTemperatura()
        temperatura2 = pronost_tiempo.getTemperatura2()
        temperatura3 = pronost_tiempo.getTemperatura3()
        temperatura4 = pronost_tiempo.getTemperatura4()
        temperatura5 = pronost_tiempo.getTemperatura5()
        temperatura6 = pronost_tiempo.getTemperatura6()
        temperatura7 = pronost_tiempo.getTemperatura7()

        # Crear el constructor para proporcionar el icono
        icon_tiempo = pronostico()
        iconP = icon_tiempo.getIconPronostico()

        def crear_contenedor(pronostico, icon, temperatura):
            return ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            f"Puerto Montt \n{pronostico}",
                            color='#ffffff',
                            weight=ft.FontWeight.W_500,
                            size=11,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Image(
                            src=f"https://www.meteosource.com/api/icons/{icon}.png",
                            width=30,
                            height=30,
                        ),
                        ft.Text(
                            f"{temperatura}",
                            color='#ffffff',
                            weight=ft.FontWeight.W_500,
                            size=11,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.top_left,
                border_radius=10,
                bgcolor='#AF8260',
                padding=10,
                width=170,
                height=400,
            )

        if pronost is not None and iconP is not None:
            pronostico_contenedor1 = crear_contenedor(pronost, iconP, temperatura1)
            pronostico_contenedor2 = crear_contenedor(pronost2, iconP, temperatura2)
            pronostico_contenedor3 = crear_contenedor(pronost3, iconP, temperatura3)
            pronostico_contenedor4 = crear_contenedor(pronost4, iconP, temperatura4)
            pronostico_contenedor5 = crear_contenedor(pronost5, iconP, temperatura5)
            pronostico_contenedor6 = crear_contenedor(pronost6, iconP, temperatura6)
            pronostico_contenedor7 = crear_contenedor(pronost7, iconP, temperatura7)

            fila_contenedores = ft.Row(
                [
                    pronostico_contenedor1, 
                    pronostico_contenedor2, 
                    pronostico_contenedor3, 
                    pronostico_contenedor4, 
                    pronostico_contenedor5,
                    pronostico_contenedor6,
                    pronostico_contenedor7,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=False  # Asegúrate de que la fila no se envuelva a la siguiente línea
            )

            def volver_al_menu(e):
                page.clean()
                menu.main(page)
                page.update()

            boton_volver = ft.ElevatedButton(
                text="volver al menu",
                on_click=volver_al_menu
            )

            page.add(boton_volver)
            page.add(fila_contenedores)