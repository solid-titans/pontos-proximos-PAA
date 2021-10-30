# A class to represent a Point in 2D plane
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return f"X = {self.x}\nY = {self.y}\n"


    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y