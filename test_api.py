import pytest
import os
import requests
import json
import sys
import json
import allure
import uuid
from PIL import Image
from psycopg2.extensions import JSON
from core.models.auth_model import AuthModel
from core.auth import Authorization
from core.constants.user_type import UserType
from core.utils.list_equals import ListEquals
from core.profile import Profile
from core.program import TestProgram
from core.posts import create_posts

url = "https://programs.stage.incase.work/api/v1/user/login/"
url2 = "https://programs.stage.incase.work/api/v1/user/profile/"
url3 = "https://programs.stage.incase.work/api/v1/django/manager/programs/new/"
url4 = "https://programs.stage.incase.work/api/v1/posts/post/"
file = open("/home/mark/PycharmProjects/Pytest/data/login.json")
json_input = file.read()
requests_json = json.loads(json_input)
people_string = json_input
data = json.loads(people_string)


@allure.step('Login пользователей')
class TestLogin:
    def test_login_owner_company(self):
        authorization = Authorization()

        assert authorization.auth(UserType.owner) == requests.status_codes.codes.OK

    def test_login_acceptor_company(self):
        authorization = Authorization()

        assert authorization.auth(UserType.acceptor) == requests.status_codes.codes.OK

    def test_login_cardholder_personal(self):
        authorization = Authorization()

        assert authorization.auth(UserType.cardholder) == requests.status_codes.codes.OK


@allure.step('Негаивные тесты на овнера')
def test_error_owner():
    error_msg = {
        'title': 'Bad Request', 'status': 400, 'instance': '/api/v1/user/login/',
        'detail': 'Username or password was not provided'
    }

    authorization = Authorization()
    status, msg = authorization.error(_type=UserType.owner, field="username")

    assert status == requests.status_codes.codes.BAD_REQUEST
    assert msg == error_msg

    status, msg = authorization.error(_type=UserType.owner, field="password")

    assert status == requests.status_codes.codes.BAD_REQUEST
    assert msg == error_msg

    # response = requests.post(url, data["1"]["username"]["password"]["user_type = 2"], requests_json)
    # assert response.status_code == 400
    # # assert response.text == ('{"title": "Bad Request", "status": 400, "instance": "/api/v1/user/login/", '
    # #                          '"detail": "Username or password was not provided"}')
    # print(response.headers.get('Content-Lenght'))
    # print(response.text)


@allure.step('Негативные тесты на ацептора')
def test_error_acceptor():
    error_msg = {
        'title': 'Bad Request', 'status': 400, 'instance': '/api/v1/user/login/',
        'detail': 'Username or password was not provided'
    }

    authorization = Authorization()
    status, msg = authorization.error(_type=UserType.acceptor, field="username")

    assert status == requests.status_codes.codes.BAD_REQUEST
    assert msg == error_msg

    authorization = Authorization()
    status, msg = authorization.error(_type=UserType.acceptor, field="password")

    assert status == requests.status_codes.codes.BAD_REQUEST
    assert msg == error_msg

@allure.step('Негативные тесты на картхолдера')
def test_error_cardholder():
    error_msg = {
        'title': 'Bad Request', 'status': 400, 'instance': '/api/v1/user/login/',
        'detail': 'Username or password was not provided'
    }

    authorization = Authorization()
    status, msg = authorization.error(_type=UserType.cardholder, field="username")

    assert status == requests.status_codes.codes.BAD_REQUEST
    assert msg == error_msg

    authorization = Authorization()
    status, msg = authorization.error(_type=UserType.cardholder, field="password")

    assert status == requests.status_codes.codes.BAD_REQUEST
    assert msg == error_msg


@allure.step('Проверка данных при входе овнера, ацептора, кардхолдера')
class TestProfile_info:
    owner_fields = [
        'address', 'avatar', 'birth_date', 'city', 'city_object', 'company_name', 'company_phone',
        'company_phone_code', 'company_reg_number', 'company_vat_number', 'country', 'country_object', 'created',
        'description', 'first_name', 'full_name', 'gender', 'last_name', 'legal_type', 'modified', 'phone',
        'position', 'phone_code', 'state', 'state_object', 'type', 'url', 'username', 'uuid', 'zip'
    ]

    acceptor_fields = [
        'address', 'avatar', 'birth_date', 'city', 'city_object', 'company_name', 'company_phone',
        'company_phone_code', 'company_reg_number', 'company_vat_number', 'country', 'country_object', 'created',
        'description', 'first_name', 'full_name', 'gender', 'last_name', 'legal_type', 'modified', 'phone',
        'position', 'phone_code', 'state', 'state_object', 'type', 'url', 'username', 'uuid', 'zip'
    ]

    # def test_profile_info_owner(self):
    #     profile = Profile()
    #     status, keys = profile.get_info(UserType.owner)
    #
    #     assert status == requests.status_codes.codes.OK
    #     assert ListEquals.equals(keys, self.owner_fields)
    #
    # def test_profile_info_acceptor(self):
    #     profile = Profile()
    #     status, keys = profile.get_info(UserType.acceptor)
    #
    #     assert status == requests.status_codes.codes.OK
    #     assert ListEquals.equals(keys, self.acceptor_fields)
    # def test_profile_info_cardholder(self):
    #     profile = Profile()
    #     status, keys = profile.get_info(UserType.cardholder)
    #
    #     assert status == requests.status_codes.codes.OK
    #     assert ListEquals.equals(keys, self.owner_fields)


