#!/usr/bin/env python3
"""Module providing asynchronous function with random wait capability.

This module contains a coroutine that demonstrates basic async syntax
and asynchronous sleep functionality in Python.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random amount of time and return the wait duration.

    This coroutine generates a random delay between 0 and max_delay
    seconds, asynchronously sleeps for that duration, and then returns
    the actual delay that was used.

    Args:
        max_delay: The maximum number of seconds to wait. Defaults to 10.

    Returns:
        The actual number of seconds the coroutine waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
