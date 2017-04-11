# coding: utf-8

import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


from urllib.parse import urljoin
import requests
import conf


class SyncClient:
    def __init__(self, token):
        self.token = token

    def start(self):
        return self.__call_method(
            'rtm.start', 'get', params={'token': self.token})

    def __call_method(self, rtm_method, http_method, params: dict = None):
        if not params:
            params = {}

        url = urljoin(conf.SLACK_API_URL, rtm_method)
        response = getattr(requests, http_method)(url, params=params)
        return {
            'code': response.status_code,
            'json': response.json()
        }
