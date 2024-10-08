from socket import socket
import threading
from .common import echo_server


def reader1(sock: socket):
    while data := sock.recv(8192):
        print("reader1 got:", data)


def reader2(sock: socket):
    while data := sock.recv(8192):
        print("reader2 got:", data)


def run(sock1: socket, sock2: socket):
    t1 = threading.Thread(target=reader1, args=[sock1])
    t2 = threading.Thread(target=reader2, args=[sock2])

    # Start the threads.
    t1.start()
    t2.start()

    # Wait for the threads to finish.
    t1.join()
    t2.join()


if __name__ == "__main__":
    sock1, sock2 = echo_server(("", 25000))
    run(sock1, sock2)