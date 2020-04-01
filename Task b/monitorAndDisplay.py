from sense_hat import SenseHat
from time import sleep
from reader import Reader
import subprocess

def checkTemp(sense):
	cpuTemp = subprocess.check_output("vcgencmd measure_temp", shell=True)
	array1 = str(cpuTemp).split("=")
	array2 = array1[1].split("'")
	cpuTempFloat = float(array2[0])
	temp = sense.get_temperature()
	actualTemp = temp - ((cpuTempFloat - temp)/1.4) #the formula to derrive temp
	return actualTemp

def displayTemp(sense, temp, reader):
	color = reader.checkComfort(temp) #determines the color of the display
	temp = round(temp,1)
	sense.show_message(str(temp),text_colour=color)


def main():
	sense = SenseHat()
	reader = Reader()
	while True:
		currentTemp = checkTemp(sense)
		displayTemp(sense,currentTemp,reader)
		sleep(10)
		sense.clear()
	

main()
