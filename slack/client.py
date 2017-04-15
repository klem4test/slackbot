# coding: utf-8

from aiohttp import ClientSession
from urllib.parse import urljoin
import conf
from log import default_logger


class SlackAsyncClient:
    def __init__(self, token: str, logger=default_logger):
        self.token = token
        self.wss_url = None
        self.logger = logger

    async def start(self):
        rtm_response = await self.__rtm(
            'rtm.start', 'get', params={'token': self.token})
        self.wss_url = rtm_response['url']

    async def __rtm(self, rtm_method: str, http_method: str,
                    params: dict = None):
        self.logger.debug("__rtm %s" % (rtm_method.upper()))

        if not params:
            params = {}

        url = urljoin(conf.SLACK_API_URL, rtm_method)
        async with ClientSession() as session:
            method = getattr(session, http_method)
            self.logger.info("__rtm %s %s with %s" % (http_method, url, params))
            response = await method(url, params=params)
            return await response.json()
