import flet as ft
import os

UPLOAD_DIR = "uploads"

def main(page: ft.Page):

    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    info_text = ft.Text("Nenhum arquivo enviado ainda.")

    def on_upload_result(e: ft.FilePickerResultEvent):
        if e.files:
            file = e.files[0]

            # Salva o arquivo em disco
            file_path = os.path.join(UPLOAD_DIR, file.name)
            with open(file_path, "wb") as f:
                print(file.name)
                print(type(file))
                f.write(file)

            info_text.value = f"Upload concluído: {file.name}"
            page.update()

    file_picker = ft.FilePicker(on_result=on_upload_result)
    page.overlay.append(file_picker)

    upload_button = ft.ElevatedButton("Selecionar Arquivo", on_click=lambda _: file_picker.pick_files(allow_multiple=False))

    page.add(
        ft.Text("Upload de Arquivos no Render"),
        upload_button,
        info_text
    )

ft.app(target=main)
