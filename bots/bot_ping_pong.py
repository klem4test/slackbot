# coding: utf-8

from aiohttp.http_websocket import WSMessage
from bots.prototype import SlackBotPrototype


class PingPongBot(SlackBotPrototype):
    async def react(self, msg: WSMessage):
        self.logger.debug("RECEIVE MESSAGE: [%s] %s" % (msg.tp, msg.data))
        data = msg.json()
        if data.get('text') == 'ping':
            self.client.ws.send_json({
                "id": 1,
                "type": "message",
                "channel": data['channel'],
                "text": "Pong, motherfucker!"
            })
