import allure
import  requests

from utils.logger import Logger

"""Список http методов"""
# скобки не нужны, логичнее назвать HttpClient
class HttpMethod():
    # лучше это вынести в инит
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    # опять же один статик методы
    @staticmethod
    def get(url): # typing
        with allure.step("GET"):
            # logger вынести в инит, а не обращаться к классу всегда
            # базовую часть урла лучше вынести в инит и принимать как параметр
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

    # во всех методах один и тот же код, только отличается метод, можно сделать базовый метод для отправки запроса,
    # который будет выпонять общие действия и уже использовать его