#!/usr/bin/env python3
"""
Coroutine that collects random numbers using async comprehension.
"""
from typing import List
from importlib import import_module

''' 
Dynamically importing async_generator from the previous module
'''
async_generator = import_module('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [number async for number in async_generator()]
