import pytest
import requests
import json
import sys
import json
import allure
import uuid

from psycopg2.extensions import JSON
from core.models.auth_model import AuthModel
from core.auth import Authorization
from core.constants.user_type import UserType
from core.utils.list_equals import ListEquals
from core.profile import Profile
from core.program import TestProgram

url = "https://programs.stage.incase.work/api/v1/user/login/"
url2 = "https://programs.stage.incase.work/api/v1/user/profile/"
url3 = "https://programs.stage.incase.work/api/v1/django/manager/programs/new/"
file = open("/home/mark/PycharmProjects/Pytest/data/login.json")
json_input = file.read()
requests_json = json.loads(json_input)
people_string = json_input
data = json.loads(people_string)


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

    def test_profile_info_owner(self):
        profile = Profile()
        status, keys = profile.get_info(UserType.owner)

        assert status == requests.status_codes.codes.OK
        assert ListEquals.equals(keys, self.owner_fields)

    def test_profile_info_acceptor(self):
        profile = Profile()
        status, keys = profile.get_info(UserType.acceptor)

        assert status == requests.status_codes.codes.OK
        assert ListEquals.equals(keys, self.acceptor_fields)
    # def test_profile_info_cardholder(self):
    #     profile = Profile()
    #     status, keys = profile.get_info(UserType.cardholder)
    #
    #     assert status == requests.status_codes.codes.OK
    #     assert ListEquals.equals(keys, self.owner_fields)


def test_bad_create_program():
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


def test_bad_create_program2():
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


def test_bad_create_program3():
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
