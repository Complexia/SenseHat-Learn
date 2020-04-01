class Screens():

    @staticmethod
    def getScreenOne(c):
        a = (255,51,51)
        b = (0, 0, 204)
        
        return [
            c, c, c, c, c, c, c, c,
            c, b, b, c, c, b, b, c,
            c, b, b, c, c, b, b, c,
            c, c, c, c, c, c, c, c,
            c, a, c, c, c, c, a, c,
            c, a, a, c, c, a, a, c,
            c, c, a, a, a, a, c, c,
            c, c, c, c, c, c, c, c
        ]

    @staticmethod
    def getScreenTwo(c):
        a = (255,102,178)
        b = (255, 255, 0)
        d = (255,51,51)
        
        return [
            c, c, c, c, c, c, c, c,
            c, b, b, c, c, b, b, c,
            c, c, b, c, c, c, b, c,
            c, c, c, d, d, c, c, c,
            c, c, c, d, d, c, c, c,
            c, a, c, c, c, c, a, c,
            c, a, a, a, a, a, a, c,
            c, c, c, c, c, c, c, c
        ]

    @staticmethod
    def getScreenThree(c):
        a = (128,128,128)
        b = (51, 255, 153)
        return [
            c, c, c, c, c, c, c, c,
            c, c, b, c, c, b, c, c,
            c, b, c, c, c, c, b, c,
            c, c, c, c, c, c, c, c,
            c, c, c, c, c, c, b, c,
            c, c, a, a, a, a, c, c,
            c, a, c, c, c, c, a, c,
            c, c, c, c, c, c, c, c
        ]