import pytest
import os
import requests
import json
import sys

url1 = 'http://77.120.162.154:9999/categories/'
url2 = 'http://77.120.162.154:9999/books/'

json_books = [
    {
        "Accept-Language": "En",
        "name": "Name 322",
        "category_id": 3,
        "genre": "horror",
        "annotation": ""

    }
]

json_cate = [
    {
        "Accept-Language": "En",
        "name": "Nice",
        "is_archived": 1
    }
]


def test_create_book():
    response = requests.post(url2, json=json_books)
    print(response.text)

