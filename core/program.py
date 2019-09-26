import os
import requests
from .models.auth_model import AuthModel

class TestProgram(object):

    def __init__(self, _data):
        self.__BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if isinstance(_data, dict):
            self.__data = _data
        else:
            raise ValueError('data must be a dict')

    def get_program(self, _type):
        url = 'https://programs.stage.incase.work/api/v1/user/profile/'

        auth_model = AuthModel(os.path.join(self.__BASE_DIR, 'tmp', f'token{_type}'))

        headers = {'Authorization': f'Bearer {auth_model.auth_token}'}
        response = requests.get(url, headers=headers)
        print(response.headers.get('Content-Lenght'))
        print(response.text)

        return response.status_code, list(dict(response.json()).keys())

    def create_program(self, data,  _type):
        url = 'https://programs.stage.incase.work/api/v1/django/manager/programs/'

        auth_model = AuthModel(os.path.join(self.__BASE_DIR, 'tmp', f'token{_type}'))

        headers = {'Authorization': f'Bearer {auth_model.auth_token}'}

        response = requests.post(url, json=self.__data, headers=headers)
        print(response.headers.get('Content-Lenght'))
        print(response.text)

        return response.status_code, response.json(), list(dict(response.json()).keys())

    def update_program(self, uuid, data, _type):
        url = f'https://programs.stage.incase.work/api/v1/django/manager/programs/{uuid}'

        auth_model = AuthModel(os.path.join(self.__BASE_DIR, 'tmp', f'token{_type}'))

        headers = {'Authorization': f'Bearer {auth_model.auth_token}'}
        response = requests.put(url, json=self.__data, headers=headers)
        print(response.headers.get('Content-Lenght'))
        print(response.text)

        return response.status_code, list(dict(response.json()).keys())

    def delete_program(self, _type):
        url = 'https://programs.stage.incase.work/api/v1/django/manager/programs/'

        auth_model = AuthModel(os.path.join(self.__BASE_DIR, 'tmp', f'token{_type}'))

        headers = {'Authorization': f'Bearer {auth_model.auth_token}'}
        response = requests.delete(url, headers=headers)
        print(response.headers.get('Content-Lenght'))
        print(response.text)

        return response.status_code, list(dict(response.json()).keys())
