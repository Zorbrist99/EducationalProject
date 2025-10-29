import pytest
import requests

from tests.api_tests.requests.post_login_in_lk_requests_model import LoginRequest
from tests.api_tests.responses.post.auth.post_login_in_lk_response_model import PostLoginInLkResponse
from tests.api_tests.helpers import validate_response
from tests.logger import logger

@pytest.fixture()
def base_url():
    return "https://habitica.com/api/v4/"


@pytest.fixture()
def api_url(base_url):
    return {
        "login": f'{base_url}user/auth/local/login',
        "tags": f'{base_url}tags'
    }


@pytest.fixture
def credits_for_authorization(scope="session"):
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

@pytest.fixture()
def get_header_auth(api_url, credits_for_authorization):
    try:
        logger.info("Попытка авторизации...")
        res = requests.post(api_url["login"], json=credits_for_authorization.model_dump())

        res.raise_for_status()

        val = validate_response(PostLoginInLkResponse, res)

        logger.info("Авторизация пройдена успешно")
        return {
            "X-Api-User": val.data.id,
            "X-Api-Key": val.data.apiToken,
            "X-Client": val.data.username
        }

    except requests.exceptions.HTTPError as e:
        logger.error(f"Ошибка: {e}\n"
              f"Статус код: {res.status_code}. Тело ответа: {res.text}"
              )
        raise

    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка сети при авторизации: {e}")
        raise

    except Exception as e:
        logger.exception(f"Непредвиденная ошибка при авторизации: {e}")
        raise

