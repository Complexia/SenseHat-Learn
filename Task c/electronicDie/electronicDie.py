from random import randrange
from time import sleep

from .screens import Screens
from .sensor import Sensor

class Die:
    def __init__(self):
        self.__number = 0
        self.__sensor = Sensor()
        self.__matrix = []

    def getNumber(self):
        return self.__number

    def __randomizeNumber(self):
        self.__number = randrange(1, 7)

    def __display(self):
        self.__sensor.update_sense_hat(self.__matrix)
    
    def shake(self):
        if self.__sensor.detect_shake():
            self.__randomizeNumber()
            self.__role_num()
            self.__display()
            sleep(1)

    def __role_num(self):
        if self.__number == 1:
            self.__matrix = Screens.get_one()
        elif self.__number == 2:
            self.__matrix = Screens.get_two()
        elif self.__number == 3:
            self.__matrix = Screens.get_three()
        elif self.__number == 4:
            self.__matrix = Screens.get_four()
        elif self.__number == 5:
            self.__matrix = Screens.get_five()
        elif self.__number == 6:
            self.__matrix = Screens.get_six()
        else:
            self.__matrix = Screens.get_blank()