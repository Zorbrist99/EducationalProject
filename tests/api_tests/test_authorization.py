import pytest

import requests
from tests.api_tests.conftest import validate_response
from tests.api_tests.responses.post_login_in_lk_auth_bad_response_model import PostLoginInLkAuthBadResponse
from tests.api_tests.responses.post_login_in_lk_response_model import PostLoginInLkResponse
from tests.api_tests.responses.post_login_in_lk_unauthorized_response_model import PostLoginInLkUnauthorizedResponse


# TODO: Понять что не так с фикстурами.
class TestAuthorization:

    @pytest.mark.api_auth
    def test_login_in_lk_habitica(self, credits_for_authorization, api_url):
        """Проверка авторизации в лк"""
        "Метод model_dump возвращает словарь, который передается в метод post"
        res = requests.post(api_url["login"], json=credits_for_authorization.model_dump())

        """
            Метод, который проверяет был ли HTTP запрос успешным и автоматически выбрасывает исключение
            если получен код ошибки. 200-299 - Успех. 400-599 - выбрасывает исключение HTTPError
        """
        res.raise_for_status()
        answer = validate_response(PostLoginInLkResponse, res)

        assert answer.success == True
        assert answer.data.username == 'Sergey_01'
        assert answer.data.newUser == False

    @pytest.mark.api_auth
    def test_auth_bad_request(self, api_url):
        """Проверка, что без логина и пароля авторизация не проходит"""
        res = requests.post(api_url["login"])
        answer = validate_response(PostLoginInLkAuthBadResponse, res)

        assert res.status_code == 400
        assert answer.success == False
        assert answer.error == "BadRequest"
        assert answer.message == 'Invalid request parameters.'
        assert answer.errors[0].message == "Missing username or email."
        assert answer.errors[0].param == "username"
        assert answer.errors[1].message == "Missing password."
        assert answer.errors[1].param == "password"

    @pytest.mark.api_auth
    def test_auth_unauthorized(self, api_url, credits_for_authorization_incorrect):
        """Проверка, что с не валидными данными авторизация не проходит"""
        res = requests.post(api_url["login"], json=credits_for_authorization_incorrect.model_dump())
        answer = validate_response(PostLoginInLkUnauthorizedResponse, res)

        assert res.status_code == 401
        assert answer.success == False
        assert answer.error == 'NotAuthorized'
        assert answer.message == 'Your email, username, or password are incorrect. Please try again or use "Forgot Password."'
