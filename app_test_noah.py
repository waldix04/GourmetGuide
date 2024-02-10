import flet 
from flet import * 
from flet import app


def main(page: Page):
    page.title = "Gourmet Guide"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = "dark"  

    # ElevatedButtons für die untere Leiste
    btn_eigene_rezepte = ElevatedButton(text='Eigene Rezepte', icon=icons.ADD, on_click=lambda _: page.go('2'))
    btn_entdecken = ElevatedButton(text='Entdecken', icon=icons.EXPLORE, on_click=lambda _: page.go('3'))
    btn_gespeichert = ElevatedButton(text='Gespeichert', icon=icons.BOOKMARK, on_click=lambda _: page.go('4'))

    # Container für die untere Leiste (um den grauen Hintergrund zu erzeugen)
    bottom_bar = Container(
        content=Row([btn_eigene_rezepte, btn_entdecken, btn_gespeichert], alignment='space-between'),
        #Position Bottom?? Wie kriegt man das hin
        #bgcolor='gray',
        #width='100%',
        #padding=100,
        #alignment= 'bottom_center',
        #bottom=0
    )

    
    data = [
        {"name": "Mehl"},
        {"name": "Zucker"},
        {"name": "Butter"},
        {"name": "Eier"},
        {"name": "Vanillezucker"},
        {"name": "Backpulver"},
        {"name": "Salz"},
        {"name": "Milch"},
        {"name": "Schokoladenstückchen"},
        {"name": "gehackte Nüsse"},
        {"name": "Haferflocken"},
        {"name": "Rosinen"},
        {"name": "Zimt"},
        {"name": "Vanilleextrakt"},
        {"name": "Rindfleisch"},
        {"name": "Hühnchen"},
        {"name": "Lachs"},
        {"name": "Schweinefleisch"},
        {"name": "Rucola"},
        {"name": "Spinat"},
        {"name": "Kopfsalat"},
        {"name": "Tomaten"},
        {"name": "Gurken"},
        {"name": "Karotten"},
        {"name": "Zwiebeln"},
        {"name": "Knoblauch"},
        {"name": "Kartoffeln"},
        {"name": "Paprika"},
        {"name": "Champignons"},
        {"name": "Brokkoli"},
        {"name": "Blumenkohl"},
        {"name": "Sellerie"},
        {"name": "Zucchini"},
        {"name": "Mais"},
        {"name": "Erbsen"},
        {"name": "Bohnen"},
        {"name": "Linsen"},
        {"name": "Quinoa"},
        {"name": "Reis"},
        {"name": "Nudeln"},
        {"name": "Brot"},
        {"name": "Joghurt"},
        {"name": "Käse"},
        {"name": "Olivenöl"},
        {"name": "Essig"},
        {"name": "Senf"},
        {"name": "Sojasauce"}
    ]

    resultdata = ListView()

    resultcon = Container(
        bgcolor="red200",
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
                resultdata.controls.append(
                    Text(f"name : {x['name']} ",
                         size=20, color="white"

                         )

                )
            page.update()

        else:
            resultcon.offset = Offset(-2, 0)  
            resultdata.controls.clear()
            page.update()

    resultcon.visible = False

    txtsearch = TextField(label="Search now", on_change=searchnow)

    page.add(
	Column([
	Text("Search Anything",size=30,weight="bold"),
	txtsearch,
	resultcon
	])
		)

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        page.views.append(

            View(
                route='1',
                controls=[
                    AppBar(title=Text('Home'), bgcolor='black'),
                    Text(value='Lebensmittel', size=30),
                    txtsearch,  # Search-TextField hinzugefügt
                    resultcon,  # Ergebnis-Container hinzugefügt
                    bottom_bar,
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
    app(target=main)
