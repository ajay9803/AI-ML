### Multithreading

## When to use multithreading
# For I/O bound tasks
# To improve concurrent execution

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")
        
def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")
        
# Create two threads        
        
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()
