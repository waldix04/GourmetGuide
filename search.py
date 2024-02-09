from flet import *
import flet as ft
def main(page:Page):
 
	# CREATE FAKE DATA
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
		offset=transform.Offset(-2,0),
		animate_offset = animation.Animation(600,curve="easeIn"),
		content=Column([
			resultdata
 
			])
		)
 
	def searchnow(e):
		mysearch = e.control.value
		result = []
 
		# IF NOT BLANK YOU TEXTFIELD SEARCH THE RUN FUNCTION
		if not mysearch == "":
			resultcon.visible = True
			for item in data:
				if mysearch in item['name']:
					resultcon.offset = transform.Offset(0,0)
					result.append(item)
			page.update()
 
		# IF RESULT THERE DATA THEN PUSH DATA TO WIDGET CONTAINER Resultcon
		if result:
			resultdata.controls.clear()
			print(f"YOu result {result}")
			for x in result:
				resultdata.controls.append(
					Text(f"name : {x['name']} ",
						size=20,color="white"
 
						)
 
					)
			page.update()
		else:
			resultcon.offset = transform.Offset(-2,0)
			resultdata.controls.clear()
			page.update()
 
	# HIDE RESULT FOR YOU SEARCH DEFAULT
	resultcon.visible = False
 
	txtsearch = TextField(label="Search now",
		on_change=searchnow
		)
 
 
	page.add(
	Column([
	Text("Search Anything",size=30,weight="bold"),
	txtsearch,
	resultcon
	])
		)
 
ft.app(target=main)