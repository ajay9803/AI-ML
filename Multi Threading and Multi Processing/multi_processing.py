## run multiple processes in parallel

## when to use - for CPU bound tasks, to use multiple CPU cores

import multiprocessing
import multiprocessing.process
import time

def print_squares():
    for i in range(5):
        time.sleep(1)
        print(f"Squares: {i * i}")
        
def print_cubes():
    for i in range(5):
        time.sleep(1)
        print(f"Cubes: {i * i * i}")
        
if __name__ == '__main__':
        
    # Create two processes
    p1 = multiprocessing.Process(target=print_squares)
    p2 = multiprocessing.Process(target=print_cubes)

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the processes to complete
    p1.join()
    p2.join()
