import requests


class TestGetPets:
    def test_add_new_pat_the_store(self):
        response = requests.post(url='https://petstore3.swagger.io/api/v3/pet',
                                 json={
                                     "id": 111,
                                     "name": "mun",
                                     "category": {
                                         "id": 1,
                                         "name": "Dogs"
                                     },
                                     "photoUrls": [
                                         "primer"
                                     ],
                                     "tags": [
                                         {
                                             "id": 1,
                                             "name": "smart"
                                         }
                                     ],
                                     "status": "available"
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
