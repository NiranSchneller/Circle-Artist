import math




class Vector():

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def rotate(self, angle):
        theta = math.radians(angle)
        self.x = self.x * math.cos(theta) - self.y * math.sin(theta)
        self.y = self.x * math.sin(theta) + self.y * math.cos(theta)
    

        