import flet as ft
from flet import *
import pronostico, horario
from api import Tiempo


class UI:
    def __init__(self, page):
        self.page = page
        self.color_red = '#803D3B'
        self.Clima = Tiempo()
        self.temp = self.Clima.getTemp()
        self.img = self.Clima.getImg()
        self.hum = self.Clima.getHum()
        self.vie = self.Clima.getViento()
        

        


        self.navigation_rail = ft.NavigationRail(
            expand=True,
            bgcolor=self.color_red,
            selected_index=0,
            on_change=self.navigation_change,
            destinations=[
                ft.NavigationDestination(icon=ft.icons.HOME, label="Inicio"),
                ft.NavigationDestination(icon=ft.icons.LOCATION_ON_OUTLINED, label="Pronostico"),
                ft.NavigationDestination(icon=ft.icons.CALENDAR_MONTH_SHARP, label="Horario"),
                
            ]
        )
        

        self.navigation_container = ft.Container(
            col=1,
            bgcolor=self.color_red,
            border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        expand=True,
                        content=self.navigation_rail
                    ),
                    ft.Container(
                        expand=True,
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            expand=True,
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                
                            ]
                        )
                    )
                ]
            )
        )

        self.frame_2 = ft.Container(
            expand=True,
            content=self.get_page_content(0)
        )

        self.container = ft.Row(
            controls=[
                self.navigation_container,
                self.frame_2
            ],
            expand=True
        )

    def navigation_change(self, e):
        selected_index = e.control.selected_index
        self.frame_2.content = self.get_page_content(selected_index)
        self.page.update()

    def get_page_content(self, index):
        if index == 0:
            return ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        
                                        content=ft.Rive(
                                        "../images/clima.riv",
                                        
                                        ),
                                        expand=True,
                                                       
                                    ),
                                ],expand=True,
                                
                            ),
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                ft.Container(
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Icon("LOCATION_ON"),
                                                                    ft.Text("Puerto Montt",size=30)
                                                                ]
                                                            ),
                                                            ft.Image(
                                                                src=f"../images/{self.img}.png",  # Usa la URL para el icono
                                                                width=120,
                                                                height=120,
                                                            ),
                                                            ft.Text(f"{self.temp:.0f}°C",size=30),
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Icon('WATER'),
                                                                    ft.Text(f"{self.hum}%"),
                                                                    ft.Container(width=15),
                                                                    ft.Icon("WIND_POWER"),
                                                                    ft.Text(f"{self.vie:.0f} m/s")
                                                                ]
                                                            )
                                                        ],horizontal_alignment= ft.CrossAxisAlignment.CENTER
                                                    ),
                                                    padding=ft.padding.only(right=20,top=10,left=20,bottom=20),bgcolor='#423937',border_radius=35
                                                ),
                                            ],alignment=ft.MainAxisAlignment.END,
                                        )
                                    ),
                                    ft.Container(
                                        expand=True,
                                        
                                    )
                                ],alignment=ft.MainAxisAlignment.END,expand=True
                            )
                        ],expand=True
                    )
                ],expand=True
            )
        elif index == 1:
            main_page = pronostico.Pronostico() 
            return main_page.build(self.page)
        elif index == 2:
            calendario_page = horario.Calendario()
            
            return calendario_page.build(self.page)
    
   

    def build(self):
        return self.container

def main(page: ft.Page):
    page.window_maximized = True
    color_interfaz = '#AF8260'
    page.window_min_height = 820
    page.window_min_width = 1000
    
    page.bgcolor = '#322C2B'
    page.theme_mode = 'dark'
    page.theme = ft.Theme(
        color_scheme_seed=color_interfaz,
    )

    ui = UI(page)
    page.add(ui.build())

ft.app(main)
