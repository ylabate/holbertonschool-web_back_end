# python async function

## 0-basic_async_syntax.py
Coroutine that asynchronously waits for a random amount of time between 0 and max_delay seconds, then returns the actual delay.

## 1-concurrent_coroutines.py
Asynchronous function that spawns and manages n concurrent coroutines using wait_random, returning their completion times in the order they finish.

## 2-measure_runtime.py
Function that measures the average runtime of executing n concurrent coroutines by dividing total execution time by the number of coroutines.

## 3-tasks.py
Function that creates and returns an asyncio Task object wrapping a wait_random coroutine for task-based asynchronous execution.

## 4-tasks.py
Asynchronous function that executes n asyncio Task objects concurrently using task_wait_random and returns their completion times in completion order.