# coding: utf-8

from urllib.parse import urljoin
import requests
import conf
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


class SyncClient:
    def __init__(self, token: str):
        self.token = token

    def start(self):
        return self.__rtm(
            'rtm.start', 'get', params={'token': self.token})

    def __rtm(self, rtm_method: str, http_method: str, params: dict = None):
        if not params:
            params = {}

        url = urljoin(conf.SLACK_API_URL, rtm_method)
        response = getattr(requests, http_method)(url, params=params)
        return {
            'code': response.status_code,
            'json': response.json()
        }
