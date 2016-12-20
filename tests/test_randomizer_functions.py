import pytest

import randomizer.dice as dice
import randomizer.functions as rand_functions


def test_add_ability_to_pool(filled_pool):
    assert len(filled_pool) == 3


def test_remove_ability_from_pool(pool_without_ranged):
    assert len(pool_without_ranged) == 2


def test_empty_pool(emptied_pool):
    assert len(emptied_pool) == 0


def test_pop_value_from_pool(popped_value, filled_pool, valeros_support):
    assert popped_value == valeros_support
    assert len(filled_pool) == 2


def test_get_random_ability_value(random_value_from_valeros_support,
                                  possible_valeros_support_values):
    assert random_value_from_valeros_support in possible_valeros_support_values


def test_get_sum_of_random_values_from_pool(possible_values_from_pool,
                                            sum_from_pool, filled_pool):
    assert sum_from_pool in possible_values_from_pool
    assert len(filled_pool) == 0


@pytest.fixture
def dexterity(ability_class):
    return ability_class(dice.d8, 0)


@pytest.fixture
def ranged(ability_class):
    return ability_class(dice.d8, 3)


@pytest.fixture
def valeros_support(ability_class):
    return ability_class(dice.d4, 0)


@pytest.fixture
def filled_pool(pool, ranged, valeros_support, dexterity):
    rand_functions.add_ability_to_pool(pool, dexterity)
    rand_functions.add_ability_to_pool(pool, ranged)
    rand_functions.add_ability_to_pool(pool, valeros_support)

    return pool


@pytest.fixture
def pool_without_ranged(filled_pool, ranged):
    rand_functions.remove_ability_from_pool(filled_pool, ranged)

    return filled_pool


@pytest.fixture
def emptied_pool(filled_pool):
    rand_functions.empty_pool(filled_pool)

    return filled_pool


@pytest.fixture
def popped_value(filled_pool):
    return rand_functions.pop_value_from_pool(filled_pool)


@pytest.fixture
def random_value_from_valeros_support(valeros_support):
    return rand_functions.get_random_ability_value(valeros_support)


@pytest.fixture
def possible_valeros_support_values(valeros_support):
    valeros_support_dice = valeros_support.dice + valeros_support.modifier

    return valeros_support_dice.randomDraw(sorted=True)


@pytest.fixture
def sum_from_pool(filled_pool):
    result = rand_functions.get_sum_of_random_values_from_pool(filled_pool)

    return result


@pytest.fixture
def possible_values_from_pool(filled_pool):
    sum_of_dice_values = sum([x.dice + x.modifier for x in filled_pool])

    return sum_of_dice_values.randomDraw(sorted=True)
