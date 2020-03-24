from random import randrange
from sense_hat import SenseHat

from screens import Screens
from sensor import Sensor

class Die:
    def __init__(self, sensor):
        self.__number = 0
        self.__sensor = sensor
        self.__matrix = []

    def randomizeNumber(self):
        self.__number = randrange(1, 7)

    def display(self):
        self.__role_num()
        self.__sensor.update_sense_hat(self.__matrix)

    def __role_num(self):
        print('A %d was roled' % self.__number)
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