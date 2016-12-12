import collections

Ability = collections.namedtuple('Ability', 'dice, modifier')


class NoRequiredFields(Exception):
    pass


class Singleton(type):
    # TODO: move this to other file
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class DicePool(list, metaclass=Singleton):

    def __init__(self, seq=None):
        if seq:
            self.__check_sequence_objects_type(seq)
        else:
            seq = ()

        super().__init__(seq)

    def append(self, p_object):
        if not self.__hasrequired_fields(p_object):
            raise NoRequiredFields

        super().append(p_object)

    def extend(self, iterable):
        self.__check_sequence_objects_type(iterable)

        super().extend(iterable)

    def insert(self, index, p_object):
        if not self.__hasrequired_fields(p_object):
            raise NoRequiredFields

        super().insert(index, p_object)

    def __check_sequence_objects_type(self, seq):
        if any(not self.__hasrequired_fields(x) for x in seq):
            raise NoRequiredFields

    def __hasrequired_fields(self, check_object):
        return hasattr(check_object, 'dice') and hasattr(check_object,
                                                         'modifier')
