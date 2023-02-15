#!/usr/bin/env python3
""" multiple coroutines at the same time with async """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        n: number of seconds to wait
        max_delay: maximum delay in seconds
    Returns (float) : List of delays
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
