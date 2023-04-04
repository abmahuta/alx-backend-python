#!/usr/bin/env python3
'''waits for a random delay
between 0 and max_delay
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    delay_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return delay_time
