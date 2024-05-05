import flet as ft
from mainPag import MainPage  # Asegúrate de que este archivo exista y tenga la clase MainPage

def main(page: ft.Page):
    # Configuración de la página principal
    page.title = "Menú TPA"
    page.horizontal_alignment = page.vertical_alignment = "center"
    page.window_width = 640
    page.window_height = 680
    page.window_resizable = False
    
    page.bgcolor = ft.colors.LIGHT_BLUE_100  # Color de fondo inicial
    
    # Configuración del AppBar
    page.appbar = ft.AppBar(
        title=ft.Text("Bienvenidos", color=ft.colors.WHITE),
        center_title=True,
        automatically_imply_leading=False,
    )

    def on_button_click(e):
        # Limpiar la página y reconstruirla
        page.clean()  # Limpia la página para nuevas estructuras
        
        # Construir la nueva página
        main_page = MainPage()  # Instancia la clase de la nueva página
        main_page.build(page)  # Llama a la función de construcción
        
        # Cambiar el color de fondo
        if page.bgcolor == ft.colors.LIGHT_BLUE_100:
            page.bgcolor = ft.colors.BLACK
        else:
            page.bgcolor = ft.colors.LIGHT_BLUE_100
        
        # Actualizar la página para reflejar los cambios
        page.update()

    # Botón para cambiar de página
    boton = ft.ElevatedButton(
        text="Ver calendario",
        on_click=on_button_click  # Vincula el clic con el evento que cambia la página
    )

    # Añadir el botón y otros elementos a la página
    page.add(ft.Text("Haga clic para ver el calendario"), boton)
    
    # Actualizar la página para reflejar los cambios
    page.update()

# Iniciar la aplicación
ft.app(target=main)