@allure.step('Негативные на создание программы')
class test_bad_create_program():
    def test_bad_create_program0(self):
        program_data = {}

        program = TestProgram(program_data)
        error_fields = {
            'title': 'This field is required',
            'status': 'This field is required'
        }

        status, response_data, fields = program.create_program(program_data, UserType.owner)

        assert status == 400
        assert "fields" in fields

        assert ListEquals.equals(list(error_fields.keys()), list(response_data["fields"].keys()))

        for k, v in response_data["fields"].items():
            assert k in error_fields.keys()
            assert error_fields[k] in v if error_fields.get(k) else False

    def test_bad_create_program2(self):
        program_data = {
            'title': 'test1'
        }

        program = TestProgram(program_data)
        error_fields = {

            'status': 'This field is required'
        }

        status, response_data, fields = program.create_program(program_data, UserType.owner)

        assert status == 400
        assert "fields" in fields

        assert ListEquals.equals(list(error_fields.keys()), list(response_data["fields"].keys()))

        for k, v in response_data["fields"].items():
            assert k in error_fields.keys()
            assert error_fields[k] in v if error_fields.get(k) else False

    def test_bad_create_program3(self):
        program_data = {
            'title': 'title_test',
            'status': {
                'id': ''
            }
        }

        program = TestProgram(program_data)
        error_fields = {
            'status': 'A valid integer is required.'
        }

        status, response_data, fields = program.create_program(program_data, UserType.owner)

        assert status == 400

    # assert "fields" in fields
    #
    # assert ListEquals.equals(list(error_fields.keys()), list(response_data["fields"].keys()))
    #
    # for k, v in response_data["fields"].items():
    #     assert k in error_fields.keys()
    #     assert error_fields[k] in v if error_fields.get(k) else False


'''''''''Program Owner posts testing'''''


@allure.step('Негативные тесты на посты')
def test_bad_post1():
    i_path = '/home/mark/Pictures/car.jpg'
    files = None

    post_data = {'text': 'Hi, test',
                 'program_uuid': '',
                 'is_private': 0,
                 'tags': '',
                 'url': ''

                 }

    post = create_posts(post_data)
    status = _data = fields = None

    with open(i_path, 'rb') as f:
        name = os.path.basename(i_path)
        files = {'images[0]': (name, f, 'multipart/form-data')}

        print(f'files = {files}')

        status, _data, fields = post.create_post(_type=UserType.owner, files=files)

    print(status)

    assert status == requests.status_codes.codes.OK


@allure.step('Негативные тесты на посты 2')
def test_bad_post2():
    i_path = '/home/mark/Pictures/car.jpg'
    files = None

    post_data = {'text': '',
                 'program_uuid': '',
                 'is_private': 0,
                 'tags': '',
                 'url': ''

                 }

    post = create_posts(post_data)
    status = _data = fields = None

    with open(i_path, 'rb') as f:
        name = os.path.basename(i_path)
        files = {'images[0]': (name, f, 'multipart/form-data')}

        print(f'files = {files}')

        status, _data, fields = post.create_post(_type=UserType.owner, files=files)

    print(status)

    assert status == requests.status_codes.codes.BAD_REQUEST


@allure.step('Негативные тесты на посты 3')
def test_bad_post3():
    i_path = '/home/mark/Pictures/car.jpg'
    files = None

    post_data = {'text': 'Hi,test',
                 'program_uuid': '',
                 'is_private': -1,
                 'tags': '',
                 'url': ''

                 }

    post = create_posts(post_data)
    status = _data = fields = None

    with open(i_path, 'rb') as f:
        name = os.path.basename(i_path)
        files = {'images[0]': (name, f, 'multipart/form-data')}

        print(f'files = {files}')

        status, _data, fields = post.create_post(_type=UserType.owner, files=files)

    print(status)

    assert status == requests.status_codes.codes.BAD_REQUEST


"""нужно убрать возможность ставить 0 в is_private"""


