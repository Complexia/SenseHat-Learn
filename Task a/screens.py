class Screens():
    @staticmethod
    def getScreenOne(c):
        b = (0, 0, 204)
        a = (255,51,51)
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