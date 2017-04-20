# coding: utf-8

from bots.prototype import SlackBotPrototype


class VoiceGenBot(SlackBotPrototype):
    def __init__(self, loop, client, yandex_token, **kwargs):
        super(VoiceGenBot, self).__init__(loop, client, **kwargs)

    def react(self, msg):
