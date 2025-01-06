import asyncio


async def baz() -> str:
    print("Before Sleep")
    await asyncio.sleep(1)
    print("After Sleep")
    return "Hello world"


async def main():
    r = baz()
    print("coroutine object baz: ", r)
    result = await r
    print("result: ", result)


if __name__ == "__main__":
    asyncio.run(main())
