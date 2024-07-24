import pytest


@pytest.fixture
def read():
    print("\n\ntest place\n\n")

def test(read):
    pass