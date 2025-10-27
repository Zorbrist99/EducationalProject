# TODO: Написать тест создания задачи пользователя, используя модель.
import requests


def test_create_task(get_token_auth, api_url):
    res = requests.get(api_url['tags'],headers={"X-API-Token": get_token_auth})

    assert res.status_code == 200
