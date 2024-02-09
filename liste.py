# Liste von Gerichten
gerichte = [
    {
        'name': 'Spaghetti Carbonara',
        'beschreibung': 'Nudeln mit Speck, Ei und Parmesan in Sahnesauce',
        'preis': 9.99,
        'zutaten': ['Nudeln', 'Speck', 'Ei', 'Parmesan', 'Sahne']
    },
    {
        'name': 'Gegrilltes Hähnchen',
        'beschreibung': 'Saftiges Hähnchenbrustfilet vom Grill mit Gemüsebeilage',
        'preis': 12.50,
        'zutaten': ['Hähnchenbrustfilet', 'Gemüse', 'Gewürze']
    },
    {
        'name': 'Vegetarische Pizza',
        'beschreibung': 'Pizza mit Tomatensauce, Mozzarella und verschiedenen Gemüsesorten',
        'preis': 8.99,
        'zutaten': ['Teig', 'Tomatensauce', 'Mozzarella', 'Gemüse']
    }
]

# Zugriff auf Gerichte
for gericht in gerichte:
    print(f"Name: {gericht['name']}")
    print(f"Beschreibung: {gericht['beschreibung']}")
    print(f"Preis: {gericht['preis']}")
    print(f"Zutaten: {', '.join(gericht['zutaten'])}")
    print()


def suche_nach_gerichten(nach_zutaten, gerichte):
    gefundenen_gerichte = []
    for gericht in gerichte:
        if all(zutat.lower() in [z.lower() for z in gericht['zutaten']] for zutat in nach_zutaten):
            gefundenen_gerichte.append(gericht)
    return gefundenen_gerichte

# Beispielaufruf der Funktion
eingegebene_zutaten = ['Nudeln', 'Ei']  # Annahme: Liste von eingegebenen Zutaten aus dem Textfeld
gefundene_gerichte = suche_nach_gerichten(eingegebene_zutaten, gerichte)



   
