import flet 
from flet import * 
#Unsere Datenbanken
import daten
from daten import data, speisedata, gerichte


def main(page: Page):
    page.title = "Gourmet Guide"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = "dark"  
 
    page.appbar1= flet.AppBar(
        title=Text('Home'), 
        bgcolor='black',
        center_title=False,
        actions=[
            ElevatedButton(text='Speisekammer', icon=icons.FOOD_BANK, on_click=lambda _:page.go('5'))
        ]

    )
    # ElevatedButtons für die untere Leiste
    btn_eigene_rezepte = ElevatedButton(text='Eigene Rezepte', icon=icons.ADD, on_click=lambda _: page.go('2'))
    btn_entdecken = ElevatedButton(text='Entdecken', icon=icons.EXPLORE, on_click=lambda _: page.go('3'))
    btn_gespeichert = ElevatedButton(text='Gespeichert', icon=icons.BOOKMARK, on_click=lambda _: page.go('4'))

    page.bottom_appbar= flet.BottomAppBar(
        bgcolor=flet.colors.BLACK12,
        shape=flet.NotchShape.CIRCULAR,
        content=flet.Row(
            controls=[
                btn_eigene_rezepte,
                btn_entdecken,
                btn_gespeichert,
            ]
        ),

    )

    
   
    #Container mit den Zutaten
    resultdata = ListView()

    resultcon = Container(
        #bgcolor="red200",
        bgcolor="grey850",
        padding=10,
        margin=10,
        offset=Offset(-2, 0), 
        animate_offset=Animation(600, curve="easeIn"),
        content=Column([
            resultdata

        ])
    )

    def searchnow(e):
        mysearch = e.control.value
        result = []

        if not mysearch == "":
            resultcon.visible = True
            for item in data:
                if mysearch in item['name']:
                    resultcon.offset = Offset(0, 0)  
                    result.append(item)
            page.update()

        if result:
            resultdata.controls.clear()
            print(f"Your result {result}")  
            for x in result:
                row_container = Row([
                    Text(f"Zutat : {x['name']} ", size=20, color="white"),
                    IconButton(icons.ADD_BOX_SHARP, on_click=lambda e, name=x['name']: add_to_inventory(name))
                ])
                resultdata.controls.append(row_container)
            page.update()

        else:
            resultcon.offset = Offset(-2, 0)  
            resultdata.controls.clear()
            page.update()

    resultcon.visible = False

    txtsearch = TextField(label="Suche", on_change=searchnow)

    page.add(
	Column([
	Text("Search Anything",size=30,weight="bold"),
	txtsearch,
	resultcon
	])
		)
    def add_to_inventory(name):
    # Hier fügen Sie das ausgewählte Nahrungsmittel zur Speisekammer hinzu
    # Zum Beispiel:
        print(f"Adding {name} to inventory")
    # Fügen Sie das ausgewählte Nahrungsmittel zur Inventartabelle hinzu und speichern Sie es






    #Die verschiedenen Seiten, wenn man etwas designen will, dann bei controls hinzufügen. Definieren muss man die Variblen außerhalb
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        page.views.append(

            View(
                route='1',
                controls=[
                    page.appbar1,
                    Text(value='Lebensmittel', size=30),
                    txtsearch,  
                    resultcon,  
                    page.bottom_appbar,
                ],

                vertical_alignment=MainAxisAlignment.START,
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
                    vertical_alignment=MainAxisAlignment.START,
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
                    vertical_alignment=MainAxisAlignment.START,
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
                    vertical_alignment=MainAxisAlignment.START,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26


                )
            )

        if page.route == '5':
            page.views.append(
                View(
                    route='5',
                    controls=[
                        AppBar(title=Text('Speisekammer'), bgcolor='black'),
                        Text(value='Hier sind alle deine Lebensmittel', size=30),
                        #ElevatedButton(text='Zurück', on_click=lambda _: page.go('1')),
                            
                        speisedata
                    ],
                      
                    vertical_alignment=MainAxisAlignment.START,
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
    app(target=main)
