import flet
from flet import *
# Unsere Datenbanken
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

    bottom_app_bar= flet.BottomAppBar(
        bgcolor=flet.colors.BLACK12,
        shape=flet.NotchShape.CIRCULAR,

        #padding=flet.PaddingValue(horizontal=16),       
        content=flet.Row(
            controls=[
                btn_eigene_rezepte,
                flet.Container(expand=True),
                btn_entdecken,
                flet.Container(expand=True),
                btn_gespeichert,
            ]
        ),

    )
   
    # Container mit den Zutaten
    resultdata = ListView()

    resultcon = Container(
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
            for x in result:
                row_container = Row([
                    Text(f" {x['name']} ", size=20, color="white"),
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

    def extract_text(cell):
        if hasattr(cell, 'text'):
            return cell.text.strip().split()[0]  # Nur den ersten Teil des Textes (den Namen) extrahieren
        else:
            return ""


    def check_matching_dishes():
        available_ingredients = {extract_text(row.cells[0]) for row in speisedata.rows}  # Extrahiere alle Zutatennamen aus speisedata
        matching_dishes_names = []

        for dish in gerichte:
            dish_ingredients = [extract_text(ingredient[0]) for ingredient in dish['zutaten']]  # Extrahiere die Zutatennamen des Gerichts
            if all(ingredient in available_ingredients for ingredient in dish_ingredients):
                matching_dishes_names.append(dish['name'])

        return matching_dishes_names

    def add_to_inventory(name):
        speisedata.rows.append(
            flet.DataRow(
                cells=[
                    flet.DataCell(flet.Text(name)),
                    flet.DataCell(flet.Text("100")),
                    flet.DataCell(flet.Text("Gramm")),
                ]
            )
        )
        matching_dishes = check_matching_dishes()
        print("Matching dishes:", matching_dishes)

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        page.views.append(
            View(
                route='1',
                controls=[
                    page.appbar1,
                    Text('Lebensmittel', size=30),
                    txtsearch,  
                    resultcon,  
                    bottom_app_bar,
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
                        Text('Deine eigenen Rezepte', size=30),
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
                        Text('Diese Rezepte könnten dir gefallen', size=30),
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
                        Text('Deine gespeicherten Rezepte', size=30),
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
                        Text('Hier sind alle deine Lebensmittel', size=30),
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