import flet as ft
import random

def main(page: ft.Page):
    page.title = "Bad Jokes Hahaha"
    page.padding = 20

    jokes = [
        "Why do monkeys share Amazon Prime accounts? Prime mates.",
        "Why did the chicken cross the road? To get to the other side.",
        "Why are the stairs so evil? They are always up to something.",
        "What's LeBron James' favorite salon? The Bronze Jade.",
        "¿Qué le dijo un taco al otro taco? Tacomo un poco raro tú.",
        "I would tell you a construction pun… but I’m still working on it.",
        "Why are vampires so sick? Because they are always coffin.",
        "What does a baby computer call its father? Data.",
        "Which knight invented King Arthur's Round Table? Sir Cumference.",
        "How can you find Will Smith in the snow? Follow the fresh prints."
    ]

    joke_text = ft.Text()

    def show_joke(e):
        joke_text.value = random.choice(jokes)
        sheet.open = True
        page.update()

    def close_joke(e):
        sheet.open = False
        page.update()

    sheet = ft.BottomSheet(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Here's a joke:"),
                joke_text,
                ft.ElevatedButton("Close", on_click=close_joke)
            ]),
            padding=20
        ),
        open=False
    )

    joke_button = ft.ElevatedButton("Tell me a joke", on_click=show_joke)

    page.add(joke_button)
    page.overlay.append(sheet)

ft.app(target=main)
#(i really wanted to put in the whole shrek 3 script but failed and got a 1k errors and it wont apply to the freaking comment, yes it was funny for no reason)
#padding link on flet i forgo to put in https://flet.dev/docs/reference/types/padding/ how i learn to use padding a bit more

