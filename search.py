from flet import *
import flet as ft
def main(page:Page):
 
	# CREATE FAKE DATA
	data = [
		{
			"name":"","age":12
		},
		{
			"name":"oppw","age":12
		},
		{
			"name":"jenifer","age":12
		},
		{
			"name":"aaan","age":12
		},
		{
			"name":"buyua","age":12
		},
		{
			"name":"qwmiu","age":12
		},
		{
			"name":"dokoo","age":12
		},
 
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
					Text(f"name : {x['name']} age : {x['age']}",
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