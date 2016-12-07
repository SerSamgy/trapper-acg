import collections

Ability = collections.namedtuple('Ability', 'dice, modifier')


class DicePool(list):
    def __init__(self, seq=None):
        if seq:
            self.__check_sequence_objects_type(seq)
        else:
            seq = ()

        super(DicePool, self).__init__(seq)

    def append(self, p_object):
        if not self.__iscorrect_type(p_object):
            raise TypeError

        super(DicePool, self).append(p_object)

    def extend(self, iterable):
        try:
            self.__check_sequence_objects_type(iterable)
        except TypeError:
            raise

        super(DicePool, self).extend(iterable)

    def insert(self, index, p_object):
        if not self.__iscorrect_type(p_object):
            raise TypeError

        super(DicePool, self).insert(index, p_object)

    def __check_sequence_objects_type(self, seq):
        if any(not self.__iscorrect_type(x) for x in seq):
            raise TypeError

    def __iscorrect_type(self, check_object):
        return isinstance(check_object, Ability)
