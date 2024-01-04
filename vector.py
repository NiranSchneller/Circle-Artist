# The following functions (cos and sin) are more efficient in small angles than math module.

@staticmethod
def cos(x: float):  # Taylor expansion for cosine, see: https://www.desmos.com/calculator/zndrlyt63c
    return 1 - (x * x) / 2


@staticmethod
def sin(x: float):  # Taylor expansion for sine, see: https://www.desmos.com/calculator/k8na06dihl
    return x - (x * x * x) / 6


PI = 3.1415926535


@staticmethod
def radians(x: float):
    return x * (PI / 180)


class Vector():

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def rotate(self, angle: float):
        theta = radians(angle)
        self.x = self.x * cos(theta) - self.y * sin(theta)
        self.y = self.x * sin(theta) + self.y * cos(theta)
