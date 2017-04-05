# coding: utf-8

from urllib.parse import urljoin
import requests
import conf


class Client:
    def __init__(self, ):
        pass

    def start(self):
        self.__call_method('rtm.start')

    def __call_method(self, slack_method, method, *request_args, **request_kwargs):
        url = urljoin(conf.SLACK_API_URL, slack_method)
        response = getattr(requests, method)(*request_args, **request_kwargs)
