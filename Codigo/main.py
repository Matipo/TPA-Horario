import flet as ft

def main(page: ft.Page):
    # Definir los días de la semana y las actividades diarias
    dias = ["","Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    actividades = {
        "Lunes": ["Trabajo", "Gimnasio", "Estudio"],
        "Martes": ["Trabajo", "Clases de baile", "Estudio"],
        "Miércoles": ["Trabajo", "Gimnasio", "Estudio"],
        "Jueves": ["Trabajo", "Clases de baile", "Estudio"],
        "Viernes": ["Trabajo", "Gimnasio", "Estudio"],
        "Sábado": ["Descanso", "Paseo", "Cine"],
        "Domingo": ["Descanso", "Familia", "Preparación para la semana"]
    }
    #Crea los cuadros para los dias de la semana
    def items(i):
        items = []
        for i in dias:
            if i=="":
                items.append(
                    ft.Container(
                        content=ft.Text(value=str(i)),
                        alignment=ft.alignment.center,
                        width=100,
                        height=50,
                        bgcolor=ft.colors.TRANSPARENT,
                        border_radius=ft.border_radius.all(5),
                    )    )
            else:
                
                items.append(
                    ft.Container(
                    
                        content=ft.Text(value=str(i)),
                        alignment=ft.alignment.center,
                        width=100,
                        height=50,
                        bgcolor=ft.colors.GREEN,
                        border_radius=ft.border_radius.all(5),
                    ))
                    
        return items
    row = ft.Row(spacing=10, controls=items(10))
    page.add(row)

    

    # Actualizar la página para mostrar los cambios
    page.update()

ft.app(target=main)
