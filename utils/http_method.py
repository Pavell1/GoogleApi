import allure
import  requests

from utils.logger import Logger

"""Список http методов"""
class HttpMethod():
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
            Logger.add_responce(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
            Logger.add_responce(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
            Logger.add_responce(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method="Delete")
            result = requests.delete(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
            Logger.add_responce(result)
            return result