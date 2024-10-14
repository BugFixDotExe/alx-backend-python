#!/usr/bin/env python3
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random
'''
an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
'''


async def wait_n(n: int, max_delay: int):
    '''
        wait_n: an async fun that returns a list of random floats
        Args:
            n: the range for the loop
            max_delay: the upperbound for the randome generator
        Returns:
            A list of randomly choosen floats
    '''
    #TODO: Sort the generated outputs, cant use sort, cocurrency issue huh?
    list_of_delays = []
    for i in range(n):
        output = await wait_random(max_delay)
        list_of_delays.append(output)
    return list_of_delays
