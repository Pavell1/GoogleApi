from typing import Optional

import allure
import requests

from utils.logger import Logger

"""Список http методов"""


# скобки не нужны, логичнее назвать HttpClient
class HttpClient:
    # лучше это вынести в инит
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    def __init__(self, base_url: str):
        self.base_url = base_url

    # опять же один статик методы
    def get(self, api_path: str, params: Optional[dict] = None,) -> requests.Response:
        return self._send_request(url=f"{self.base_url}/{api_path}", method="GET", params=params,)
        # result = requests.get(url, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
        # Logger.add_responce(result)
        # return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=HttpClient.headers, cookies=HttpClient.cookie)
            Logger.add_responce(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=HttpClient.headers, cookies=HttpClient.cookie)
            Logger.add_responce(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method="Delete")
            result = requests.delete(url, json=body, headers=HttpClient.headers, cookies=HttpClient.cookie)
            Logger.add_responce(result)
            return result

    def _send_request(self, url: str, method: str, body: Optional[dict] = None, **kwargs,) -> requests.Response:
        with allure.step(method.upper()):
            Logger.add_request(url, method=method)
            result = requests.request(url, method=method, json=body, headers=HttpClient.headers,
                                      cookies=HttpClient.cookie, **kwargs)
            Logger.add_responce(result)
            return result

# HttpClient(base_url="https://google.com")
    # во всех методах один и тот же код, только отличается метод, можно сделать базовый метод для отправки запроса,
    # который будет выпонять общие действия и уже использовать его