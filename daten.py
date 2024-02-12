import flet

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

speisedata= flet.DataTable(
        columns=[
            flet.DataColumn(flet.Text("name")),
            flet.DataColumn(flet.Text("Menge")),
            flet.DataColumn(flet.Text("Einheit")),
        ],
        rows=[
            flet.DataRow(
                cells=[
                    flet.DataCell(flet.Text("Tomaten")),
                    flet.DataCell(flet.Text("200")),
                    flet.DataCell(flet.Text("Gramm")),
                ]
            )
        ]

    )

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