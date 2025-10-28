import requests

from tests.api_tests.conftest import validate_response
from tests.api_tests.helpers import assert_status_code_ok, assertion_general_response_fields, \
    assert_status_code_bad_request
from tests.api_tests.responses.get.tag.get_all_tags_response_model import GetAllTagsResponse
from tests.api_tests.responses.get.tag.get_tagId_random_user_response_model import GetTagIdRandomUserResponse
from tests.api_tests.responses.get.tag.get_tagId_user_response_model import GetTagIdResponse


def test_get_all_user_tags_returns_expected_tags(get_header_auth, api_url):
    """Проверка, что авторизованную пользователю приходят все заведеные теги"""
    res = requests.get(api_url['tags'], headers=get_header_auth)
    assert_status_code_ok(res)

    val = validate_response(GetAllTagsResponse, res)

    tags_name = [tags.name for tags in val.data]

    assertion_general_response_fields(val)
    assert val.success == True
    assert "Работа" in tags_name
    assert "Машина" in tags_name


def test_get_user_tag_by_id_returns_correct_tag(get_header_auth, api_url):
    """Проверка поиска тега по id"""
    id_tag = "8a6a2a7a-62f8-463b-b88e-5951669f6f3e"
    res = requests.get(api_url['tags'] + f'/{id_tag}', headers=get_header_auth)
    assert_status_code_ok(res)

    val = validate_response(GetTagIdResponse, res)

    assertion_general_response_fields(val)
    assert val.success == True
    assert val.data.id == id_tag
    assert val.data.name == 'Работа'


def test_get_user_tag_by_invalid_id_returns_not_found(api_url, get_header_auth):
    """Проверка ошибки валидации с не существующем id"""
    id_tag = "8a6a2a7a-62f8-463b-b88e-000000000000"
    res = requests.get(api_url['tags'] + f'/{id_tag}', headers=get_header_auth)
    assert_status_code_bad_request(res)

    val = validate_response(GetTagIdRandomUserResponse, res)

    assert val.success == False
    assert val.error == "NotFound"
    assert val.message == 'Не был найден тег с таким id.'
