import json
import allure

from utils.api import GoogleMapsApi
from utils.checking import Checking

"""Создание, изменение и удаление новой локации"""

# python -m pytest --alluredir=test_results/ tests/test_google_maps_api.py - для создания папки отчетов с аллюром
@allure.epic('Test create new location')
class Test_create_place():  # TestCreatePlace
    @allure.description('Создание места')
    def test_create_new_place(self, create_new_place, delete_place):
        print("Метод POST")
        result_post = create_new_place # GoogleMapsApi создаем в фикстуре и принимаем ее как параметр теста
        Checking.check_status_code(result_post, 200) # тоже самое в чекере
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

    @allure.description('Чтение места')
    def test_read_new_place(self, create_new_place, delete_place):
        place_id_post = create_new_place
        print("Метод GET")
        result_get = GoogleMapsApi.get_new_place(place_id_post)
        Checking.check_status_code(result_get, 200)
        # общее замечание 2 и более параметра лучше передавать с названием
        # Checking.check_status_code(result=result_get, status_code=200) - более читаемо, не нужно смотреть сам метод
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')



    @allure.description('Обновление места')
    def test_update_new_place(self, ):
        place_id = self.test_create_new_place()
        print("Метод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

    @allure.description('Чтение после обновления места')
    def test_read_new_place_after_update(self):
        place_id = self.test_create_new_place()
        print("Метод GET для проверки PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

    @allure.description('Удаление места')
    def test_delete_new_place(self, create_new_place):
        place_id = create_new_place
        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

    @allure.description('Проверка удаления места')
    def test_read_new_place_after_delete(sel, create_new_place):
        place_id = self.test_create_new_place()
        print("Метод GET для проверки DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

    @allure.description('Повторное удаление места')
    def test_delete_new_place_second_once(self, create_new_place):
        place_id = create_new_place
        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 404)
