import flet as ft
from flet import RouteChangeEvent, View, AppBar, Text, ElevatedButton, MainAxisAlignment, CrossAxisAlignment, ViewPopEvent, TextField, NavigationBar, ListView, Container, transform, Offset, Column, Animation


def main(page: ft.Page):
    page.title = "Gourmet Guide"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    
    def route_change(e: RouteChangeEvent) -> None: 
        page.views.clear()
        page.views.append(

            View(
                route='1',
                controls=[
                    AppBar(title=Text('Home'), bgcolor='black'),
                    Text(value='Lebensmittel', size=30),
                    ft.TextField(hint_text="Was hast du noch in der Vorratskammer?", expand=True),
                    ElevatedButton(text='Eigene Rezepte', on_click=lambda _: page.go('2')),
                    ElevatedButton(text='Entdecken', on_click=lambda _: page.go('3')),
                    ElevatedButton(text='Gespeichert', on_click=lambda _: page.go('4')),

                ],
                         
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
                
                )
            )
        
        
        if page.route == '2':
            page.views.append(
            View(
                route='2',
                controls=[
                    AppBar(title=Text('Eigene Rezepte'), bgcolor='black'),
                    Text(value='Deine eigenen Rezepte', size=30),
                    ElevatedButton(text='Zurück', on_click=lambda _: page.go('1'))

                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
                

            )
        )
            

        if page.route == '3':
            page.views.append(
            View(
                route='3',
                controls=[
                    AppBar(title=Text('Entdecken'), bgcolor='black'),
                    Text(value='Diese Rezepte könnten dir gefallen', size=30),
                    ElevatedButton(text='Zurück', on_click=lambda _: page.go('1'))

                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
                

            )
        )

        if page.route == '4':
            page.views.append(
            View(
                route='4',
                controls=[
                    AppBar(title=Text('Gespeichert'), bgcolor='black'),
                    Text(value='Deine gespeicherten Rezepte', size=30),
                    ElevatedButton(text='Zurück', on_click=lambda _: page.go('1'))

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