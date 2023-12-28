import time

import random

# import threading

import asyncio


async def main_loop_1():
    while True:
        zufall_1 = random.randint(0, 9)
        asyncio.sleep(1)
        return zufall_1


async def main_loop_2():
    while True:
        zufall_2 = print(random.randint(0, 9))
        asyncio.sleep(1)
        return zufall_2


if __name__ == "__main__":
    timer_1 = time.perf_counter()
    asyncio.run(main_loop_1())
    asyncio.run(main_loop_2())
    print(f"Duration time: {time.perf_counter() - timer_1}")
