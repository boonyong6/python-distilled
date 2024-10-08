from socket import socket, AF_INET, SOCK_STREAM
from typing import Callable


def echo_server(address):
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.bind(address)
    server_sock.listen(1)

    print("Waiting for the client 1 connection...")
    client_sock1, (host, port) = server_sock.accept()
    print(f"{host}:{port} connected.")

    print("Waiting for the client 2 connection...")
    client_sock2, _ = server_sock.accept()
    print(f"{host}:{port} connected.")

    return (client_sock1, client_sock2)
