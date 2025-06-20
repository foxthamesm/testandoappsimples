import flet as ft
import requests


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
            path = file.path
            #@app.post("/cadastrar_produto/")
            url = "https://api-flet.onrender.com/cadastrar_produto/"

            with open(path, 'rb') as f:
                files = {"arquivo": f}
                response = requests.post(url=url, files=files)

            if response.status_code:
                page.add(ft.Text(f"Codigo retornado: {response.json()}"))




    def on_upload_clicked(e):
        if upload_list:
            upload_status_text.value = "Enviando arquivo..."
            page.update()

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

    page.add()

ft.app(target=main, view=ft.WEB_BROWSER)
