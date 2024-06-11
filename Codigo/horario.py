import flet as ft

class Calendario:
    def __init__(self):
        self.actividades = {}  # Diccionario para almacenar las actividades
        self.botones = {}  # Diccionario para almacenar los botones de actividad

    def build(self, page):
        days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        hours = [f"{i}:00" for i in range(8, 24)]  # Horas de 8 AM a 11 PM

        grid = ft.Column(expand=True)
        
        # Botón para agregar actividad
        add_activity_button = ft.TextButton(
            icon=ft.icons.ADD,
            text="Evento",
            on_click=lambda e: self.open_add_activity_dialog(page),
            width=110,
        )

        # Crear la cabecera de días
        header_row = ft.Row(
            controls=[add_activity_button] + [ft.Container(ft.Text(day, weight="bold"), width=200, alignment=ft.alignment.center, border_radius=10, bgcolor='#803D3B', padding=5) for day in days]
        )
        grid.controls.append(header_row)

        rows = []
        
        # Crear las filas de horas y celdas de actividades
        for hour in hours:
            hour_row = ft.Row(
                controls=[ft.Container(ft.Text(hour, weight="bold"), width=110, alignment=ft.alignment.center)]
            )
            for day in days:
                activity_key = f"{day}_{hour}"
                activity_button = ft.TextButton(
                    text="",
                    visible=False,
                    on_click=lambda e, k=activity_key: self.open_edit_activity_dialog(page, k)
                )
                self.botones[activity_key] = activity_button  # Almacenar el botón para referencia posterior
                hour_row.controls.append(
                    ft.Container(
                        content=activity_button,
                        border_radius=5,
                        border=ft.border.all(1, "black"),
                        padding=5,
                        width=200,
                        height=50
                    )
                )
            rows.append(hour_row)
        
        grid.controls.extend(rows)

        # Campo de entrada para el cuadro de diálogo
        self.add_dialog_input = ft.TextField(label="Actividad", autofocus=True)
        self.add_dialog_hour = ft.Dropdown(label="Hora", options=[ft.dropdown.Option(f"{i}:00") for i in range(8, 24)])
        self.add_dialog_days = [ft.Checkbox(label=day) for day in days]

        # Crear el cuadro de diálogo para agregar el contenido del cuadrado
        self.add_dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Agregar actividad"),
            content=ft.Column(controls=[self.add_dialog_input, self.add_dialog_hour] + self.add_dialog_days),
            actions=[
                ft.IconButton(icon=ft.icons.SAVE, on_click=self.save_new_activity),
                ft.IconButton(icon=ft.icons.CANCEL, on_click=self.cancel_add)
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

        # Campo de entrada para el cuadro de diálogo de edición
        self.edit_dialog_input = ft.TextField(label="Actividad", autofocus=True)

        # Crear el cuadro de diálogo para modificar el contenido del cuadrado
        self.edit_dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Modificar actividad"),
            content=self.edit_dialog_input,
            actions=[
                ft.IconButton(icon=ft.icons.SAVE, on_click=self.save_content),
                ft.IconButton(icon=ft.icons.DELETE, on_click=self.delete_content),
                ft.IconButton(icon=ft.icons.CANCEL, on_click=self.cancel_edit)
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

        # Envolver el grid en un ListView para la barra de desplazamiento vertical
        scrollable_grid = ft.ListView(
            expand=True,
            controls=[grid]
        )

        return scrollable_grid

    # Función para abrir el cuadro de diálogo para agregar actividad
    def open_add_activity_dialog(self, page):
        self.current_key = None
        self.add_dialog_input.value = ""
        self.add_dialog_hour.value = None
        for checkbox in self.add_dialog_days:
            checkbox.value = False
        page.dialog = self.add_dlg_modal
        self.add_dlg_modal.open = True
        page.update()

    # Función para abrir el cuadro de diálogo para modificar el contenido
    def open_edit_activity_dialog(self, page, key):
        self.current_key = key
        self.edit_dialog_input.value = self.actividades.get(key, "")
        page.dialog = self.edit_dlg_modal
        self.edit_dlg_modal.open = True
        page.update()

    # Función para guardar el contenido del cuadro al agregar nueva actividad
    def save_new_activity(self, e):
        new_content = self.add_dialog_input.value
        selected_hour = self.add_dialog_hour.value
        selected_days = [checkbox.label for checkbox in self.add_dialog_days if checkbox.value]

        for day in selected_days:
            key = f"{day}_{selected_hour}"
            self.actividades[key] = new_content
            button = self.botones[key]
            button.text = new_content
            button.visible = True
            button.update()  # Actualizar visualmente el botón

        self.add_dlg_modal.open = False
        e.page.update()

    # Función para guardar el contenido del cuadro
    def save_content(self, e):
        if self.current_key:
            new_content = self.edit_dialog_input.value
            self.actividades[self.current_key] = new_content
            button = self.botones[self.current_key]
            button.text = new_content
            button.visible = True
            button.update()  # Actualizar visualmente el botón

        self.edit_dlg_modal.open = False
        e.page.update()

    # Función para eliminar el contenido del cuadro
    def delete_content(self, e):
        if self.current_key:
            if self.current_key in self.actividades:
                del self.actividades[self.current_key]
            button = self.botones[self.current_key]
            button.text = ""
            button.visible = False
            button.update()  # Actualizar visualmente el botón

        self.edit_dlg_modal.open = False
        e.page.update()

    # Función para cancelar la adición de actividad
    def cancel_add(self, e):
        self.add_dialog_input.value = ""
        self.add_dlg_modal.open = False
        e.page.update()

    # Función para cancelar la edición
    def cancel_edit(self, e):
        self.edit_dialog_input.value = ""
        self.edit_dlg_modal.open = False
        e.page.update()

