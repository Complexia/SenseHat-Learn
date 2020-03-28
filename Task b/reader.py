import json

class Reader:

	def __init__(self):
	

	def checkComfort(self, temp):
		blue = (0,0,255)
		green = (0,255,0)
		red = (255,0,0)
		try:
			with open('config.json') as json_file:
				data = json.load(json_file)
				if temp < data["cold_max"]:
					return blue
				elif temp >= data["comfortable_min"] and temp < data["comfortable_max"]:
					return green
				else:
					return red

		except:
			print("Invalid Json format.")


		
				

