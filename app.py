# Imports die man braucht
from typing import Any, List, Optional, Union
import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue

# Klasse GourmetApp ist schon direkt sichtbar auf Mainpage
class GourmetApp(ft.UserControl):

    # Funktion, die in Abhängigkeit von "self" agiert
    def build(self):

        #Zuerst das Eingabefeld mit Hinweistext
        self.new_meal = ft.TextField(hint_text="Was hast du noch in der Vorratskammer?", expand=True)
        self.meals = ft.Column()

        # Überschrift Lebensmittel und der Add-Button rechts vom Eingabefeld
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
    
    # Die Funktion wenn der Add-Button geklickt wird, ruft auch die Klasse "Meal" auf
    def add_clicked(self, e):
        meal = Meal(self.new_meal.value, self.meal_delete)
        self.meals.controls.append(meal)
        self.new_meal.value = ""
        self.update()

    def meal_delete(self, meal):
        self.meals.controls.remove(meal)
        self.update()


# Klasse "Meal" mit weiteren Benutzerkontrollmöglichkeiten, um die Lebensmittel zu bearbeiten
class Meal(ft.UserControl):

    # Initialisierung und Übergabe von Variablen
    def __init__(self, meal_name, meal_delete):
        super().__init__()
        self.meal_name = meal_name
        self.meal_delete = meal_delete

    # Hinzugefügte Lebensmittel werden aufgebaut/angezeigt (Checkbox und danben Textfeld)
    def build(self):
        self.display_meal = ft.Checkbox(value=False, label=self.meal_name)
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,

            # Kontrollmöglichkeiten für die Lebensmittel mit Icon und Text (=Iconbutton)
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

        # Iconbutton zum Bestätigen der Veränderungen ist am Anfang nicht sichtbar
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

    # Logik dahinter wenn man die unterschiedlichen Buttons benutzt, werden auch direkt von den Buttons aufgerufen
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

# Mainpage wird definiert: Titel, Ausrichtung, Navigationsbuttons
def main(page: ft.Page):
    page.title = "Gourmet Guide"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    #Die Buttons machen bisher noch nichts
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Entdecken"),
            ft.NavigationDestination(icon=ft.icons.ADD_BOX, label="Eigene Rezepte"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Gespeicherte Rezepte",
            ),
        ]
    )

    # Klasse GourmetAPP wird zu der Mainpage hinzugefügt durch Variable "meal" (man könnte noch mehr von der Mainpage in die Klasse schreiben)
    meal = GourmetApp()
    page.add(meal)
    
ft.app(target=main)