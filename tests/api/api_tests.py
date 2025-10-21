
import requests
from tests.api.requests.post_login_in_lk_requests_model import LoginRequest
from tests.api.responses.post_login_in_lk_response_model import PostLoginInLkResponse


#TODO: нужно вынести работу с кредами и самим запросом из теста
def test_login_in_lk_habitica():
    request_data = LoginRequest(password='QAguru2024', username='beryozkinkonstantin@yandex.ru')
    "Метод model_dump возвращает словарь, который передается в метод post"
    res = requests.post("https://habitica.com/api/v4/user/auth/local/login", json=request_data.model_dump())
    """
        Метод, который проверяет был ли HTTP запрос успешным и автоматически выбрасывает исключение
        если получен код ошибки. 200-299 - Успех. 400-599 - выбрасывает исключение HTTPError
    """
    res.raise_for_status()

    validate_response = PostLoginInLkResponse(**res.json())

    print(validate_response)
    assert validate_response.success == True
    assert validate_response.data.username == 'Sergey_01'
