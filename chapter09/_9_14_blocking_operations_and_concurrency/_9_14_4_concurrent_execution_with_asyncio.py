import asyncio
from .common import echo_server


async def reader1(sock):
    evt_loop = asyncio.get_event_loop()
    while data := await evt_loop.sock_recv(sock, 8192):
        print("reader1 got:", data)


async def reader2(sock):
    evt_loop = asyncio.get_event_loop()
    while data := await evt_loop.sock_recv(sock, 8192):
        print("reader2 got:", data)


async def main(sock1, sock2):
    evt_loop = asyncio.get_event_loop()
    t1 = evt_loop.create_task(reader1(sock1))
    t2 = evt_loop.create_task(reader2(sock2))

    # Wait for the tasks to finish
    await t1
    await t2


if __name__ == "__main__":
    sock1, sock2 = echo_server(("", 25000))

    asyncio.run(main(sock1, sock2))
