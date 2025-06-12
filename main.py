import flet as ft
import os

# Define a pasta de upload
UPLOAD_DIR = "uploads"

def main(page: ft.Page):

    # Garante que a pasta exista (tanto local quanto no Render)
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    progress = ft.ProgressBar(width=400)
    info_text = ft.Text("Nenhum arquivo enviado ainda.")

    # Função para acompanhar o progresso de upload
    def on_upload_progress(e: ft.FilePickerUploadEvent):
        progress.value = e.progress
        page.update()

    # Quando o arquivo for selecionado
    def on_upload_result(e: ft.FilePickerResultEvent):
        if e.files:
            file = e.files[0]
            info_text.value = f"Enviando: {file.name}"

            # Cria a URL temporária para o upload
            file_path = os.path.join(UPLOAD_DIR, file.name)
            upload_url = page.get_upload_url(file_path, 600)

            # Inicia o upload
            file_picker.upload(
                [(file, upload_url)],
                on_upload_progress=on_upload_progress
            )
            page.update()
            info_text.value = f"Upload concluído: {file.name}"
            page.update()

    # Configuração do file picker
    file_picker = ft.FilePicker(on_result=on_upload_result)
    page.overlay.append(file_picker)

    upload_button = ft.ElevatedButton("Selecionar Arquivo", on_click=lambda _: file_picker.pick_files(allow_multiple=False))

    # Adiciona os componentes na página
    page.add(
        ft.Text("Upload de Arquivos no Render"),
        upload_button,
        progress,
        info_text
    )

ft.app(target=main)
