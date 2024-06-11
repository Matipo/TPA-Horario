import flet as ft
import requests

class Pronostico:
    def __init__(self):
        self.API_KEY = '1x8puwibcez794mfjrzr4x4nhrn3odokuqeq8rj7'
        self.city = 'Puerto-Montt'
        self.url = f"https://www.meteosource.com/api/v1/free/point?place_id={self.city}&sections=all&timezone=UTC&language=en&units=metric&key={self.API_KEY}"
        self.color_bg = '#423937'

    def getPronostico(self,x):
        response = requests.get(self.url).json()
        clima = response["daily"]["data"][x]["weather"]
        temp_min = response["daily"]["data"][x]["all_day"]["temperature_min"]
        temp_max = response["daily"]["data"][x]["all_day"]["temperature_max"]
        viento = response["daily"]["data"][x]["all_day"]["wind"]["speed"]
        precipitacion = response["daily"]["data"][x]["all_day"]["precipitation"]["total"]
        img = response["daily"]["data"][x]["icon"]
        

        list = [clima,temp_min,temp_max,viento,precipitacion,img]

        return list

    def build(self, page):
        a = Pronostico()
        
        mi_lista = a.getPronostico(x=0)
        mi_lista1 = a.getPronostico(x=1)
        mi_lista2 = a.getPronostico(x=2)
        mi_lista3 = a.getPronostico(x=3)
        mi_lista4 = a.getPronostico(x=4)
        mi_lista5 = a.getPronostico(x=5)
        mi_lista6 = a.getPronostico(x=6)

        
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(padding=ft.padding.all(40),content=ft.Column(controls=[
                            ft.Text("Lunes",size=25,weight=ft.FontWeight.BOLD),
                            ft.Image(src=f"../images/{mi_lista[5]}.png",width=100,height=100),
                            ft.Text(f"{mi_lista[0]}",size=15),
                            ft.Row(controls=[
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista[1]:.0f}°C")
                                    ]),
                                    ft.Row(controls=[
                                        ft.Icon('WATER_DROP'),
                                        ft.Text(f"{mi_lista[4]:.0f}"),
                                    ],)
                                ]),
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista[2]:.0f}°C")
                                        ]),
                                    ft.Row(controls=[
                                        ft.Icon('WIND_POWER'),
                                        ft.Text(f"{mi_lista[3]:.0f}m/s")
                                        ])
                                ])
                            ])
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER),bgcolor=self.color_bg,border_radius=35
                        ),
                        ft.Container(padding=ft.padding.all(40),content=ft.Column(controls=[
                            ft.Text("Martes",size=25,weight=ft.FontWeight.BOLD),
                            ft.Image(src=f"../images/{mi_lista1[5]}.png",width=100,height=100),
                            ft.Text(f"{mi_lista1[0]}",size=15),
                            ft.Row(controls=[
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista1[1]:.0f}°C")
                                    ]),
                                    ft.Row(controls=[
                                        ft.Icon('WATER_DROP'),
                                        ft.Text(f"{mi_lista1[4]:.0f}"),
                                    ],)
                                ]),
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista1[2]:.0f}°C")
                                        ]),
                                    ft.Row(controls=[
                                        ft.Icon('WIND_POWER'),
                                        ft.Text(f"{mi_lista1[3]:.0f}m/s")
                                        ])
                                ])
                            ])
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER),bgcolor=self.color_bg,border_radius=35
                        ),
                        ft.Container(padding=ft.padding.all(40),content=ft.Column(controls=[
                            ft.Text("Miércoles",size=25,weight=ft.FontWeight.BOLD),
                            ft.Image(src=f"../images/{mi_lista2[5]}.png",width=100,height=100),
                            ft.Text(f"{mi_lista2[0]}",size=15),
                            ft.Row(controls=[
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista2[1]:.0f}°C")
                                    ]),
                                    ft.Row(controls=[
                                        ft.Icon('WATER_DROP'),
                                        ft.Text(f"{mi_lista2[4]:.0f}"),
                                    ],)
                                ]),
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista2[2]:.0f}°C")
                                        ]),
                                    ft.Row(controls=[
                                        ft.Icon('WIND_POWER'),
                                        ft.Text(f"{mi_lista2[3]:.0f}m/s")
                                        ])
                                ])
                            ])
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER),bgcolor=self.color_bg,border_radius=35
                        ),
                        ft.Container(padding=ft.padding.all(40),content=ft.Column(controls=[
                            ft.Text("Jueves",size=25,weight=ft.FontWeight.BOLD),
                            ft.Image(src=f"../images/{mi_lista3[5]}.png",width=100,height=100),
                            ft.Text(f"{mi_lista3[0]}",size=15),
                            ft.Row(controls=[
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista3[1]:.0f}°C")
                                    ]),
                                    ft.Row(controls=[
                                        ft.Icon('WATER_DROP'),
                                        ft.Text(f"{mi_lista3[4]:.0f}"),
                                    ],)
                                ]),
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista3[2]:.0f}°C")
                                        ]),
                                    ft.Row(controls=[
                                        ft.Icon('WIND_POWER'),
                                        ft.Text(f"{mi_lista3[3]:.0f}m/s")
                                        ])
                                ])
                            ])
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER),bgcolor=self.color_bg,border_radius=35
                        ),
                        ft.Container(padding=ft.padding.all(40),content=ft.Column(controls=[
                            ft.Text("Viernes",size=25,weight=ft.FontWeight.BOLD),
                            ft.Image(src=f"../images/{mi_lista4[5]}.png",width=100,height=100),
                            ft.Text(f"{mi_lista4[0]}",size=15),
                            ft.Row(controls=[
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista4[1]:.0f}°C")
                                    ]),
                                    ft.Row(controls=[
                                        ft.Icon('WATER_DROP'),
                                        ft.Text(f"{mi_lista4[4]:.0f}"),
                                    ],)
                                ]),
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista4[2]:.0f}°C")
                                        ]),
                                    ft.Row(controls=[
                                        ft.Icon('WIND_POWER'),
                                        ft.Text(f"{mi_lista4[3]:.0f}m/s")
                                        ])
                                ])
                            ])
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER),bgcolor=self.color_bg,border_radius=35
                        ),
                        ft.Container(padding=ft.padding.all(40),content=ft.Column(controls=[
                            ft.Text("Sábado",size=25,weight=ft.FontWeight.BOLD),
                            ft.Image(src=f"../images/{mi_lista5[5]}.png",width=100,height=100),
                            ft.Text(f"{mi_lista5[0]}",size=15),
                            ft.Row(controls=[
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista5[1]:.0f}°C")
                                    ]),
                                    ft.Row(controls=[
                                        ft.Icon('WATER_DROP'),
                                        ft.Text(f"{mi_lista5[4]:.0f}"),
                                    ],)
                                ]),
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista5[2]:.0f}°C")
                                        ]),
                                    ft.Row(controls=[
                                        ft.Icon('WIND_POWER'),
                                        ft.Text(f"{mi_lista5[3]:.0f}m/s")
                                        ])
                                ])
                            ])
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER),bgcolor=self.color_bg,border_radius=35
                        ),
                        ft.Container(padding=ft.padding.all(40),content=ft.Column(controls=[
                            ft.Text("Domingo",size=25,weight=ft.FontWeight.BOLD),
                            ft.Image(src=f"../images/{mi_lista6[5]}.png",width=100,height=100),
                            ft.Text(f"{mi_lista6[0]}",size=15),
                            ft.Row(controls=[
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista6[1]:.0f}°C")
                                    ]),
                                    ft.Row(controls=[
                                        ft.Icon('WATER_DROP'),
                                        ft.Text(f"{mi_lista6[4]:.0f}"),
                                    ],)
                                ]),
                                ft.Column(controls=[
                                    ft.Row(controls=[
                                        ft.Icon('THERMOSTAT'),
                                        ft.Text(f"{mi_lista6[2]:.0f}°C")
                                        ]),
                                    ft.Row(controls=[
                                        ft.Icon('WIND_POWER'),
                                        ft.Text(f"{mi_lista6[3]:.0f}m/s")
                                        ])
                                ])
                            ])
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER),bgcolor=self.color_bg,border_radius=35
                        ),
                        
                    ]
                )
            ]
        )
