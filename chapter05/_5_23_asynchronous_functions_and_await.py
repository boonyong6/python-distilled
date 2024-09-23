import asyncio

async def make_greeting(name):
    greeting = f"Hello {name}"
    # print(greeting)
    return greeting


coroutine = make_greeting("Guido")
print(coroutine)

result = asyncio.run(coroutine)
print(result)


# await Usage:
async def main():
    for name in ["Paula", "Thomas", "Lewis"]:
        a = await make_greeting(name)  # <--
        print(a)

asyncio.run(main())


# Async protocols
# class AsyncManager(object):  # `object` is the implicit base class for classes that don't specify any base class.
class AsyncManager():
    def __init__(self, x):
        self.x = x
    
    async def yow(self):
        print("yowing...")

    async def __aenter__(self):  # <--
        print("async enter")
        return self
    
    async def __aexit__(self, ty, val, tb):  # <--
        print("async exit")

async def main_mgr():
    async with AsyncManager(42) as mgr:  # <--
        await mgr.yow()

asyncio.run(main_mgr())
