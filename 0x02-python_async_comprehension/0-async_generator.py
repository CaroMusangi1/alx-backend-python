#!/usr/bin/env python3
'''Module: async generator example'''
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that asynchronously generates 10 random floating-point numbers
    between 0 and 10, with a 1-second delay between each number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
