import pytest
import requests
from pydantic import BaseModel, ValidationError
from requests import Response

from tests.api_tests.requests.post_login_in_lk_requests_model import LoginRequest
from tests.api_tests.responses.post.auth.post_login_in_lk_response_model import PostLoginInLkResponse


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


# TODO: Не очень хорошая реализация, на мой взгляд можно лучше. Особенно мне не нравится момент с отображением exception
@pytest.fixture
def get_header_auth(api_url, credits_for_authorization):
    try:
        print("Попытка авторизации...")
        res = requests.post(api_url["login"], json=credits_for_authorization.model_dump())

        if res.status_code != 200:
            raise ValueError(f"Статус код {res.status_code}, ожидали 200")

        val = validate_response(PostLoginInLkResponse, res)

        print("Авторизация пройдена успешно")
        return {
            "X-Api-User": val.data.id,
            "X-Api-Key": val.data.apiToken,
            "X-Client": val.data.username
        }

    except ValueError as e:
        print(f"Ошибка: {e}",
              f"Тело ответа: {res.text}"
              )
        raise


# TODO: Сделал логирование, но мне не нравится как в логах выводится сообщение об ошибке
def validate_response(model: type[BaseModel], response: Response):
    try:
        return model.model_validate(response.json())

    except ValidationError as e:
        print(f"Ошибка: {e}")
        raise
