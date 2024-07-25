import pytest
import requests

from utils.api import GoogleMapsApi


@pytest.fixture(scope="session")
def google_api() -> GoogleMapsApi:
    return GoogleMapsApi()


@pytest.fixture
def create_new_place(google_api)  -> requests.Response:
    return google_api.create_new_place()


@pytest.fixture
def delete_place(create_new_place, google_api):
    yield
    google_api.delete_new_place(create_new_place)


import pytest


@pytest.fixture
def read():
    print("\n\nroot_place\n\n")
