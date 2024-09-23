import asyncio

class Awaitable:
    # Must be a generator.
    def __await__(self):
        print("About to await")
        yield  # <--
        print("Resuming")

# Function compatible with "await". Returns an "awaitable".
def func():
    return Awaitable()

async def main():
    await func()

asyncio.run(main())
