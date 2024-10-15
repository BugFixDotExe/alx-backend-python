#!/usr/bin/env python3
'''
A Python Script/Module as the case may be that
The coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers.
'''
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''
        async_comprehension: A function that takes no ags but
        returns 10 random numbers.
        Args: None
        Returns:
            Returns the 10 random numbers.
    '''
    random_numbers = [number async for number in async_generator()]
    return random_numbers
