import threading
import time

# Example 1:
#   Run a task using a thread.
def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(1)

thread = threading.Thread(target=countdown, args=[3])
# # Use `daemon` argument to make the thread daemonic by not waiting for 
# #   the thread to finish.
# thread = threading.Thread(target=countdown, args=[3], daemon=True)
thread.start()
thread.join()  # Wait for the thread to finish.
print()


# Example 2:
#   Use a flag or variable to control the thread termination.
must_stop = False

def countdown_stoppable(n):
    while n > 0 and not must_stop:
        print("T-minus", n)
        n -= 1
        time.sleep(1)


# Example 3:
#   Use `Lock` to protect shared data from inconsistent mutations by 
#   multiple threads concurrently.
class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    
    def increment(self):
        with self.lock:
            self.value += 1
    
    def decrement(self):
        with self.lock:
            self.value -= 1


# Example 4: 
#   Use `Event` to make one thread wait for another thread.
def step1(op_evt: threading.Event):
    print("Step 1")
    time.sleep(2)
    op_evt.set()


def step2(pre_evt: threading.Event):
    pre_evt.wait()
    print("Step 2")

step1_evt = threading.Event()
threading.Thread(target=step1, args=[step1_evt]).start()
threading.Thread(target=step2, args=[step1_evt]).start()


# Example 5:
#   Use `Queue` as a medium to communicate between threads.
import queue

def producer(q: queue.Queue):
    for i in range(10):
        print("Producing:", i)
        q.put(i)

    print("Done")
    q.put(None)

def consumer(q: queue.Queue):
    while True:
        item = q.get()  # A blocking call.
        if item is None:
            break
        print("Consuming:", item)

    print("Goodbye")

q = queue.Queue()
threading.Thread(target=producer, args=[q]).start()
threading.Thread(target=consumer, args=[q]).start()
