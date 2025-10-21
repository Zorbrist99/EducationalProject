import json
import requests
import pytest


def json_print(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))


# TODO:сделать валидацию ответа от api, при помощи pydantica.
def test_get_single_user():
    res = requests.get("https://reqres.in/api/users/2")
    """
    Метод, который проверяет был ли HTTP запрос успешным и автоматически выбрасывает исключение
    если получен код ошибки. 200-299 - Успех. 400-599 - выбрасывает исключение HTTPError
    """
    res.raise_for_status()
