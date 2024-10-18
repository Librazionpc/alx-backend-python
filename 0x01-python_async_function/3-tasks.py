#!/usr/bin/env python3
""" The basics of async in python"""

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Tasks No three """
    task = create_task(wait_random(max_delay))
    return task
