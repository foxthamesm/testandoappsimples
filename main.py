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

    selected_file = None  # Armazena o arquivo selecionado

    def on_file_selected(e: ft.FilePickerResultEvent):
        nonlocal selected_file
        if e.files:
            file = e.files[0]
            file_name_text.value = f"Arquivo selecionado: {file.name}"
            page.update()

            if file.bytes:
                selected_file = file  # Guarda o arquivo para envio posterior
            else:
                page.add(ft.Text("❌ O arquivo não tem bytes disponíveis. Verifique o picker!"))
        else:
            file_name_text.value = "Nenhum arquivo selecionado"
            page.update()

    def on_upload_clicked(e):
        if selected_file and selected_file.bytes:
            upload_status_text.value = "Enviando arquivo..."
            page.update()

            # Monta o payload do arquivo
            arquivo_payload = {
                'arquivo': (selected_file.name, selected_file.bytes, 'application/octet-stream')
            }
            url = "https://api-flet.onrender.com/cadastrar_produto/"

            response = requests.post(url, files=arquivo_payload)

            if response.ok:
                upload_status_text.value = "✅ Upload concluído com sucesso!"
                result = response.json()
                uploaded_image.src = result.get("url", "")
                uploaded_image.visible = True
            else:
                upload_status_text.value = f"❌ Erro no upload: {response.status_code} - {response.text}"
                uploaded_image.visible = False

            page.update()
        else:
            upload_status_text.value = "Por favor, selecione um arquivo antes de enviar."
            page.update()

    file_picker.on_result = on_file_selected

    pick_file_button = ft.ElevatedButton(
        "Selecionar Arquivo",
        on_click=lambda _: file_picker.pick_files(read_bytes=True)  # <- Aqui é fundamental!
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
