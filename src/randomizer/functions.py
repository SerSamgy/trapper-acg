def add_ability_to_pool(pool, ability):
    pool.append(ability)


def remove_ability_from_pool(pool, ability):
    pool.remove(ability)


def empty_pool(pool):
    pool.clear()


def pop_value_from_pool(pool):
    return pool.pop()


def get_random_ability_value(ability):
    return ability.dice.randomVal() + ability.modifier


def get_sum_of_random_values_from_pool(pool):
    result = 0
    while len(pool) > 0:
        ability = pop_value_from_pool(pool)
        result += get_random_ability_value(ability)

    return result
