from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM

# Example 1:
#   Outgoing connection
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("python.org", 80))
sock.send(b"GET /index.html HTTP/1.0\r\n\r\n")
parts = []

while True:
    part = sock.recv(10000)
    if not part:
        print("=>", repr(part))
        break
    parts.append(part)

response = b"".join(parts)
print(response)


# Example 2:
#   Basic echo server that accepts client connections and echoes back
#   any received data.
def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)

    while True:
        client, addr = sock.accept()
        echo_handler(client, addr)


def echo_handler(client: socket, addr):
    print("Connection from:", addr)
    with client:
        while True:
            data = client.recv(10000)
            if not data:
                break
            client.sendall(data)

        print("Connection closed.")


if __name__ == "__main__":
    # echo_server(("", 25000))
    ...


# Example 3:
#   UDP server and client
def run_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)      # 1. Create a UDP socket.
    sock.bind(address)                      # 2. Bind to a address/port.

    while True:
        msg, addr = sock.recvfrom(2000)     # 3. Get a message.
        print(f'Processing "{msg}"...')
        response = b"world"
        sock.sendto(response, addr)         # 4. Send a response back.


def run_client(address):
    sock = socket(AF_INET, SOCK_DGRAM)      # 1. Create a UDP socket.
    sock.sendto(b"hello", address)          # 2. Send a message.
    response, addr = sock.recvfrom(2000)    # 3. Get response.
    print("Received:", response)
    sock.close()


if __name__ == "__main__":
    import sys
    from pathlib import Path

    filename = Path(__file__).name

    if len(sys.argv) != 4:
        raise SystemExit(f"Usage: {filename} [--client|--server] hostname port")
    
    address = (sys.argv[2], int(sys.argv[3]))

    if sys.argv[1] == "--server":
        run_server(address)
    elif sys.argv[1] == "--client":
        run_client(address)
