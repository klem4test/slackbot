# coding: utf-8

from collections import OrderedDict


async def _raise(e):
    raise e


class ExceptionHandler:
    exceptions = OrderedDict({
            Exception: OrderedDict({'': _raise})
    })

    async def handle_error(self, error: Exception):
        handler = self.get_handler(error)
        if handler:
            await handler(error)
        else:
            raise error

    def get_handler(self, error):
        err_message = error.args[0] if error.args else ''
        try:
            choices = self.exceptions[type(error)]
            for msg, handler_name in choices.items():
                if msg in err_message:
                    return getattr(self, handler_name)
        except KeyError:
            return None
        return None
