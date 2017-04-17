# coding: utf-8

from aiohttp import ClientSession
from urllib.parse import urljoin
import conf
from log import default_logger
from client import exceptions


class SlackAsyncClient:
    def __init__(self, token: str, logger=default_logger):
        self.token = token
        self.logger = logger
        self.wss_url = None
        self._websocket = None
        self.session = ClientSession()

    async def connect(self):
        await self.rtm_start()
        self._websocket = await self.session.ws_connect(self.wss_url)

    async def terminate(self):
        await self.session.close()

    async def rtm_start(self):
        rtm_response = await self.__rtm(
            'rtm.start', 'get', params={'token': self.token})
        try:
            self.wss_url = rtm_response['url']
        except KeyError:
            if not rtm_response['ok']:
                raise exceptions.NotAuthenticatedError(rtm_response['error'])

    async def __rtm(self, rtm_method: str, http_method: str,
                    params: dict = None):
        self.logger.debug("__rtm %s" % (rtm_method.upper()))

        if not params:
            params = {}

        url = urljoin(conf.SLACK_API_URL, rtm_method)

        method = getattr(self.session, http_method)
        self.logger.info("__rtm %s %s with %s" % (http_method, url, params))
        response = await method(url, params=params)
        return await response.json()

    @property
    def ws(self):
        return self._websocket
