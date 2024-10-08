from socket import socket
from .common import echo_server

def reader1(sock: socket):
    try:
        data = sock.recv(8192)
        print("reader1 got:", data)
    except BlockingIOError:
        pass


def reader2(sock: socket):
    try:
        data = sock.recv(8192)
        print("reader2 got:", data)
    except BlockingIOError:
        pass


def run(sock1: socket, sock2: socket):
    sock1.setblocking(False)
    sock2.setblocking(False)

    while True:
        reader1(sock1)
        reader2(sock2)


if __name__ == "__main__":
    sock1, sock2 = echo_server(("", 25000))
    run(sock1, sock2)
