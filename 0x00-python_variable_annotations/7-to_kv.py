#!/usr/bin/env python3
from typing import Union, Tuple

''' a type-annotated function to_kv that takes a string k and
    an int OR float v as arguments and returns a tuple'''


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''A function that taken in str and a Union return a Tuple'''
    '''
        Args:
            k: A string argunment
            v: A Union Data Struct accepting types int || float
        Return:
            A tuple having types str && float
    '''
    return (k, v**2)
