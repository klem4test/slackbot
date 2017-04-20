# coding: utf-8

import asyncio
from aiohttp.http_websocket import WSMessage
from collections import OrderedDict

from tools.exception_handler import ExceptionHandler
from log import default_logger
from client import SlackAsyncClient, exceptions


class SlackBotPrototype(ExceptionHandler):
    exceptions = OrderedDict({
        exceptions.NotAuthenticatedError: {
            '': '_on_err_non_authenticated_client'
        }
    })

    def __init__(self, loop: asyncio.BaseEventLoop, client: SlackAsyncClient,
                 logger=default_logger, loop_wait=1):
        self.client = client
        self.loop = loop
        self.logger = logger
        self.loop_wait = loop_wait

    async def run(self):
        try:
            await self.init()
            await self.life_cycle()
        except Exception as e:
            await self.handle_error(e)
        finally:
            await self.terminate()

    async def init(self):
        await self.client.connect()

    async def life_cycle(self):
        while True:
            self.logger.debug("loop iteration")
            try:
                msg = await self.client.ws.receive()
                await self.react(msg)
                await asyncio.sleep(self.loop_wait)
            except Exception:
                self.logger.exception("Unhandled exception")

    async def terminate(self):
        await self.client.disconnect()

    async def react(self, msg: WSMessage):
        raise NotImplementedError()

    async def _on_err_non_authenticated_client(self, error):
        self.logger.error(str(error))
