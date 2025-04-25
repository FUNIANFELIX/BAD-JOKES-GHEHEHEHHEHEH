import flet as ft


POLAR_MORSECODE = {'P': 'C', 'C': 'P', 'O': 'E', 'E': 'O', 'L': 'N', 'N': 'L', 
                   'A': 'I', 'I': 'A', 'R': 'T', 'T': 'R'}

def main(page: ft.Page):
    page.title = "Guess that word!"
    page.window_width = 300
    page.window_height = 300

    text_visual = ft.TextField(label="Enter text", expand=True)
    result = ft.TextField(label="Result", expand=True)

    def encrypt_button_click(e):
    
        result = ''
        result.value = result
        page.update()

    def copy_to_clipboard(e):
        page.set_clipboard(result.value)
        page.update()

    button_encrypt = ft.ElevatedButton("Encrypt", on_click=encrypt_button_click)
    button_copy = ft.ElevatedButton("Copy", on_click=copy_to_clipboard)


ft.app(target=main)