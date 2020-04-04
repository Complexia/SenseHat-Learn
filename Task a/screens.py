class Screens():

    @staticmethod
    def getScreenOne(c):
        a = (255,51,51) #mouth
        b = (0, 0, 204) #eyes
        d = (255,255,0) #nose
        
        return [
            c, c, c, c, c, c, c, c,
            c, b, b, c, c, b, b, c,
            c, b, b, c, c, b, b, c,
            c, c, c, d, c, c, c, c,
            c, a, c, c, d, c, a, c,
            c, a, a, c, c, a, a, c,
            c, c, a, a, a, a, c, c,
            c, c, c, c, c, c, c, c
        ]

    @staticmethod
    def getScreenTwo(c):
        a = (255,102,178) #mouth
        b = (255, 255, 0) #eyes
        d = (255,51,51) #nose
        
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
        a = (153,0,153) #mouth
        b = (0, 76, 153) #eyes
        d = (255,0,0) #tears
        return [
            c, c, c, c, c, c, c, c,
            c, b, b, c, c, b, b, c,
            c, d, c, c, c, c, d, c,
            c, d, c, c, c, c, d, c,
            c, c, c, c, c, c, c, c,
            c, c, a, a, a, a, c, c,
            c, a, c, c, c, c, a, c,
            c, c, c, c, c, c, c, c
        ]