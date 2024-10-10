#!/usr/bin/env python3
from typing import List
'''a type-annotated function sum_list which takes
    a list input_list of floats as
    argument and returns their sum as a float.
'''


def sum_list(input_list: List[float]) -> float:
    '''
    sum_list: a function that takes as args a flot of list type returns a float
    Args:
        input_list: a list containing only float types
    Return:
        A sum of the content of the list in float type
    '''
    return sum(input_list)
