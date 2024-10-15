#!/usr/bin/env python3
'''
A Python that contains a coroutine
a function called async_generator that
takes no arguments.
'''
import asyncio
import random


async def async_generator():
    '''
        async_generator: a function that takes no args
        Args: None
        Returns: None
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
