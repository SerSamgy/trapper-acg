import pytest

import dice
import dice_pool


def test_ability_class_has_proper_fields(ability_class):
    assert hasattr(ability_class, 'dice')
    assert hasattr(ability_class, 'modifier')


def test_dice_pool_can_contain_only_ability_objects(pool_class, melee_ability):
    with pytest.raises(dice_pool.NoRequiredFields):
        pool_class([1])

    new_pool = pool_class([melee_ability])
    assert melee_ability == new_pool.pop()


def test_dice_pool_appends_only_ability_objects(pool, melee_ability):
    with pytest.raises(dice_pool.NoRequiredFields):
        pool.append('ability')

    pool.append(melee_ability)
    assert pool.count(melee_ability) == 1


def test_dice_pool_extends_only_by_ability_objects(pool, melee_ability):
    with pytest.raises(dice_pool.NoRequiredFields):
        pool.extend(['ability'])

    pool.extend([melee_ability])
    assert pool.count(melee_ability) == 1


def test_dice_pool_insert_only_ability_objects(pool, melee_ability):
    with pytest.raises(dice_pool.NoRequiredFields):
        pool.insert(0, 'ability')

    pool.insert(1, melee_ability)
    assert pool.count(melee_ability) == 1


@pytest.fixture
def melee_ability(ability_class):
    melee = ability_class(dice.d10, 3)
    return melee
