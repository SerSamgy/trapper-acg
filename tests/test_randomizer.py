import pytest


# FIXME: uncommit this and fix tests
# def test_add_ability_to_pool(pool, ability_d4):
#     randomizer.add_ability_to_pool(pool, ability_d4)
#     assert len(pool) == 1
#
#
# def test_remove_ability_from_pool(pool_class, ability_d4):
#     new_pool = pool_class([ability_d4])
#     initial_len = len(new_pool)
#
#     randomizer.remove_ability_from_pool(new_pool, ability_d4)
#     assert len(new_pool) < initial_len
#
#
# def test_empty_pool(pool_class, ability_d4, ability_d8):
#     new_pool = pool_class([ability_d4, ability_d8])
#
#     randomizer.empty_pool(new_pool)
#     assert len(new_pool) == 0
#
#
# def test_shuffle_ability_dice(dice_d4, ability_d4):
#     ability_dice = ability_d4.dice
#
#     randomizer.shuffle_ability_dice(ability_dice)
#     assert ability_dice != dice_d4
#
#
# def test_shuffle_pool(pool_class, ability_d4, ability_d8, dice_d4, dice_d8):
#     new_pool = pool_class([ability_d4, ability_d8])
#
#     randomizer.shuffle_pool_dices(new_pool)
#     assert ability_d4.dice != dice_d4
#     assert ability_d8.dice != dice_d8
#
#
# def test_get_random_ability_value(ability_d4):
#     random_value = randomizer.get_random_ability_value(ability_d4)
#
#     assert random_value in range(1, 6)
#
#
# def test_get_sum_of_random_values_from_pool(pool_class, ability_d4,
#                                             ability_d4_without_modifier):
#     new_pool = pool_class([ability_d4, ability_d4_without_modifier])
#
#     sum_from_pool = randomizer.get_sum_of_random_values_from_pool(new_pool)
#     assert sum_from_pool in range(2, 10)


@pytest.fixture
def ability_d4(dice_d4, ability_class):
    return ability_class(dice_d4.copy(), 1)


@pytest.fixture
def ability_d4_without_modifier(dice_d4, ability_class):
    return ability_class(dice_d4.copy(), 0)


@pytest.fixture
def ability_d8(dice_d8, ability_class):
    return ability_class(dice_d8.copy(), 2)
