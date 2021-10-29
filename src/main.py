import sys
import time

from algorithms.brute_force import bruteForce
from algorithms.divide_and_conquer import closest
from point.point_factory import create_n_points

n = 10

algorithm = "1"

if len(sys.argv) >= 2:
    n = int(sys.argv[1])
    algorithm = sys.argv[2]
elif len(sys.argv) >= 3:
    algorithm = sys.argv[2]

P = create_n_points(n)

if algorithm == "1":
    print("Running Bruteforce...\n")

    initialWClock = time.process_time()
    print("The smallest distance is",bruteForce(P, n))
    clock = time.process_time() - initialWClock
    print(f'Tempo: {clock} seconds' )

elif algorithm == "2":
    print("Running Divide and Conquer...\n")

    initialWClock = time.process_time()
    print("The smallest distance is",closest(P, n))
    clock = time.process_time() - initialWClock
    print(f'Tempo: {clock} seconds' )
else:
    print("Error! Unknown algorithm")