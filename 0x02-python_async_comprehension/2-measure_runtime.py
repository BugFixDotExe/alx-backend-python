#!/usr/bin/env python3
'''
A Module or script that:
async_comprehension from the previous file
and write a measure_runtime coroutine that
will execute async_comprehension four times
in parallel using asyncio.gather.
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    measure_runtime: A function that  measure the total runtime and return it.
    Args: None
    Returns:
        Returns measured time it took for the yield & async comprehension
    '''
    s = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    total_time = time.perf_counter() - s
    return total_time
