import os
import requests
from .models.auth_model import AuthModel


class Profile(object):

    def __init__(self):
        self.__BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def get_info(self, _type):
        url = "https://programs.stage.incase.work/api/v1/user/profile/"

        auth_model = AuthModel(os.path.join(self.__BASE_DIR, 'tmp', f'token{_type}'))

        headers = {'Authorization': f'Bearer {auth_model.auth_token}'}
        response = requests.get(url, headers=headers)
        print(response.headers.get('Content-Lenght'))
        print(response.text)

        return response.status_code, list(dict(response.json()).keys())
