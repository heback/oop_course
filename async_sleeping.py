import asyncio
import flet as ft


async def main(page: ft.Page):
    async def button_click(e):
        await asyncio.sleep(1)
        await page.add_async(ft.Text("Hello!"))

    await page.add_async(
        ft.ElevatedButton("Say hello with delay!", on_click=button_click)
    )


ft.app(main)
