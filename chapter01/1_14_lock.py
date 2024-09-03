import threading

lock = threading.Lock()

lock.acquire()
# If a lock has been acquired. it MUST be released.
try:
    print("Some processing...")
finally:
    lock.release()  # Always runs

# Alternative:
with lock:
    print("Some processing...")
