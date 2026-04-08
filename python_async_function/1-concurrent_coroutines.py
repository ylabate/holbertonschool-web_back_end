#!/usr/bin/env python3
"""Module for waiting for multiple random async tasks concurrently.

This module provides a function that spawns multiple concurrent coroutines
that wait for random delays and returns their completion times in order.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn n coroutines with random delays and collect results concurrently.

    This function creates n concurrent tasks that each wait for a random
    delay up to max_delay seconds, then returns the results as they complete
    in order of completion.

    Args:
        n: The number of coroutines to spawn.
        max_delay: The maximum delay in seconds for each coroutine.

    Returns:
        A list of floats representing the delay time for each completed
        coroutine, ordered by completion time.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await result for result in asyncio.as_completed(tasks)]
