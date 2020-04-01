from sense_hat import SenseHat

from random import randrange

def main():
    emoji = Emoji()
    # put in a loop and sleep(3) at the end of each iteration
    emoji.setColor((0, 255, 0))
    emoji.display()

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

class Screens():
    @staticmethod
    def getScreenOne(c):
        b = (0, 0, 0)
        return [
            c, c, c, c, c, c, c, c,
            c, b, b, c, c, b, b, c,
            c, b, b, c, c, b, b, c,
            c, c, c, c, c, c, c, c,
            c, b, c, c, c, c, b, c,
            c, b, b, c, c, b, b, c,
            c, c, b, b, b, b, c, c,
            c, c, c, c, c, c, c, c
        ]

    @staticmethod
    def getScreenTwo(c):
        b = (0, 0, 0)
        return [
            c, c, c, c, c, c, c, c,
            c, b, b, c, c, b, b, c,
            c, c, b, c, c, c, b, c,
            c, c, c, c, c, c, c, c,
            c, c, c, c, c, c, c, c,
            c, b, c, c, c, c, c, c,
            c, b, b, b, b, b, b, c,
            c, c, c, c, c, c, c, c
        ]

    @staticmethod
    def getScreenThree(c):
        b = (0, 0, 0)
        return [
            c, c, c, c, c, c, c, c,
            c, c, b, c, c, c, b, c,
            c, b, c, c, c, b, c, c,
            c, c, c, c, c, c, c, c,
            c, c, c, c, c, c, b, c,
            c, c, b, b, b, b, c, c,
            c, b, c, c, c, c, c, c,
            c, c, c, c, c, c, c, c
        ]

main()