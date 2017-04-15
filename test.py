#!/usr/env/python3.5
# coding: utf-8

import asyncio

from slack.client import SlackAsyncClient
from bots import TestBot
from log import default_logger as logger

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    client = SlackAsyncClient('xoxb-167954558500-gynLZemDSn3WpVtbSf2oeiX7')
    bot = TestBot(loop, client)
    loop.run_until_complete(bot.run())

    logger.info(bot.client.wss_url)
