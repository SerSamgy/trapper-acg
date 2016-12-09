import pytest

import dice
import dice_pool


@pytest.fixture
def dice_d4():
    return dice.d4.copy()


@pytest.fixture
def dice_d6():
    return dice.d6.copy()


@pytest.fixture
def dice_d8():
    return dice.d8.copy()


@pytest.fixture
def dice_d10():
    return dice.d10.copy()


@pytest.fixture
def dice_d12():
    return dice.d12.copy()


@pytest.fixture
def ability_class():
    return dice_pool.Ability


@pytest.fixture
def pool_class():
    return dice_pool.DicePool


@pytest.fixture
def pool(pool_class):
    return pool_class()
