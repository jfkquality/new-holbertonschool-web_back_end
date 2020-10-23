#!/usr/bin/env python3
""" 0. Async Generator Comprehensions  """

import asyncio
import random
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """ Yield list of random numbers btwn 0-10 """
    result = []
    async for i in async_generator():
        result.append(i)
    return(result)
