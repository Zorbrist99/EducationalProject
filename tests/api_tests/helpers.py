def assert_status_code_ok(response):
    """Проверка что статус код 200 Ок"""
    assert response.status_code == 200

def asser_status_code_created(response):
    """Проверка что статус код 201 Created"""
    assert response.status_code == 201

def assert_status_code_bad_request(response):
    """Проверка что статус код 404 BadRequest"""
    assert response.status_code == 404

def assertion_general_response_fields(val):
    """Проверка повторяющихся полей в ответе /tags"""
    assert val.success == True
    assert val.notifications[0].type == "NEW_STUFF"
    assert val.notifications[0].seen == True
    assert val.appVersion == "5.41.5"