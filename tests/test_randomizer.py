import pytest

import dice
import randomizer


def test_add_ability_to_pool(ability_d4):
    randomizer.add_ability_to_pool(ability_d4)
    assert len(randomizer.Pool) == 1


def test_remove_ability_from_pool(ability_d4):
    initial_len = len(randomizer.Pool)

    randomizer.remove_ability_from_pool(ability_d4)
    assert len(randomizer.Pool) < initial_len


def test_empty_pool(ability_d4, ability_d8):
    randomizer.add_ability_to_pool(ability_d4)
    randomizer.add_ability_to_pool(ability_d8)

    randomizer.empty_pool()
    assert len(randomizer.Pool) == 0


def test_pop_value_from_pool(ability_d8):
    randomizer.add_ability_to_pool(ability_d8)

    pop_value = randomizer.pop_value_from_pool()
    assert pop_value == ability_d8
    assert len(randomizer.Pool) == 0


def test_get_random_ability_value(ability_d4):
    random_value = randomizer.get_random_ability_value(ability_d4)

    assert random_value in range(1, 6)


def test_get_sum_of_random_values_from_pool(ability_d4,
                                            ability_d4_without_modifier):
    randomizer.add_ability_to_pool(ability_d4)
    randomizer.add_ability_to_pool(ability_d4_without_modifier)

    sum_from_pool = randomizer.get_sum_of_random_values_from_pool()
    assert sum_from_pool in range(2, 10)
    assert len(randomizer.Pool) == 0


@pytest.fixture
def ability_d4(ability_class):
    return ability_class(dice.d4, 1)


@pytest.fixture
def ability_d4_without_modifier(ability_class):
    return ability_class(dice.d4, 0)


@pytest.fixture
def ability_d8(ability_class):
    return ability_class(dice.d8, 2)
