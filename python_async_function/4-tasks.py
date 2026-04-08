#!/usr/bin/env python3
"""Module for executing multiple asynchronous tasks concurrently.

This module provides functionality to create and manage multiple asyncio
tasks that wait for random delays, allowing them to execute concurrently
and return their results in completion order.
"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """Execute n concurrent tasks, each waiting for a random delay.

    This coroutine creates n asyncio Task objects that each wait for a
    random delay up to max_delay seconds. The tasks are executed
    concurrently and the function returns their results in the order
    they complete.

    Args:
        n: The number of concurrent tasks to create and execute.
        max_delay: The maximum delay in seconds for each task.

    Returns:
        A list of delays (floats) from each completed task, ordered by
        completion time.
    """
    return [
        await result
        for result in asyncio.as_completed(
            task_wait_random(max_delay)
            for _ in range(n)
        )
    ]
