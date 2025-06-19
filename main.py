import flet as ft

def main(page: ft.Page):
    page.title = "Upload de Arquivo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    file_name_text = ft.Text("Nenhum arquivo selecionado")
    upload_status_text = ft.Text("")
    uploaded_image = ft.Image(src="", width=300, height=300, fit=ft.ImageFit.CONTAIN, visible=False)

    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    upload_list = []
    uploaded_url = ""

    def on_file_selected(e: ft.FilePickerResultEvent):
        nonlocal uploaded_url
        if e.files:
            file = e.files[0]
            file_name_text.value = f"Arquivo selecionado: {file.name}"

            # Gera URL temporária para upload
            username = "usuario_demo"
            upload_url = page.get_upload_url(f"/{username}/uploads/{file.name}", 600)

            upload_list.clear()
            upload_list.append(
                ft.FilePickerUploadFile(
                    file.name,
                    upload_url=upload_url
                )
            )

            uploaded_url = upload_url
            page.update()

    def on_upload_clicked(e):
        if upload_list:
            upload_status_text.value = "Enviando arquivo..."
            page.update()
            file_picker.upload(upload_list)
        else:
            file_name_text.value = "Por favor, selecione um arquivo antes de enviar."
            page.update()

    def on_upload_complete(e):
        upload_status_text.value = "✅ Upload concluído com sucesso!"

        # Se for imagem, exibe na tela
        file_name = upload_list[0].name.lower()
        if file_name.endswith((".png", ".jpg", ".jpeg", ".gif")):
            uploaded_image.src = upload_list[0].upload_url
            uploaded_image.visible = True
        else:
            uploaded_image.visible = False

        page.update()

    file_picker.on_result = on_file_selected
    file_picker.on_upload_complete = on_upload_complete

    pick_file_button = ft.ElevatedButton(
        "Selecionar Arquivo",
        on_click=lambda _: file_picker.pick_files()
    )

    upload_button = ft.ElevatedButton(
        "Enviar para o servidor",
        on_click=on_upload_clicked
    )

    page.add(
        pick_file_button,
        file_name_text,
        upload_button,
        upload_status_text,
        uploaded_image
    )

ft.app(target=main, view=ft.WEB_BROWSER)
