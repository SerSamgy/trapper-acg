import pytest

import dice_pool


@pytest.fixture
def ability_class():
    return dice_pool.Ability


@pytest.fixture
def pool_class():
    return dice_pool.DicePool


@pytest.fixture
def pool(pool_class):
    instance = pool_class()
    yield instance

    instance.clear()
