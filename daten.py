import flet

data = [
    {"name": "Ananas"},
    {"name": "Apfel"},
    {"name": "Avocado"},
    {"name": "Backpulver"},
    {"name": "Banane"},
    {"name": "Birne"},
    {"name": "Blumenkohl"},
    {"name": "Bohnen"},
    {"name": "Brot"},
    {"name": "Brokkoli"},
    {"name": "Butter"},
    {"name": "Champignons"},
    {"name": "Ei"},
    {"name": "Eier"},
    {"name": "Erdbeere"},
    {"name": "Erbsen"},
    {"name": "Essig"},
    {"name": "Gurke"},
    {"name": "Gurken"},
    {"name": "Haferflocken"},
    {"name": "Himbeere"},
    {"name": "Hühnchen"},
    {"name": "Joghurt"},
    {"name": "Kartoffel"},
    {"name": "Kartoffeln"},
    {"name": "Karotten"},
    {"name": "Käse"},
    {"name": "Kiwi"},
    {"name": "Knoblauch"},
    {"name": "Kopfsalat"},
    {"name": "Lachs"},
    {"name": "Linsen"},
    {"name": "Mango"},
    {"name": "Mehl"},
    {"name": "Milch"},
    {"name": "Nudeln"},
    {"name": "Olivenöl"},
    {"name": "Orange"},
    {"name": "Paprika"},
    {"name": "Pfirsich"},
    {"name": "Quinoa"},
    {"name": "Reis"},
    {"name": "Rindfleisch"},
    {"name": "Rosinen"},
    {"name": "Rucola"},
    {"name": "Salat"},
    {"name": "Salz"},
    {"name": "Schinken"},
    {"name": "Schokolade"},
    {"name": "Schweinefleisch"},
    {"name": "Sellerie"},
    {"name": "Senf"},
    {"name": "Sojasauce"},
    {"name": "Spinat"},
    {"name": "Tomate"},
    {"name": "Tomaten"},
    {"name": "Vanilleextrakt"},
    {"name": "Vanillezucker"},
    {"name": "Zimt"},
    {"name": "Zitrone"},
    {"name": "Zucchini"},
    {"name": "Zucker"},
    {"name": "Zwiebeln"},
    {"name": "gehackte Nüsse"},
    {"name": "Ananas"},
    {"name": "Apfel"},
    {"name": "Avocado"},
    {"name": "Backpulver"},
    {"name": "Banane"},
    {"name": "Birne"},
    {"name": "Blumenkohl"},
    {"name": "Bohnen"},
    {"name": "Brot"},
    {"name": "Brokkoli"},
    {"name": "Butter"},
    {"name": "Champignons"},
    {"name": "Ei"},
    {"name": "Eier"},
    {"name": "Erdbeere"},
    {"name": "Erbsen"},
    {"name": "Essig"},
    {"name": "Gurke"},
    {"name": "Gurken"},
    {"name": "Haferflocken"},
    {"name": "Himbeere"},
    {"name": "Hühnchen"},
    {"name": "Joghurt"},
    {"name": "Kartoffel"},
    {"name": "Kartoffeln"},
    {"name": "Karotten"},
    {"name": "Käse"},
    {"name": "Kiwi"},
    {"name": "Knoblauch"},
    {"name": "Kopfsalat"},
    {"name": "Lachs"},
    {"name": "Linsen"},
    {"name": "Mango"},
    {"name": "Mehl"},
    {"name": "Milch"},
    {"name": "Nudeln"},
    {"name": "Olivenöl"},
    {"name": "Orange"},
    {"name": "Paprika"},
    {"name": "Pfirsich"},
    {"name": "Quinoa"},
    {"name": "Reis"},
    {"name": "Rindfleisch"},
    {"name": "Rosinen"},
    {"name": "Rucola"},
    {"name": "Salat"},
    {"name": "Salz"},
    {"name": "Schinken"},
    {"name": "Schokolade"},
    {"name": "Schweinefleisch"},
    {"name": "Sellerie"},
    {"name": "Senf"},
    {"name": "Sojasauce"},
    {"name": "Spinat"},
    {"name": "Tomate"},
    {"name": "Tomaten"},
    {"name": "Vanilleextrakt"},
    {"name": "Vanillezucker"},
    {"name": "Zimt"},
    {"name": "Zitrone"},
    {"name": "Zucchini"},
    {"name": "Zucker"},
    {"name": "Zwiebeln"},
    {"name": "gehackte Nüsse"}
]


speisedata= flet.DataTable(
        columns=[
            flet.DataColumn(flet.Text("Name")),
            flet.DataColumn(flet.Text("Menge")),
            flet.DataColumn(flet.Text("Einheit")),
        ],
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