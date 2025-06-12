import flet as ft
import os

def main(page: ft.Page):
    page.title = "Testando"

    text = ft.TextField(label='Say anything:')
    show_text = ft.Text(value=' ')

    def on_change_text(e):
        show_text.value = text.value
        page.update()

    content_to_show = ft.Container(
        content=ft.Column(
            controls=[
                text,
                ft.ElevatedButton(text='Click Here', on_click=on_change_text),
                show_text
            ]
        ),
        visible=True
    )

    page.add(content_to_show)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    ft.app(target=main, port=port, view=ft.WEB_BROWSER)
