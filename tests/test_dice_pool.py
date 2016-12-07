import pytest

from src import dice, dice_pool


def test_ability_class_has_proper_fields(ability_class):
    assert ability_class._fields == ('dice', 'modifier')


def test_dice_pool_can_contain_only_ability_objects(pool_class, melee_ability):
    with pytest.raises(TypeError):
        pool_class([1])

    new_pool = pool_class([melee_ability])
    assert melee_ability == new_pool.pop()


def test_dice_pool_appends_only_ability_objects(pool, melee_ability):
    with pytest.raises(TypeError):
        pool.append('ability')

    pool.append(melee_ability)
    assert pool.count(melee_ability) == 1


def test_dice_pool_extends_only_by_ability_objects(pool, melee_ability):
    with pytest.raises(TypeError):
        pool.extend(['ability'])

    pool.extend([melee_ability])
    assert pool.count(melee_ability) == 1


def test_dice_pool_insert_only_ability_objects(pool, melee_ability):
    with pytest.raises(TypeError):
        pool.insert(0, 'ability')

    pool.insert(1, melee_ability)
    assert pool.count(melee_ability) == 1


@pytest.fixture
def ability_class():
    return dice_pool.Ability


@pytest.fixture
def melee_ability():
    melee = dice_pool.Ability(dice.d10, 3)
    return melee


@pytest.fixture
def pool_class():
    return dice_pool.DicePool


@pytest.fixture
def pool():
    return dice_pool.DicePool()
