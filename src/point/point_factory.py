from point.point import Point
import random 

def create_n_points(n):

    points = []

    for i in range(n):

        x = random.randrange(-10000,10000)
        y = random.randrange(-10000,10000)

        points.append(Point(x,y))

    return points