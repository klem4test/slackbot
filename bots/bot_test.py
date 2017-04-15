# coding: utf-8
from aiohttp.http_websocket import WSMessage
from bots.prototype import SlackBotPrototype


class TestBot(SlackBotPrototype):
    async def process_message(self, msg: WSMessage):
        self.logger.info("RECEIVE MESSAGE: [%s] %s" % (msg.tp, msg.data))
