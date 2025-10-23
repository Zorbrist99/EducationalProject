import pytest

import requests
from tests.api.requests.post_login_in_lk_requests_model import LoginRequest
from tests.api.responses.post_login_in_lk_auth_bad_response import PostLoginInLkAuthBadResponse
from tests.api.responses.post_login_in_lk_response_model import PostLoginInLkResponse


@pytest.fixture
def credits_for_authorization_incorrect():
    return LoginRequest(
        password='QAguru3333',
        username='beryozkinkonstantin@yandex.ru'
    )


def test_login_in_lk_habitica(credits_for_authorization, api_url):
    "Метод model_dump возвращает словарь, который передается в метод post"
    res = requests.post(api_url["login"], json=credits_for_authorization.model_dump())

    """
        Метод, который проверяет был ли HTTP запрос успешным и автоматически выбрасывает исключение
        если получен код ошибки. 200-299 - Успех. 400-599 - выбрасывает исключение HTTPError
    """
    res.raise_for_status()

    validate_response = PostLoginInLkResponse(**res.json())

    assert validate_response.success == True
    assert validate_response.data.username == 'Sergey_01'
    assert validate_response.data.newUser == False


# TODO:
def test_auth_bad_request(api_url):
    res = requests.post(api_url["login"])
    validate_response = PostLoginInLkAuthBadResponse(**res.json())

    assert validate_response.success == False
    assert validate_response.error == "BadRequest"
    assert validate_response.message == 'Invalid request parameters.'
    assert validate_response.errors[0].message == "Missing username or email."
    assert validate_response.errors[0].param == "Missing username or email."
    assert res.status_code == 400


def test_auth_unauthorized(api_url, credits_for_authorization_incorrect):
    res = requests.post(api_url["login"], json=credits_for_authorization_incorrect.model_dump())
    assert res.status_code == 401
