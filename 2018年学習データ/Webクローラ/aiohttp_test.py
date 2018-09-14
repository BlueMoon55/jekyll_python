# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:34:53 2018

@author: T6014250
"""

import asyncio
import aiohttp
def get_body(url):
    response = yield from aiohttp.request('GET', url)
    return (yield from response.text())
loop = asyncio.get_event_loop()
loop.run_until_complete(get_body('http://qiita.com/advent-calendar/2014'))
