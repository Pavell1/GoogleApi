from utils.http_method import HttpClient

"""Методы для тестирования гугл мапс"""

# константы в аппер кейсе
base_url = "https://rahulshettyacademy.com"
KEY = "?key=qaclick123"

from enum import StrEnum
from os import environ


class MapsApiRoute(StrEnum):
    CREATE_PLACE = "maps/api/place/add/json"
    GET_RESOURCE = "/maps/api/place/get/json"


class GoogleMapsApi:
    """"Метод для создания новой локации"""

    def __init__(self):
        self.http_client = HttpClient(base_url=base_url)

    def create_new_place(self, l_lat: float, l_lng: int):
        # не надо хакодить дату, т.е.
        # нужно выносить как минимум в параметры денные из этого словаря, чтобы это было более гибко
        json_create_new_place = {

            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        # использование f строки предпочтительнее
        post_url = f"{base_url}{MapsApiRoute.CREATE_PLACE}{KEY}"
        print(post_url)
        # HttpMethod засунуть в __init__
        result_post = self.http_client.post(post_url, json_create_new_place)
        print(result_post.text)
        return result_post

    """"Метод для проверки новой локации"""

    def get_new_place(self, place_id):  # лучше указывать типы, это увеличивает читаемость кода
        return self.http_client.get(api_path=f"{MapsApiRoute.GET_RESOURCE}{KEY}",
                                    params={"place_id": place_id}, )

    @staticmethod
    def put_new_place(place_id):
        put_resourse = "/maps/api/place/update/json"
        put_url = base_url + put_resourse + KEY
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = HttpClient.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        delete_resourse = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resourse + KEY
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id,
        }
        result_delete = HttpClient.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete
