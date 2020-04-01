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
        emoji.clear()
        sleep(0.5)

    

class Emoji:
    def __init__(self):
        self.__sense = SenseHat()
        self.__matrix = []
        self.__iterator = 0

    def setColor(self, colorTuple : tuple):
        self.__color = colorTuple

    def display(self):
        #self.__getRandomScreen()
        self.__getScreen()
        self.__sense.set_pixels(self.__matrix)

    #display emojis in random order
    def __getRandomScreen(self):
        num = randrange(1, 4)
        if num == 1:
            self.__matrix = Screens.getScreenOne(self.__color)
        elif num == 2:
            self.__matrix = Screens.getScreenTwo(self.__color)
        else:
            self.__matrix = Screens.getScreenThree(self.__color)

    #display emojis in order
    def __getScreen(self):
        array = [1,2,3]
        if(self.__iterator > 2):
            self.__iterator = 0
        num = array[self.__iterator]
        self.__iterator += 1
        if num == 1:
            self.__matrix = Screens.getScreenOne(self.__color)
        elif num == 2:
            self.__matrix = Screens.getScreenTwo(self.__color)
        else:
            self.__matrix = Screens.getScreenThree(self.__color)

    def clear(self):
        self.__sense.clear();



main()