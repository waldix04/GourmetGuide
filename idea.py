# unterschiedliche Ideen, die wir noch benutzen könnten
import flet as ft
from flet import RouteChangeEvent, View, AppBar, Text, ElevatedButton, MainAxisAlignment, CrossAxisAlignment, ViewPopEvent

def main(page: ft.Page):
    page.title = "Gourmet Guide"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    first_name = ft.TextField(label="First name", autofocus=True)
    last_name = ft.TextField(label="Last name")
    greetings = ft.Column()

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        greetings,
    )

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    def route_change(e: RouteChangeEvent) -> None: 
        page.views.clear()
        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Home'), bgcolor='blue'),
                    Text(value='Home', size=30),
                    ElevatedButton(text='Go to store', on_click=lambda _: page.go('/store'))

                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
                

            )
        )
        if page.route == '/store':
            page.views.append(
            View(
                route='/store',
                controls=[
                    AppBar(title=Text('Store'), bgcolor='blue'),
                    Text(value='Store', size=30),
                    ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))

                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
                

            )
        )

    def view_pop(e: ViewPopEvent) -> None: 
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__': 
    ft.app(target=main)


#page.appbar = ft.AppBar(
        #title=ft.Text("Gourmet Guide"),
        #center_title=True,
        #bgcolor=ft.colors.BLACK)
