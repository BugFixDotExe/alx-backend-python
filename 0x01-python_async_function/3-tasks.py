#!/usr/bin/env python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
'''
 function that does not create an async function,
 but uses the regular function syntax to pass into
 task_wait_random with an integer max_delay
 and returns a asyncio.Task.
'''


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
        task_wait_random: a non async function
        Args:
            max_delay: an int type for max delay
        Returns:
            Returns a Asyncio.Task Type
    '''
    return asyncio.Task(wait_random(max_delay))
