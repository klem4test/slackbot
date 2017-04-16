# coding: utf-8


class ClientError(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return '%s: %s' % (self.name, self.msg)

    @property
    def name(self):
        return self.__class__.__name__


class NotAuthenticatedError(ClientError):
    pass
