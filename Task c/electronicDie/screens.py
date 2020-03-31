class Screens:
    @staticmethod
    def get_blank():
        w = (255, 255, 255)
        return [
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w
        ]

    @staticmethod
    def get_one(id):
        if id == 1:
            b = (100, 0, 0)
        else:
            b = (0, 0, 100)
        w = (255, 255, 255)
        return [
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, b, b, w, w, w,
            w, w, w, b, b, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w
        ]

    @staticmethod
    def get_two(id):
        if id == 1:
            b = (100, 0, 0)
        else:
            b = (0, 0, 100)
        w = (255, 255, 255)
        return [
            w, w, w, w, w, w, w, w,
            w, b, b, w, w, w, w, w,
            w, b, b, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, b, b, w,
            w, w, w, w, w, b, b, w,
            w, w, w, w, w, w, w, w
        ]

    @staticmethod
    def get_three(id):
        if id == 1:
            b = (100, 0, 0)
        else:
            b = (0, 0, 100)
        w = (255, 255, 255)
        return [
            b, b, w, w, w, w, w, w,
            b, b, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, b, b, w, w, w,
            w, w, w, b, b, w, w, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, b, b,
            w, w, w, w, w, w, b, b
        ]

    @staticmethod
    def get_four(id):
        if id == 1:
            b = (100, 0, 0)
        else:
            b = (0, 0, 100)
        w = (255, 255, 255)
        return [
            w, w, w, w, w, w, w, w,
            w, b, b, w, w, b, b, w,
            w, b, b, w, w, b, b, w,
            w, w, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w,
            w, b, b, w, w, b, b, w,
            w, b, b, w, w, b, b, w,
            w, w, w, w, w, w, w, w
        ]

    @staticmethod
    def get_five(id):
        if id == 1:
            b = (100, 0, 0)
        else:
            b = (0, 0, 100)
        w = (255, 255, 255)
        return [
            b, b, w, w, w, w, b, b,
            b, b, w, w, w, w, b, b,
            w, w, w, w, w, w, w, w,
            w, w, w, b, b, w, w, w,
            w, w, w, b, b, w, w, w,
            w, w, w, w, w, w, w, w,
            b, b, w, w, w, w, b, b,
            b, b, w, w, w, w, b, b
        ]

    @staticmethod
    def get_six(id):
        if id == 1:
            b = (100, 0, 0)
        else:
            b = (0, 0, 100)
        w = (255, 255, 255)
        return [
            w, b, b, w, w, b, b, w,
            w, b, b, w, w, b, b, w,
            w, w, w, w, w, w, w, w,
            w, b, b, w, w, b, b, w,
            w, b, b, w, w, b, b, w,
            w, w, w, w, w, w, w, w,
            w, b, b, w, w, b, b, w,
            w, b, b, w, w, b, b, w
        ]