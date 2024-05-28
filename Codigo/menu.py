import flet as ft

#from mainPag import MainPage  # Asegúrate de que este archivo exista y tenga la clase MainPage
import mainPag
from pronosticoMain import pronostMain

def main(page: ft.Page):
    # Configuración de la página principal
    page.title = "Menú TPA"
    page.horizontal_alignment = page.vertical_alignment = "center"
    page.window_width = 640
    page.window_height = 680
    page.window_resizable = False
    page.bgcolor='#322C2B'
    
    
    # Configuración del AppBar
    page.appbar = ft.AppBar(
        title=ft.Text("Bienvenidos", color=ft.colors.WHITE, size=40, weight=ft.FontWeight.W_900),
        center_title=True,
        automatically_imply_leading=False,
    )

    def on_button_click(e):
        # Limpiar la página y reconstruirla
        page.clean()  # Limpia la página para nuevas estructuras
        
        # Construir la nueva página
        main_page = mainPag.MainPage()  # Instancia la clase de la nueva página
        main_page.build(page)  # Llama a la función de construcción
        
        
        # Actualizar la página para reflejar los cambios
        page.update()

    # Botón para cambiar de página
    boton = ft.ElevatedButton(
        text="Ver calendario",
        on_click=on_button_click  # Vincula el clic con el evento que cambia la página
    )

    def on_button_click2(e):
        # Limpiar la página y reconstruirla
        page.clean()  # Limpia la página para nuevas estructuras
        
        # Construir la nueva página
        main_page2 = pronostMain()  # Instancia la clase de la nueva página
        main_page2.buildp(page)  # Llama a la función de construcción
        
        # Actualizar la página para reflejar los cambios
        page.update()

    boton2 = ft.ElevatedButton(
        text = "Ver pronostico del tiempo",
        on_click=on_button_click2
    )

    # Añadir el botón y otros elementos a la página
    page.add(ft.Text("Haga clic para ver el calendario", size=15, color=ft.colors.BLUE, weight=ft.FontWeight.BOLD), boton, boton2)
    
    # Actualizar la página para reflejar los cambios
    page.update()

# Iniciar la aplicación
ft.app(target=main)