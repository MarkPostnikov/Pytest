import requests
import os
import json

from .models.config_model import ConfigModel


class Authorization(object):

    def __init__(self):
        self.__BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(self.__BASE_DIR)
        self.__config = ConfigModel()

        if not os.path.exists(os.path.join(self.__BASE_DIR, self.__config.tmp_dir)):
            os.mkdir(self.__config.tmp_dir)

    def auth(self, _type):
        url = 'https://programs.stage.incase.work/api/v1/user/login/'
        data = self.__get_data(_type)

        response = requests.post(url, json=data[f'{_type}'])

        with open(os.path.join(self.__BASE_DIR, self.__config.tmp_dir, f'token{_type}'), 'w', encoding='utf-8') as token:
            token.write(json.dumps(response.json()))

        print(response.headers.get('Content-Length'))
        # response_json = json.loads(response.text)
        print(response.text)

        return response.status_code

    def error(self, _type, field):
        url = 'https://programs.stage.incase.work/api/v1/user/login/'
        data = self.__get_data(_type)

        response = requests.post(url, json={field: data[f'{_type}'][field]})

        print(response.headers.get('Content-Lenght'))
        print(dict(response.json()))

        return response.status_code, dict(response.json())

    def __get_data(self, _type):
        data = None

        with open(os.path.join(self.__BASE_DIR, 'data/login.json'), encoding='utf-8') as file:
            data = json.loads(file.read())

        return data
