# unterschiedliche Ideen, die wir noch benutzen könnten
import flet as ft
from typing import Any, List, Optional, Union
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue
# Waldi testes hier importe um auf andere seiten zu kommmen!
from flet import RouteChangeEvent,ViewPopEvent,CrossAxisAlignment,MainAxisAlignment
from flet import View,Page,AppBar,ElevatedButton,Text
from flet import RouteChangeEvent, View, AppBar, Text, ElevatedButton, MainAxisAlignment, CrossAxisAlignment, ViewPopEvent, TextField

def main(page: ft.Page):
    page.title = "Gourmet Guide"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    first_name = ft.TextField(label="First name", autofocus=True)
    last_name = ft.TextField(label="Last name")
    greetings = ft.Column()

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)


 




# Titel der App oben links 
        #Homepage
def main(page: ft.Page):   
    page.title = "Gourmet Guide"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    '''Hier versuche ich ,das wenn man auf einen icon klickt das er die "Seite" wechselt. 
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        page.views.append(
            View(
                route='/',
                controls=[Appbar(title=Text('Entdecken'),bgcolor='Black'),
                Text(value='Entdecken',size=30),
                ElevatedButton(text='Go to Entdecken', on_click=lambda _: page.go('/Entdecken'))
                ],
            )
        )
'''





    def route_change(e: RouteChangeEvent) -> None: 
        page.views.clear()
        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Home'), bgcolor='blue'),
                    Text(value='Home', size=30),
                    ElevatedButton(text='Go to store', on_click=lambda _: page.go('/store'))
                    
                                ],)
        )
    def build(self):
       

        return ft.Column(
            width=600,
            controls=[
                ft.Row([ ft.Text(value="Lebensmittel", style="headlineMedium")], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    controls=[
                        self.new_meal,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.meals,
            ],
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
