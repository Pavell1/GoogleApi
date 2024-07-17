"""Методы для проверки ответов наших запросов"""
import json


class Checking():

    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Успешно! Статус код = {result.status_code}")

    @staticmethod
    def check_json_token(response, expected_value):
        """Метод для проверки наличия полей в ответе запроса"""
        token = json.loads(response.text)
        assert list(token) == expected_value, 'ОШИБКА, Список полей не совпадает'
        print(list(token))
        print("Все поля присутствуют")


    @staticmethod
    def check_json_value(response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, 'Значения не совпадают'
        print(f"{field_name} верный")

