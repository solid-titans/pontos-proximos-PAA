import sys
import time

from algorithms.brute_force import bruteForce
from algorithms.divide_and_conquer import closest
from algorithms.dc_optimized import closestOptimized
from point.point import create_n_points

n = 10

if len(sys.argv) >= 2:
    n = int(sys.argv[1])

P = create_n_points(n)


print("Running Bruteforce...\n")

initialWClock = time.process_time()
print("The smallest distance is",bruteForce(P, n))
clock = time.process_time() - initialWClock
print(f'Tempo: {clock} seconds' )

print("Running Divide and Conquer...\n")

initialWClock = time.process_time()
print("The smallest distance is",closest(P, n))
clock = time.process_time() - initialWClock
print(f'Tempo: {clock} seconds' )

print("Running Divide and Conquer optimized...\n")

initialWClock = time.process_time()
print("The smallest distance is",closestOptimized(P, n))
clock = time.process_time() - initialWClock
print(f'Tempo: {clock} seconds' )
