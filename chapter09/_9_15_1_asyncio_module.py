import asyncio
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

async def echo_server(address):
    evt_loop = asyncio.get_event_loop()
    
    # AF_INET - IPv4
    # SOCK_STREAM - TCP Connection
    sock = socket(AF_INET, SOCK_STREAM)

    # SOL_SOCKET - General socket option
    # SO_REUSEADDR - Allows address reuse even if the socket is in 
    #   a wait state after being closed.
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    sock.bind(address)
    sock.listen(5)  # Max of 5 queued connections.
    sock.setblocking(False)
    print("Server listening at", address)

    with sock:
        while True:
            client, addr = await evt_loop.sock_accept(sock)
            print("Connection from", addr)
            evt_loop.create_task(echo_client(evt_loop, client))

async def echo_client(evt_loop: asyncio.AbstractEventLoop, client: socket):
    with client:
        while True:
            data = await evt_loop.sock_recv(client, 10000)
            if data.strip() == b"exit()":
                break

            await evt_loop.sock_sendall(client, b"Got:" + data)

    print("Connection closed.")

if __name__ == "__main__":
    # Manage an event loop manually. The event loop will not close even if 
    #   the tasks are completed.
    evt_loop = asyncio.get_event_loop()
    evt_loop.create_task(echo_server(("", 25000)))
    evt_loop.run_forever()
