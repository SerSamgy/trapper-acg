import pytest

import singleton


def test_singleton(singleton_object_1, singleton_object_2):
    assert singleton_object_1 == singleton_object_2

    assert singleton_object_1.value == singleton_object_2.value
    singleton_object_1.value = 10
    assert singleton_object_2.value == 10


@pytest.fixture
def singleton_test_class():
    class TestSingleton(metaclass=singleton.Singleton):
        def __init__(self, value=5):
            self.value = value

    return TestSingleton


@pytest.fixture
def singleton_object_1(singleton_test_class):
    return singleton_test_class()


@pytest.fixture
def singleton_object_2(singleton_test_class):
    return singleton_test_class()
