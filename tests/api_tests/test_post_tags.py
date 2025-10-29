import requests
from tests.api_tests.conftest import validate_response
from tests.api_tests.helpers import asser_status_code_created, assertion_general_response_fields
from tests.api_tests.responses.get.tag.get_tagId_user_response_model import GetTagIdResponse


class TestPostNewTag:

    def test_create_new_tag(self, api_url, get_header_auth):
        test_data = {"name": "Катер"}

        res = requests.post(api_url['tags'], headers=get_header_auth, json=test_data)
        asser_status_code_created(res)

        val = validate_response(GetTagIdResponse, res)

        assertion_general_response_fields(val)
        assert val.data.name == test_data['name']
