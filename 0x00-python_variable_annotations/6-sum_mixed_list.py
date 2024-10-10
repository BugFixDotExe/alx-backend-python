#!/usr/bin/env python3
from typing import Union, List
'''
    a type-annotated function sum_mixed_list which takes a list mxd_lst of
    integers and floats and returns their sum as a float.
'''


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum_of_mix = 0.0
    '''
        sum_mixed_list: a function that takes in a list and returns float
        Args:
            mxd_list: a type list, that takes in types of int and float
        Returns:
            A float of the sum of both int && list values.
    '''
    return sum(mxd_lst)
