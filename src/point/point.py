import random 

# A class to represent a Point in 2D plane
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def create_n_points(n):

    points = []

    for i in range(n):

        x = random.randrange(0,10000)
        y = random.randrange(0,10000)

        points.append(Point(x,y))

    return points