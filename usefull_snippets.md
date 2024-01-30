# damit kann man die App im Browser öffnen
flet.app(target=main, view=flet.WEB_BROWSER)

# unterschiedliche Dinge (Eingabefelder & Plus/Minusbutton)
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

# Dictionary für eine Datenbank

def main(page: ft.Page):
    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Eier")),
                ft.DataColumn(ft.Text("Butter")),
                ft.DataColumn(ft.Text("Mehl")),
            ],
            rows:[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("2")),
                        ft.DataCell(ft.Text("100g")),
                        ft.DataCell(ft.Text("250g")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("4")),
                        ft.DataCell(ft.Text("500g")),
                        ft.DataCell(ft.Text("500g")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("2")),
                        ft.DataCell(ft.Text("100g")),
                        ft.DataCell(ft.Text("250g")),
                    ],
                ),
            ],
        ),      
    )