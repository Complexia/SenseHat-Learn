from random import randrange

from .screens import Screens
from .sensor import Sensor

class Die:
    def __init__(self):
        self.__number = 0
        self.__sensor = Sensor()

    def getNumber(self):
        return self.__number

    def __randomizeNumber(self):
        self.__number = randrange(1, 7)

    def __display(self):
        self.__sensor.update_sense_hat(self.__matrix)
    
    def roll(self, player):
        self.__randomizeNumber()
        self.__roll_num(player.getId())
        self.__display()
        return self.__number

    def detectShake(self):
        return self.__sensor.detect_shake()

    def __roll_num(self, id):
        if self.__number == 1:
            self.__matrix = Screens.get_one(id)
        elif self.__number == 2:
            self.__matrix = Screens.get_two(id)
        elif self.__number == 3:
            self.__matrix = Screens.get_three(id)
        elif self.__number == 4:
            self.__matrix = Screens.get_four(id)
        elif self.__number == 5:
            self.__matrix = Screens.get_five(id)
        elif self.__number == 6:
            self.__matrix = Screens.get_six(id)
        else:
            self.__matrix = Screens.get_blank()