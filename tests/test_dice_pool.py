import pytest

import exceptions
import randomizer.dice as dice
import randomizer.dice_pool as dice_pool


def test_ability_has_required_fields(ability_has_required_fields_check):
    assert ability_has_required_fields_check is True


def test_object_with_ability_interface_has_required_fields(
        object_with_ability_interface_has_required_fields_check):
    assert object_with_ability_interface_has_required_fields_check is True


def test_object_without_ability_interface_has_no_required_fields(
        object_without_ability_interface_has_required_fields_check):
    assert object_without_ability_interface_has_required_fields_check is False


def test_assert_all_objects_are_dice_for_correct_sequence(correct_sequence):
    assert dice_pool.assert_all_objects_are_dice(correct_sequence) is None


def test_assert_all_objects_are_dice_for_incorrect_sequence(incorrect_sequence):
    with pytest.raises(exceptions.NoRequiredFields):
        dice_pool.assert_all_objects_are_dice(incorrect_sequence)


def test_dice_pool_is_singleton(pool_class, pool):
    new_pool = pool_class()

    assert new_pool is pool


def test_dice_pool_appends_only_ability_objects(pool, melee_ability):
    with pytest.raises(exceptions.NoRequiredFields):
        pool.append('ability')

    pool.append(melee_ability)
    assert pool.count(melee_ability) == 1


def test_dice_pool_extends_only_by_ability_objects(pool, melee_ability):
    with pytest.raises(exceptions.NoRequiredFields):
        pool.extend(['ability'])

    pool.extend([melee_ability])
    assert pool.count(melee_ability) == 1


def test_dice_pool_inserts_only_ability_objects(pool, melee_ability):
    with pytest.raises(exceptions.NoRequiredFields):
        pool.insert(0, 'ability')

    pool.insert(0, melee_ability)
    assert pool.count(melee_ability) == 1


@pytest.fixture
def melee_ability(ability_class):
    melee = ability_class(dice.d10, 3)
    return melee


@pytest.fixture
def ability_has_required_fields_check(melee_ability):
    return dice_pool.has_required_fields(melee_ability)


@pytest.fixture
def object_without_ability_interface():
    obj = type('TestObject', (), {})
    return obj


@pytest.fixture
def object_with_ability_interface(object_without_ability_interface):
    object_without_ability_interface.dice = None
    object_without_ability_interface.modifier = None

    return object_without_ability_interface


@pytest.fixture
def object_with_ability_interface_has_required_fields_check(
        object_with_ability_interface):
    return dice_pool.has_required_fields(object_with_ability_interface)


@pytest.fixture
def object_without_ability_interface_has_required_fields_check(
        object_without_ability_interface):
    return dice_pool.has_required_fields(object_without_ability_interface)


@pytest.fixture
def correct_sequence(melee_ability, object_with_ability_interface):
    return [melee_ability, object_with_ability_interface]


@pytest.fixture
def incorrect_sequence(melee_ability, object_without_ability_interface):
    return [melee_ability, object_without_ability_interface]
