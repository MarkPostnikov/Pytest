import json


class AuthModel(object):

    def __init__(self, path):
        self.auth_token = None
        self.refresh_token = None

        self.__set_tokens(path=path)

    def __set_tokens(self, path):
        with open(path, encoding='utf-8') as file:
            data = json.loads(file.read())

            if data:
                self.auth_token = data.get("auth_token", None)
                self.refresh_token = data.get("refresh_token", None)
