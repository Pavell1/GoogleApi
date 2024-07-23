"""Методы для проверки ответов наших запросов"""
import json


# тоже кавычки и название класса более корректно Checker - так как он производит проверки
class Checking():

    # когда в классе только статик методы, обычно не имеет смысла выносить в класс, можно писать как отдельные функции
    @staticmethod
    def check_status_code(result, status_code):  # указываем типы
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Успешно! Статус код = {result.status_code}")

    @staticmethod
    def check_json_token(response, expected_value):  # typing
        """Метод для проверки наличия полей в ответе запроса"""
        token = json.loads(response.text)
        assert list(token) == expected_value, 'ОШИБКА, Список полей не совпадает'
        # для дебага и тренировки принты нормально, но держим в голове что в реальном проекте так не надо
        print(list(token))
        print("Все поля присутствуют")

    @staticmethod
    def check_json_value(response, field_name, expected_value):  # typing
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, 'Значения не совпадают'
        print(f"{field_name} верный")
