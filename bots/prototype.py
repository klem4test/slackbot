# coding: utf-8

import asyncio
from slack.client import SlackAsyncClient


class SlackBotPrototype:
    def __init__(self, loop: asyncio.BaseEventLoop, client: SlackAsyncClient):
        self.client = client
        self.loop = loop

    async def run(self):
        await self.client.start()
