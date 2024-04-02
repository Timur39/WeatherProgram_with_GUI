import flet as ft
import time
from weather import weather


def main(page: ft.Page):
    def back(e):
        page.clean()
        page.add(ft.Row(controls=[
            ft.Text(f'Погода', size=45)
        ]),
            ft.Row(controls=[
                txt_city,
                button
            ]),
        )
        page.update()

    def button_clicked(e):
        try:
            if not txt_city.value:
                txt_city.error_text = 'Please enter city'
                page.update()
            else:
                city = txt_city.value
                page.clean()
                page.add(ft.Text(f"Погода в городе {city.upper()}: {weather(city)}", size=20))
                page.add(ft.ElevatedButton(text='Назад', on_click=back))
                txt_city.error_text = None
        except:
            page.clean()
            page.add(ft.Row(controls=[
                ft.Text(f'Погода', size=45)
            ]),
                ft.Row(controls=[
                    txt_city,
                    button
                ]),
            )
            page.update()
            txt_city.error_text = 'Please enter city'

    page.window_width = 550
    page.window_height = 400
    page.window_resizable = False
    txt_city = ft.TextField(label="Город")
    button = ft.ElevatedButton(text='Узнать', on_click=button_clicked)

    page.add(ft.Row(controls=[
        ft.Text(f'Погода', size=45)
    ]),
        ft.Row(controls=[
            txt_city,
            button
        ]),
    )


if __name__ == '__main__':
    ft.app(target=main)
