from sense_hat import SenseHat
from screens import Screens
from time import sleep

def main():
    emoji = Emoji()
    while True:
        emoji.setColor((51, 102, 0)) #background color
        emoji.display()
        sleep(3)
        emoji.clear()
        sleep(0.5)

    
#responsible for displaying the emojis from screens
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

    #display emojis in order
    def __getScreen(self):
        array = [1,2,3]
        #selects the emoji number from array and iterates in order
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

    #clears the screen in between each emoji to allow for smoother transition
    def clear(self):
        self.__sense.clear();



main()