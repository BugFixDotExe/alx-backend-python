#!/usr/bin/env python3
'''
 a measure_time function with integers n
 and max_delay as arguments that measures
 the total execution time for wait_n(n, max_delay),
 and returns total_time / n.
 The function returns a float.
'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
        measure_time: a function that measures the runtime of a function
        Args:
            n: the number of times to run the loop
            max_delay: the largest or inbound value
        Returns: the total_time / n
    '''
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - s
    return total_time / n
