import flet as ft

def main(page: ft.Page):
    page.title = "Upload para o Google Drive"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    file_name_text = ft.Text("Nenhum arquivo selecionado")

    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    selected_file_path = ft.TextField(visible=False)

    def on_file_selected(e: ft.FilePickerResultEvent):
        if e.files:
            file = e.files[0]
            file_name_text.value = f"Arquivo selecionado: {file.name}"
            selected_file_path.value = file.path  # no modo web, isso não funcionará como em desktop
            page.update()

    file_picker.on_result = on_file_selected

    pick_file_button = ft.ElevatedButton(
        "Selecionar Arquivo",
        on_click=lambda _: file_picker.pick_files()
    )

    upload_button = ft.ElevatedButton(
        "Enviar para o Google Drive",
        on_click=lambda _: print("Implementar envio futuramente")
    )

    page.add(
        pick_file_button,
        file_name_text,
        upload_button
    )

ft.app(target=main, view=ft.WEB_BROWSER)
