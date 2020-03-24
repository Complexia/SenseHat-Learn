from sense_hat import SenseHat

class Sensor:
    def __init__(self, sense):
        self.__sense = sense
        self.__x = 0
        self.__y = 0
        self.__z = 0

    def detect_shake(self):
        acceleration = self.__sense.get_accelerometer_raw()
        self.__x = abs(acceleration['x'])
        self.__y = abs(acceleration['y'])
        self.__z = abs(acceleration['z'])

        if self.__x > 1.5 or self.__y > 1.5 or self.__z > 1.5:
            return True
        
        return False

    def update_sense_hat(self, matrix):
        self.__sense.set_pixels(matrix)