#!/usr/env/python3.5
# coding: utf-8

import asyncio
from slack.client import SlackAsyncClient
from bots import TestBot


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    client = SlackAsyncClient('xoxb-167954558500-BHbrVzJTUuMqBfNrzOtRQK5I')
    bot = TestBot(loop, client)
    loop.run_until_complete(bot.run())

    print(bot.client.wss_url)
