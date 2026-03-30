import requests
import pytest

BASE_URL = 'https://demoqa.com/BookStore/v1/Books'
def test_get_all_book():

    response = requests.get(BASE_URL)

    assert response.status_code == 200
    print(response.json())
    print(response.text)
