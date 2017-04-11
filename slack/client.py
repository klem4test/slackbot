# coding: utf-8

from aiohttp import ClientSession
from urllib.parse import urljoin
import conf


class SlackAsyncClient:
    def __init__(self, token: str):
        self.token = token
        self.wss_url = None

    async def start(self):
        rtm_response = await self.__rtm(
            'rtm.start', 'get', params={'token': self.token})
        self.wss_url = rtm_response['url']

    async def __rtm(self, rtm_method: str, http_method: str,
                    params: dict = None):
        if not params:
            params = {}

        url = urljoin(conf.SLACK_API_URL, rtm_method)
        async with ClientSession() as session:
            method = getattr(session, http_method)
            response = await method(url, params=params)
            return await response.json()
