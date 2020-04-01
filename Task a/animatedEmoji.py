from sense_hat import SenseHat
from screens import Screens
from random import randrange
from time import sleep

def main():
    emoji = Emoji()
    while True:
        emoji.setColor((0, 255, 0))
        emoji.display()
        sleep(3)
    

class Emoji:
    def __init__(self):
        self.__sense = SenseHat()
        self.__matrix = []

    def setColor(self, colorTuple : tuple):
        self.__color = colorTuple

    def display(self):
        self.__getRandomScreen()
        self.__sense.set_pixels(self.__matrix)

    def __getRandomScreen(self):
        num = randrange(1, 4)
        if num == 1:
            self.__matrix = Screens.getScreenOne(self.__color)
        elif num == 2:
            self.__matrix = Screens.getScreenTwo(self.__color)
        else:
            self.__matrix = Screens.getScreenThree(self.__color)



main()