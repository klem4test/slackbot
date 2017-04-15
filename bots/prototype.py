# coding: utf-8

import asyncio
import aiohttp
from aiohttp.http_websocket import WSMessage
from log import default_logger
from slack.client import SlackAsyncClient


class SlackBotPrototype:
    def __init__(self, loop: asyncio.BaseEventLoop, client: SlackAsyncClient,
                 logger=default_logger, loop_wait=1):
        self.client = client
        self.loop = loop
        self.logger = logger
        self.loop_wait = loop_wait

    async def life_cycle(self):
        await self.client.start()
        session = aiohttp.ClientSession()

        ws = await session.ws_connect(self.client.wss_url)

        while True:
            self.logger.debug("loop iteration")
            try:
                msg = await ws.receive()
                await self.react(msg)
                await asyncio.sleep(self.loop_wait)
            except Exception:
                self.logger.exception("Unhandled exception")

    async def react(self, msg: WSMessage):
        raise NotImplementedError()
