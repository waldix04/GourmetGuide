from typing import Any, List, Optional, Union
import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue
# Waldi testes hier importe um auf andere seiten zu kommmen!
from flet import RouteChangeEvent,ViewPopEvent,CrossAxisAlignment,MainAxisAlignment
from flet import View,Page,AppBar,ElevatedButton,Text


# Das ist der Header mit Eingabe vom User

class GourmetApp(ft.UserControl):
    def build(self):
        self.new_meal = ft.TextField(hint_text="Was hast du noch in der Vorratskammer?", expand=True)
        self.meals = ft.Column()

        return ft.Column(
            width=600,
            controls=[
                ft.Row([ ft.Text(value="Lebensmittel", style="headlineMedium")], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    controls=[
                        self.new_meal,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                        #Noah Suchbutton
                        ft.FloatingActionButton(icon=ft.icons.SEARCH, on_click=self.search_clicked),
                    ],
                ),               
                self.meals,
            ],
        )

    def add_clicked(self, e):
        meal = Meal(self.new_meal.value, self.meal_delete)
        self.meals.controls.append(meal)
        self.new_meal.value = ""
        self.update()

    def meal_delete(self, meal):
        self.meals.controls.remove(meal)
        self.update()
    
    #Noah Suchfunktion
    def search_clicked(self, e):  # Klickereignis für die Suchfunktion
        eingegebene_zutaten = self.new_meal.value.split(",")  # Annahme: Eingegebene Zutaten werden durch Kommas getrennt
        gefundenen_gerichte = self.suche_nach_gerichten(eingegebene_zutaten, gerichte)
        # Hier kannst du die gefundenen Gerichte weiter verarbeiten, z.B. anzeigen
        print("Gefundene Gerichte:")
        for gericht in gefundenen_gerichte:
            print(f"{gericht['name']}:")
            for zutat, menge in gericht['zutaten']:
                print(f"- {zutat}: {menge}")

    def suche_nach_gerichten(self, nach_zutaten, gerichte):
        gefundenen_gerichte = []
        for gericht in gerichte:
            if all(zutat.lower() in [z[0].lower() for z in gericht['zutaten']] for zutat in nach_zutaten):
                gefundenen_gerichte.append(gericht)
        return gefundenen_gerichte
    
#Noah Datenbank als Liste:

gerichte = [
    {
        'name': 'Spaghetti Carbonara',
        'beschreibung': 'Nudeln mit Speck, Ei und Parmesan in Sahnesauce',
        'preis': 9.99,
        'zutaten': [('Nudeln', '200g'), ('Speck', '100g'), ('Ei', '2 Stück'), ('Parmesan', '50g'), ('Sahne', '100ml')]
    },
    {
        'name': 'Gegrilltes Hähnchen',
        'beschreibung': 'Saftiges Hähnchenbrustfilet vom Grill mit Gemüsebeilage',
        'preis': 12.50,
        'zutaten': [('Hähnchenbrustfilet', '300g'), ('Gemüse', '200g'), ('Gewürze', 'nach Geschmack')]
    },
    {
        'name': 'Vegetarische Pizza',
        'beschreibung': 'Pizza mit Tomatensauce, Mozzarella und verschiedenen Gemüsesorten',
        'preis': 8.99,
        'zutaten': [('Teig', '300g'), ('Tomatensauce', '150ml'), ('Mozzarella', '200g'), ('Gemüse', '150g')]
    }
]


class Meal(ft.UserControl):
    def __init__(self, meal_name, meal_delete):
        super().__init__()
        self.meal_name = meal_name
        self.meal_delete = meal_delete

    def build(self):
        self.display_meal = ft.Checkbox(value=False, label=self.meal_name)
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_meal,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Bearbeiten",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Löschen",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Bestätigen",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_name.value = self.display_meal.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_meal.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.meal_delete(self)

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


# Icons unten
    
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Entdecken"),
            ft.NavigationDestination(icon=ft.icons.ADD_BOX, label="Eigene Rezepte"),
            ft.NavigationDestination(icon=ft.icons.BOOKMARK_BORDER, selected_icon=ft.icons.BOOKMARK, label="Gespeicherte Rezepte"),
        ]
    )
   
    meal = GourmetApp()
    page.add(meal)

    #Die Bilder können wir auch statt dessen wo anders hinpacken
    images = ft.Row(expand=1, wrap=False, scroll="always", alignment=ft.MainAxisAlignment.END)

    page.add(images)
    for i in range(1,11):
        images.controls.append(
            ft.Image(
                src= f"pictures/img{i}.jpeg",
                width=150,
                height=150,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    page.update()

ft.app(target=main)

# Versuch die Icons auf andere seiten zu bringen (Verlinkung)
#def Entdecken(page: ft.Page):   
#    page.title = "Entdecken"
#    page.theme_mode = ft.ThemeMode.DARK
#    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


