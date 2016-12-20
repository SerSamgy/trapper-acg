import collections

import exceptions
import patterns.singleton

Ability = collections.namedtuple('Ability', 'dice, modifier')


def assert_all_objects_are_dice(seq):
    if not all(has_required_fields(x) for x in seq):
        raise exceptions.NoRequiredFields(seq)


def has_required_fields(check_object):
    return hasattr(check_object, 'dice') and hasattr(check_object, 'modifier')


class DicePool(list, metaclass=patterns.singleton.Singleton):
    def __init__(self, seq=None):
        if seq:
            assert_all_objects_are_dice(seq)
        else:
            seq = ()

        super().__init__(seq)

    def append(self, item):
        assert_all_objects_are_dice([item])

        super().append(item)

    def extend(self, iterable):
        assert_all_objects_are_dice(iterable)

        super().extend(iterable)

    def insert(self, index, item):
        assert_all_objects_are_dice([item])

        super().insert(index, item)
