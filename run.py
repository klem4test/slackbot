#!/usr/env/python3.5
# coding: utf-8

import sys
import asyncio

from client import SlackAsyncClient
import bots
from log import default_logger as logger


if __name__ == '__main__':
    bot_cls_name, token = sys.argv[1], sys.argv[2]
    bot_cls = getattr(bots, bot_cls_name)

    loop = asyncio.get_event_loop()

    client = SlackAsyncClient(token)
    bot = bot_cls(loop, client)
    loop.run_until_complete(bot.run())

    logger.info(bot.client.wss_url)
