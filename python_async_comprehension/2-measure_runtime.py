#!/usr/bin/env python3
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    tasks = [async_comprehension() for i in range(4)]

    start = time.time()
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
