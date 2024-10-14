#!/usr/bin/env python3
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random
'''
an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
'''


async def task_wait_n(n: int, max_delay: int):
    '''
        task_wait_n: returns a list of random float
        Args:
            n: represents number of iterations
            max_delay: the max
        Returns:
            A list of randome float values
    '''
    list_of_delays = []
    for i in range(n):
        output = await task_wait_random(max_delay)
        list_of_delays.append(output)
    return list_of_delays
