# python async comprehension

## 0-async_generator.py
Asynchronous generator coroutine that yields random numbers between 0 and 10 at one-second intervals for a total of 10 iterations.

## 1-async_comprehension.py
Coroutine that collects 10 random numbers using an async comprehension over the async generator.

## 2-measure_runtime.py
Coroutine that executes async_comprehension four times in parallel using asyncio.gather and measures the total runtime.