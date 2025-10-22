import pytest

from tests.api.requests.post_login_in_lk_requests_model import LoginRequest


@pytest.fixture
def base_url():
    return "https://habitica.com/api/v4/"


@pytest.fixture()
def api_url(base_url):
    return {
        "login": f'{base_url}user/auth/local/login'
    }


@pytest.fixture
def credits_for_authorization():
    return LoginRequest(
        password='QAguru2024',
        username='beryozkinkonstantin@yandex.ru'
    )

#TODO: Написать фикстуру, которая будет возвращать готовый токен авторизации для проверки других ручек
