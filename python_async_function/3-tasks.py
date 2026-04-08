#!/usr/bin/env python3
"""Module for creating async tasks with type annotations.

This module provides a function that wraps an async coroutine
into an asyncio.Task for concurrent execution.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio Task wrapping wait_random coroutine.

    This function takes a maximum delay value and returns an asyncio Task
    that will execute the wait_random coroutine concurrently.

    Args:
        max_delay: An integer representing the maximum delay in seconds.

    Returns:
        An asyncio.Task object that wraps the wait_random coroutine.
    """
    return asyncio.Task(wait_random(max_delay))
