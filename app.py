import flet
from flet import *
#Für die matching dishes Tabelle
from collections import Counter
# Unsere Datenbanken
from daten import *
from klassen import *

def main(page: Page):
    page.title = "Gourmet Guide"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = "dark"  

    page_appbar1 = flet.AppBar(
        title=Text('Home'), 
        bgcolor='black',
        center_title=False,
        actions=[
            ElevatedButton(text='Speisekammer', icon=icons.FOOD_BANK, on_click=lambda _:page.go('5'))
        ]
    )

    # ElevatedButtons für die untere Leiste
    btn_home = ElevatedButton(text='Home', icon=icons.HOME, on_click=lambda _: page.go('1'))
    btn_eigene_rezepte = ElevatedButton(text='Eigene Rezepte', icon=icons.ADD, on_click=lambda _: page.go('2'))
    btn_entdecken = ElevatedButton(text='Entdecken', icon=icons.EXPLORE, on_click=lambda _: page.go('3'))
    #Ich weiß noch nicht ob wir den Button auch noch nehmen sollten oder ned, aber Home-Button ist besser finde ich 
    btn_gespeichert = ElevatedButton(text='Gespeichert', icon=icons.BOOKMARK, on_click=lambda _: page.go('4'))

    bottom_app_bar = flet.BottomAppBar(
        bgcolor=flet.colors.BLACK12,
        shape=flet.NotchShape.CIRCULAR,
        content=flet.Row(
            controls=[
                btn_home,
                flet.Container(expand=True),
                btn_eigene_rezepte,
                flet.Container(expand=True),
                btn_entdecken,
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
            Text("Search Anything", size=30, weight="bold"),
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
        matching_dishes = []

        for dish in gerichte:
            dish_ingredients = [extract_text(ingredient[0]) for ingredient in dish['zutaten']]  # Extrahiere die Zutatennamen des Gerichts
            common_ingredients = set(dish_ingredients).intersection(available_ingredients)
            if len(common_ingredients) > 0:
                matching_dishes.append((dish['name'], len(common_ingredients)))

        matching_dishes.sort(key=lambda x: x[1], reverse=True)
        matching_dishes = matching_dishes[:5]  # Begrenze auf höchstens 5 Gerichte

        return [dish_name for dish_name, _ in matching_dishes]
    
    matching_dishes_names = check_matching_dishes()
    matching_dishes_table = flet.DataTable(
        columns=[
            flet.DataColumn(flet.Text("Passende Gerichte"))
        ],
        rows=[flet.DataRow(cells=[flet.DataCell(flet.Text(name))]) for name in matching_dishes_names]
    )

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
        matching_dishes_table.rows = [flet.DataRow(cells=[flet.DataCell(flet.Text(name))]) for name in matching_dishes]
        print("Matching dishes:", matching_dishes)

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        page.views.append(
            View(
                route='1',
                controls=[
                    page_appbar1,
                    Text('Lebensmittel', size=30),
                    txtsearch,  
                    resultcon, 
                    matching_dishes_table, 
                    bottom_app_bar,
                ],
                vertical_alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )

        if page.route == '2':
            name_field = TextField(label="Name des Rezepts")
            beschreibung_field = TextField(label="Beschreibung")
            zutaten_field = TextField(label="Zutaten")

            def add_recipe():
                name = name_field.value.strip()
                beschreibung = beschreibung_field.value.strip()
                zutaten_text = zutaten_field.value.strip()
                zutaten_list = [tuple(ingredient.split(',')) for ingredient in zutaten_text.split(';')]
                gerichte.append({
                    'name': name,
                    'beschreibung': beschreibung,
                    'zutaten': zutaten_list
                })
                print("Neues Rezept hinzugefügt:", gerichte[-1])

            add_recipe_button = ElevatedButton(text="Rezept hinzufügen", on_click=lambda _: add_recipe())

            page.views.append(
                View(
                    route='2',
                    controls=[
                        AppBar(title=Text('Eigene Rezepte'), bgcolor='black'),
                        Text('Deine eigenen Rezepte', size=30),
                        name_field,
                        beschreibung_field,
                        zutaten_field,
                        add_recipe_button,
                        bottom_app_bar,
                    ],
                    vertical_alignment=MainAxisAlignment.START,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )
        if page.route == '3':
            images = flet.Row(expand=1, wrap=False, scroll="always", alignment=flet.MainAxisAlignment.END)
            for i in range(1, 11):
                images.controls.append(
                    Image(
                        src=f"pictures/img{i}.jpeg",
                        width=150,
                        height=150,
                        fit=ImageFit.NONE,
                        repeat=ImageRepeat.NO_REPEAT,
                        border_radius=border_radius.all(10),
                    )
                )
            page.views.append(
                View(
                    route='3',
                    controls=[
                        AppBar(title=Text('Entdecken'), bgcolor='black'),
                        Text('Diese Rezepte könnten dir gefallen', size=30),
                       # ElevatedButton(text='Zurück', on_click=lambda _: page.go('1')),
                        images,
                        bottom_app_bar,
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
                        #Text('Deine gespeicherten Rezepte', size=30),
                        ElevatedButton(text='Zurück', on_click=lambda _: page.go('1')),
                        bottom_app_bar,
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
                        speisedata,
                        bottom_app_bar,
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