#!/usr/bin/env python3

"""Task 0's module
The coroutine will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """This coroutine generates a sequence of 10 Numbers.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
