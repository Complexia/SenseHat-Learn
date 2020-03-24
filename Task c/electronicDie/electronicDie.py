from sensor import Sensor
from die import Die
from sense_hat import SenseHat
from time import sleep

def main():
    sense = SenseHat()
    sensor = Sensor(sense)

    screen = Die(sensor)

    screen.display()

    while True:
        if sensor.detect_shake():
            screen.randomizeNumber()
            screen.display()
            sleep(1)

main()