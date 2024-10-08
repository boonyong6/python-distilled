from socket import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
from .common import echo_server


def reader1(sock: socket):
    data = sock.recv(8192)
    print("reader1 got:", data)


def reader2(sock: socket):
    data = sock.recv(8192)
    print("reader2 got:", data)


def run(sock1: socket, sock2: socket):
    selector = DefaultSelector()
    selector.register(sock1, EVENT_READ, data=reader1)
    selector.register(sock2, EVENT_READ, data=reader2)

    while True:
        # `selector.select()` blocks and waits for I/O.
        for key, evt in selector.select():
            func = key.data
            func(key.fileobj)


if __name__ == "__main__":
    sock1, sock2 = echo_server(("", 25000))
    run(sock1, sock2)
