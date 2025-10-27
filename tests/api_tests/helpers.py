#TODO: Описать doc-string
def assert_status_code_ok(response):
    assert response.status_code == 200

def assertion_general_response_fields(val):
    assert val.notifications[0].type == "NEW_STUFF"
    assert val.notifications[0].seen == True
    assert val.appVersion == "5.41.5"