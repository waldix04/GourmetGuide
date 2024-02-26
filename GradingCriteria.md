<!-- https://github.com/skills/communicate-using-markdown -->


# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.

## FACHKOMPETENZ (40 Punkte)(33)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10) (8)
<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->

Der gezeigte Code demonstriert verschiedene Konzepte der prozeduralen Programmierung. Hier einige Beispiele:

Funktionen:

Der Code verwendet verschiedene Funktionen, um bestimmte Aufgaben zu kapseln. Zum Beispiel:
searchnow(e): Sucht nach Übereinstimmungen in den Daten basierend auf der Benutzereingabe.
check_matching_dishes(): Prüft, welche Gerichte mit den verfügbaren Zutaten zubereitet werden können.
add_to_inventory(name): Fügt ein neues Lebensmittel zum Inventar hinzu.
route_change(e): Fügt je nach Route dynamisch neue Views zur App hinzu.
add_recipe(): Fügt ein neues Rezept hinzu.
Prozeduren:

Innerhalb der Funktionen werden Abfolgen von Anweisungen verwendet, um bestimmte Schritte auszuführen. Zum Beispiel:
In der searchnow-Funktion werden die Benutzereingabe verarbeitet, die Daten durchsucht und die Ergebnisse angezeigt.
In der check_matching_dishes-Funktion werden die verfügbaren Zutaten mit den Zutaten der Gerichte verglichen und passende Gerichte ermittelt.
Kontrollfluss:

Der Code verwendet verschiedene Kontrollflussstrukturen, um den Programmfluss zu steuern. Zum Beispiel:
if-Anweisungen werden verwendet, um Bedingungen zu prüfen und je nach Ergebnis unterschiedliche Codeblöcke auszuführen (z.B. in der searchnow-Funktion, um zu prüfen, ob eine Übereinstimmung gefunden wurde).
for-Schleifen werden verwendet, um Daten zu durchlaufen (z.B. in der searchnow-Funktion, um die Daten nach Übereinstimmungen zu durchsuchen).
Variablen:

Der Code verwendet verschiedene Variablen, um Daten zwischenzuspeichern. Zum Beispiel:
result: Speichert die gefundenen Suchergebnisse.
matching_dishes: Speichert die Gerichte, die mit den verfügbaren Zutaten zubereitet werden können.
name: Speichert den Namen des hinzuzufügenden Lebensmittels.
Diese Beispiele zeigen, dass der Code grundlegende Konzepte der prozeduralen Programmierung verwendet, um die Benutzeroberfläche zu gestalten, Daten zu verarbeiten und die App-Logik zu steuern.

# Sie können die Syntax und Semantik von Python (10) (9)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->

##
def route_change(e: RouteChangeEvent) -> None:
  ...
  if page.route == '2':
    ...
  if page.route == '3':
    ...
  if page.route == '4':
    ...
  if page.route == '5':
    ...
```

Die Implementierung der `route_change`-Funktion demonstriert die Verwendung von `if`-Anweisungen, um verschiedene Routen zu behandeln. Durch diese Modularität ist es einfach, neue Routen und Funktionen hinzuzufügen, ohne den bestehenden Code stark zu verändern.

**2. Dynamische Aktualisierung der Benutzeroberfläche:**

```python
def searchnow(e):
  ...
  if result:
    resultdata.controls.clear()
    for x in result:
      row_container = Row([
        Text(f" {x['name']} ", size=20, color="white"),
        IconButton(icons.ADD_BOX_SHARP, on_click=lambda e, name=x['name']: add_to_inventory(name))
      ])
      resultdata.controls.append(row_container)
    page.update()
```

Die `searchnow`-Funktion zeigt, wie die Benutzeroberfläche dynamisch aktualisiert werden kann, indem die `controls`-Eigenschaft einer `ListView` verändert wird. Die Funktion nutzt die `update`-Methode der `Page`, um die Änderungen an der Benutzeroberfläche anzuzeigen.

**3. Datenverarbeitung und Logik:**

```python
def check_matching_dishes():
  ...
  for row in gerichte2.rows:
    ...
    for ingredient in dish_ingredients:
      if ingredient in available_ingredients:
        found_matching_ingredient = True
        break

  if found_matching_ingredient:
    matching_dishes.append((dish_name, dish_description, dish_ingredients))

  return matching_dishes
