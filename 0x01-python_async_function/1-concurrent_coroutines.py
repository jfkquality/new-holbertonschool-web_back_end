#!/usr/bin/env python3
""" 1. Let's execute multiple coroutines at the same time with async """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List:
    """ Run aWait n times concurrently """

    result = []

    for i in range(n):
        result.append(await wait_random(max_delay))

    return result
