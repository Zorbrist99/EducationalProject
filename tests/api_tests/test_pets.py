import pytest
import requests


@pytest.mark.test
class TestGetPets:
    def test_add_new_pat_the_store(self,
                                   id: int = 111,
                                   name: str = "mun",
                                   category_id: int = 1,
                                   category_name: str = "Dogs",
                                   photo_urls: str = "primer",
                                   tags_id: int = 1,
                                   tags_name: str = "smart",
                                   status: str = "available"):
        response = requests.post(url='https://petstore3.swagger.io/api/v3/pet',
                                 json={
                                     "id": id,
                                     "name": name,
                                     "category": {
                                         "id": category_id,
                                         "name": category_name
                                     },
                                     "photoUrls": [
                                         photo_urls
                                     ],
                                     "tags": [
                                         {
                                             "id": tags_id,
                                             "name": tags_name
                                         }
                                     ],
                                     "status": status
                                 })

        assert response.status_code == 200

    def test_get_pet_by_pet_id(self, pet_id: int = 11):
        response = requests.get(url=f'https://petstore3.swagger.io/api/v3/pet/{pet_id}')

        assert response.status_code == 200, f"Пользователь с pet_id= {pet_id} не найден"

    def test_delete_pet_by_pet_id(self, pet_id: int = 11):
        response = requests.delete(url=f'https://petstore3.swagger.io/api/v3/pet/{pet_id}')

        assert response.status_code == 200

# testGetPets = TestGetPets()
# testGetPets.test_add_new_pat_the_store()
# testGetPets.test_get_pet_by_pet_id()
# testGetPets.test_delete_pet_by_pet_id()
# testGetPets.test_get_pet_by_pet_id()