```

Die `check_matching_dishes`-Funktion demonstriert die Verarbeitung von Daten aus zwei Tabellen (`speisedata` und `gerichte2`) und die Implementierung einer Logik, um passende Gerichte zu finden. Die Funktion verwendet for-Schleifen, `if`-Anweisungen und das `break`-Statement, um die Daten effizient zu durchsuchen und die gewünschten Ergebnisse zu liefern.

**Zusätzliche Punkte:**

* Der Code verwendet sprechende Variablennamen und Funktionen, um die Lesbarkeit und Verständlichkeit zu verbessern.
* Der Code ist sauber formatiert und gut strukturiert.

**Zusammenfassend:**

Der vorgestellte Code zeigt verschiedene Techniken der prozeduralen Programmierung und demonstriert, wie diese Techniken verwendet werden können, um eine funktionsfähige und übersichtliche App zu erstellen.


# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10) (8)
## Gemeinschaftsprojekt: Entwicklung einer funktionsfähigen App

In diesem Text möchte ich unsere Teamarbeit an einem größeren Programmierprojekt beschreiben, welches die Entwicklung einer funktionsfähigen App beinhaltet.

**Entwurf und Programmierung:**

Zu Beginn des Projekts haben wir uns gemeinsam Gedanken über den Entwurf der App gemacht. Wir haben die Funktionen und die Benutzeroberfläche skizziert und uns auf die zu verwendenden Technologien geeinigt.

Danach haben wir die App in mehreren Schritten programmiert. Dabei haben wir uns die Aufgaben aufgeteilt und den Code gemeinsam entwickelt. Wir haben uns regelmäßig verabredet, um den Fortschritt zu besprechen, Probleme zu lösen und den Code zusammenzufügen. Dazu haben uns dann auf Discord getroffen und zusaden code zusammengeführt. Daher stehen die Commits nicht im Zusammenhang mit der tatsächlichen Arbeit jedes einzelen. Alles wurde in ungefähr gleichen Teilen entwickelt.

**Testen und Fehlerbehebung:**

Während der Entwicklung haben wir die App kontinuierlich auf ihre Funktionsfähigkeit getestet. Wir haben verschiedene Testfälle definiert und die App auf verschiedenen Geräten und Betriebssystemen ausprobiert.

**Spaß und Problemlösung:**

Die Zusammenarbeit im Team hat uns allen viel Spaß gemacht. Wir haben uns gegenseitig unterstützt und konnten so Probleme und Hindernisse schnell und effizient überwinden.

**Ergebnis:**

Das Ergebnis unserer Teamarbeit ist eine funktionsfähige App, die den Anforderungen entspricht. Wir sind stolz auf das Erreichte und haben viel aus dem Projekt gelernt.

**Zusammenfassend**

Die Entwicklung der App hat gezeigt, dass wir in der Lage sind, ein größeres Programmierprojekt selbständig zu entwerfen, zu programmieren und auf Funktionsfähigkeit zu testen. Durch die gute Zusammenarbeit im Team konnten wir Probleme und Hindernisse erfolgreich meistern und ein tolles Ergebnis erzielen.

**Hinweis:**

Der Code, den du mir oben gegeben hast, ist ein Teil der App, den wir entwickelt haben. Er zeigt beispielhaft, wie wir verschiedene Techniken der prozeduralen Programmierung verwendet haben, um die App zu implementieren.



# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10) (8)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->



## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10) (Git Flet VSC 8)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein)-->

<!-- GIT -->
<!-- VSC -->
<!-- Codepilot -->
<!-- other -->



## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5) (4)
<!-- You have helped someone else and taught something to a fellow student (get a support message from one person) -->

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project -->

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10) (8)
<!-- Which technology did you learn outside of the teacher given input -->
<!-- Did you get help from someone in the classroom (get a support message here from the person who helped you) -->



## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30) (mehrere punkte auf geschriebenen text verteilen und ihn so bewerten)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->



## Kenntnisse in prozeduraler Programmierung:

# - Algorithmenbeschreibung

# - Datentypen

# - E/A-Operationen und Dateiverarbeitung

# - Operatoren

# - Kontrollstrukturen

# - Funktionen

# - Stringverarbeitung

# - Strukturierte Datentypen