import flet as ft


def main(page: ft.Page):
    page.add(ft.Text(f"Initial Toute: {page.route}"))

    def route_change(route):
        page.add()


    page.on_route_change = route_change


ft.app(target = main)