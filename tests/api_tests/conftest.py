import pytest
import requests
from pydantic import BaseModel
from requests import Response

from tests.api_tests.requests.post_login_in_lk_requests_model import LoginRequest
from tests.api_tests.responses.post_login_in_lk_response_model import PostLoginInLkResponse


@pytest.fixture
def base_url():
    return "https://habitica.com/api/v4/"


@pytest.fixture()
def api_url(base_url):
    return {
        "login": f'{base_url}user/auth/local/login',
        "tags": f'{base_url}tags'
    }


@pytest.fixture
def credits_for_authorization():
    return LoginRequest(
        password='QAguru2024',
        username='beryozkinkonstantin@yandex.ru'
    )


@pytest.fixture
def credits_for_authorization_incorrect():
    return LoginRequest(
        password='QAguru3333',
        username='beryozkinkonstantin@yandex.ru'
    )


# TODO: Написать фикстуру, которая будет возвращать готовый токен авторизации для проверки других ручек
@pytest.fixture
def get_token_auth(api_url, credits_for_authorization):

    res = requests.post(api_url["login"], json=credits_for_authorization.model_dump())
    val = validate_response(PostLoginInLkResponse, res)

    return val.data.apiToken

# TODO: Сделать красивое логирование, посмотреть гпт
def validate_response(model: type[BaseModel], response: Response):
    return model.model_validate(response.json())
