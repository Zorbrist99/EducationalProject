import json
import requests
import pytest

def json_print(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))

def test_get_single_user():
    res = requests.get("https://reqres.in/api/users/2")
    json_print(res.json())

    assert res.status_code == 200

