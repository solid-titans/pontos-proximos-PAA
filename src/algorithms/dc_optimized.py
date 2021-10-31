# A divide and conquer program in Python3
# to find the smallest distance from a
# given set of points.
import copy
from algorithms.brute_force import bruteForce
from algorithms.utils import dist

# A utility function to find the
# distance between the closest points of
# strip of given size. All points in
# strip[] are sorted according to
# y coordinate. They all have an upper
# bound on minimum distance as d.
# Note that this method seems to be
# a O(n^2) method, but it's a O(n)
# method as the inner loop runs at most 6 times
def stripClosest(strip, size, d):
     
    # Initialize the minimum distance as d
    min_val = d
    
    # Pick all points one by one and
    # try the next points till the difference
    # between y coordinates is smaller than d.
    # This is a proven fact that this loop
    # runs at most 6 times
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
 
    return min_val
 
# A recursive function to find the
# smallest distance. The array P contains
# all points sorted according to x coordinate
def closestUtil(Px, Py, n):
     
    # If there are 2 or 3 points,
    # then use brute force
    if n <= 3:
        return bruteForce(Px, n)
 
    # Find the middle point
    mid = n // 2
    midPoint = Px[mid]
 
    #keep a copy of left and right branch
    Pyl = [] 
    Pyr = []
    li = 0

    for i in range(n):
        if( (Py[i].x < midPoint.x) or ((Py[i].x == midPoint.x) and Py[i].y < midPoint.y)) and (li < mid):
            Pyl.append(Py[i])
            li += 1
        
        else:
            Pyr.append(Py[i])
 
    # Consider the vertical line passing
    # through the middle point calculate
    # the smallest distance dl on left
    # of middle point and dr on right side
    dl = closestUtil(Px, Pyl, mid - 1)
    dr = closestUtil(Px[mid:], Pyr, n - mid)
 
    # Find the smaller of two distances
    d = min(dl, dr)
 
    # Build an array strip[] that contains
    # points close (closer than d)
    # to the line passing through the middle point
    strip = []
    for i in range(n):
        if abs(Py[i].x - midPoint.x) < d:
            strip.append(Py[i])
     
    # Find the self.closest points in strip.
    # Return the minimum of d and self.closest
    # distance is strip[]
    return stripClosest(strip, len(strip), d)
 
# The main function that finds
# the smallest distance.
# This method mainly uses closestUtil()
def closestOptimized(P, n):
    P.sort(key = lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key = lambda point: point.y)
    # Use recursive function closestUtil()
    # to find the smallest distance
    return closestUtil(P, Q, n)
