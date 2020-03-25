from sense_hat import SenseHat
from time import sleep
import reader

def checkTemp(sense):
	temp = sense.get_temperature()
	return temp

def displayTemp(sense, temp, reader):
	color = reader.checkComfort(temp)
	temp = round(temp,1)
	sense.show_message(temp,text_color=color)


def main():
	sense = SenseHat()
	reader = Reader()
	

	while True:
		currentTemp = checkTemp(sense)
		displayTemp(sense,currentTemp,reader)
		sleep(10)
		sense.clear()
	


