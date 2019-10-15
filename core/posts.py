import os
import requests
from .models.auth_model import AuthModel


class file_jpg(bytes):
    def file_json(self):
        files = None
        i_path = '/home/mark/Pictures/car.jpg'
        with open(i_path, 'rb') as f:
            name = os.path.basename(i_path)
            files = {'images[0]': (name, f, 'multipart/form-data')}

            print(f'files = {files}')


class create_posts(object):
    def __init__(self, _data):
        self.__BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if isinstance(_data, dict):
            self.__data = _data
        else:
            raise ValueError('data must be a dict')

    def create_post(self, _type, files=None):
        url = "https://programs.stage.incase.work/api/v1/posts/post/"
        auth_model = AuthModel(os.path.join(self.__BASE_DIR, 'tmp', f'token{_type}'))
        headers = {'Authorization': f'Bearer {auth_model.auth_token}'}
        response = requests.post(url, data=self.__data, files=files, headers=headers)
        print(response.text)

        return response.status_code, response.json(), list(dict(response.json()).keys())

    def get_post(self, _type):
        url = "https://programs.stage.incase.work/api/v1/posts/post/"
        auth_model = AuthModel(os.path.join(self.__BASE_DIR, 'tmp', f'token{_type}'))
        headers = {'Authorization': f'Bearer {auth_model.auth_token}'}
        response = requests.get(url, json=self.__data, headers=headers)
        print(response.text)

        return response.status_code, response.json(), list(dict(response.json()).keys())

    def update_post(self, _type):
        url = "https://programs.stage.incase.work/api/v1/posts/post/"
        auth_model = AuthModel(os.path.join(self.__BASE_DIR, 'tmp', f'token{_type}'))
        headers = {'Authorization': f'Bearer {auth_model.auth_token}'}
        response = requests.put(url, json=self.__data, headers=headers)
        print(response.text)

        return response.status_code, response.json(), list(dict(response.json()).keys())

    def delete_post(self, _type):
        url = "https://programs.stage.incase.work/api/v1/posts/post/"
        auth_model = AuthModel(os.path.join(self.__BASE_DIR, 'tmp', f'token{_type}'))
        headers = {'Authorization': f'Bearer {auth_model.auth_token}'}
        response = requests.delete(url, json=self.__data, headers=headers)
        print(response.text)

        return response.status_code, response.json(), list(dict(response.json()).keys())
