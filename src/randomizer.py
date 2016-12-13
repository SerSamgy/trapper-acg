import dice_pool

Pool = dice_pool.DicePool()


def add_ability_to_pool(ability):
    Pool.append(ability)


def remove_ability_from_pool(ability):
    Pool.remove(ability)


def empty_pool():
    Pool.clear()


def pop_value_from_pool():
    return Pool.pop()


def get_random_ability_value(ability):
    return ability.dice.randomVal() + ability.modifier


def get_sum_of_random_values_from_pool():
    result = 0
    while len(Pool) > 0:
        ability = pop_value_from_pool()
        result += get_random_ability_value(ability)

    return result
