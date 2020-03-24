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
    def get_one():
        b = (0, 0, 0)
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
    def get_two():
        b = (0, 0, 0)
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
    def get_three():
        b = (0, 0, 0)
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
    def get_four():
        b = (0, 0, 0)
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
    def get_five():
        b = (0, 0, 0)
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
    def get_six():
        b = (0, 0, 0)
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