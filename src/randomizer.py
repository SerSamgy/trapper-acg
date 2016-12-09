import random


def add_ability_to_pool(pool, ability):
    pool.append(ability)


def remove_ability_from_pool(pool, ability):
    pool.remove(ability)


def empty_pool(pool):
    pool.clear()


def shuffle_ability_dice(dice):
    # lambda function guarantees we get new dice elements order
    random.shuffle(dice, lambda: random.uniform(0.0, 0.7))


def shuffle_pool_dices(pool):
    for ability in pool:
        shuffle_ability_dice(ability.dice)


def get_random_ability_value(ability):
    return random.choice(ability.dice) + ability.modifier


def get_sum_of_random_values_from_pool(pool):
    result = 0
    for ability in pool:
        result += get_random_ability_value(ability)

    return result