@allure.step('Негативные тесты на посты 4')
@pytest.mark.xfail
def test_bad_post4():
    i_path = '/home/mark/Pictures/car.jpg'
    files = None

    post_data = {'text': 'Hi,test',
                 'program_uuid': '39884dc4-39bb-4dd6-ab63-8cdcc5174cec',
                 'is_private': 0,
                 'tags': '',
                 'url': ''

                 }

    post = create_posts(post_data)
    status = _data = fields = None

    with open(i_path, 'rb') as f:
        name = os.path.basename(i_path)
        files = {'images[0]': (name, f, 'multipart/form-data')}

        print(f'files = {files}')

        status, _data, fields = post.create_post(_type=UserType.owner, files=files)

    print(status)

    assert status == requests.status_codes.codes.BAD_REQUEST


@allure.step('Негативные тесты на посты 5')
def test_bad_post5():
    i_path = '/home/mark/Pictures/car.jpg'
    files = None

    post_data = {'text': 'Hi,test',
                 'program_uuid': '39884dc4-39bb-4dd6-ab63-8cdcc5174cec',
                 'is_private': 100,
                 'tags': '',
                 'url': ''

                 }

    post = create_posts(post_data)
    status = _data = fields = None

    with open(i_path, 'rb') as f:
        name = os.path.basename(i_path)
        files = {'images[0]': (name, f, 'multipart/form-data')}

        print(f'files = {files}')

        status, _data, fields = post.create_post(_type=UserType.owner, files=files)

    print(status)

    assert status == requests.status_codes.codes.BAD_REQUEST


@allure.step('Негативные тесты на посты 6')
def test_bad_post5():
    i_path = '/home/mark/Pictures/car.jpg'
    files = None

    post_data = {'text': 'Hi,test',
                 'program_uuid': '39884dc4-39bb-4dd6-ab63-8cdcc5174cec',
                 'is_private': -1,
                 'tags': '',
                 'url': ''

                 }

    post = create_posts(post_data)
    status = _data = fields = None

    with open(i_path, 'rb') as f:
        name = os.path.basename(i_path)
        files = {'images[0]': (name, f, 'multipart/form-data')}

        print(f'files = {files}')

        status, _data, fields = post.create_post(_type=UserType.owner, files=files)

    print(status)

    assert status == requests.status_codes.codes.BAD_REQUEST


@allure.step('Негативные тесты на посты 9')
def test_bad_post9():
    i_path = '/home/mark/Pictures/car.jpg'
    files = None

    post_data = {'text': 'Hi,test',
                 'program_uuid': '39884dc4-39bb-4dd6-ab63-8cdcc5174cec',
                 'is_private': -1,
                 'tags': '',
                 'url': ''

                 }

    post = create_posts(post_data)
    status = _data = fields = None

    with open(i_path, 'rb') as f:
        name = os.path.basename(i_path)
        files = {'images[0]': (name, f, 'multipart/form-data')}

        print(f'files = {files}')

        status, _data, fields = post.create_post(_type=UserType.owner, files=files)

    print(status)

    assert status == requests.status_codes.codes.BAD_REQUEST


"""убрать program uuid если пост публичный"""


@pytest.mark.xfail
def test_bad_post6():
    i_path = '/home/mark/Pictures/logo-1.jpg'
    files = None

    post_data = {'text': 'Hi,test',
                 'program_uuid': 'gfgrgegr-77',
                 'is_private': 1,
                 'tags': '',
                 'url': ''

                 }

    post = create_posts(post_data)
    status = _data = fields = None

    with open(i_path, 'rb') as f:
        name = os.path.basename(i_path)
        files = {'images[0]': (name, f, 'multipart/form-data')}

        print(f'files = {files}')

        status, _data, fields = post.create_post(_type=UserType.owner, files=files)

    print(status)

    assert status == requests.status_codes.codes.FORBIDDEN


"""Acceptor posts"""


@allure.step('Негативные тесты на посты акцептора')
def test_bad_post7():
    i_path = '/home/mark/Pictures/logo-1.jpg'
    files = None

    post_data = {'text': 'Hi,test',
                 'program_uuid': 'b0cfa33a-4137-4d70-a162-44be5bfdac81',
                 'is_private': 1,
                 'tags': '',
                 'url': ''

                 }

    post = create_posts(post_data)
    status = _data = fields = None

    with open(i_path, 'rb') as f:
        name = os.path.basename(i_path)
        files = {'images[0]': (name, f, 'multipart/form-data')}

        print(f'files = {files}')

        status, _data, fields = post.create_post(_type=UserType.acceptor, files=files)

    print(status)

    assert status == requests.status_codes.codes.FORBIDDEN
