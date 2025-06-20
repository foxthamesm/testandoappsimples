import flet as ft

def main(page: ft.Page):
    page.title = "Upload de Arquivo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    file_name_text = ft.Text("Nenhum arquivo selecionado")
    upload_status_text = ft.Text("")
    uploaded_image = ft.Image(src="", width=300, height=300, fit=ft.ImageFit.CONTAIN, visible=False)

    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    def on_file_selected(e: ft.FilePickerResultEvent):
        if e.files:
            file = e.files[0]
            file_name_text.value = f"Arquivo selecionado: {file.name}"
            page.update()

            # Gera URL de upload no FastAPI
            upload_url = "https://api-flet.onrender.com/cadastrar_produto/"

            # Faz upload do arquivo usando o próprio Flet
            file_picker.upload(
                [ft.FilePickerUploadFile(file.name, upload_url, method="POST")]
            )

            

        else:
            file_name_text.value = "Nenhum arquivo selecionado"
            page.update()

    def on_upload_complete(e):
        upload_status_text.value = "✅ Upload concluído (verifique no servidor)!"
        page.update()

    file_picker.on_result = on_file_selected
    file_picker.on_upload_complete = on_upload_complete

    pick_file_button = ft.ElevatedButton(
        "Selecionar Arquivo",
        on_click=lambda _: file_picker.pick_files(allow_multiple=False)
    )

    page.add(
        pick_file_button,
        file_name_text,
        upload_status_text,
        uploaded_image
    )

ft.app(target=main, view=ft.WEB_BROWSER)
