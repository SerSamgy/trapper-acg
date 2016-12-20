import pytest

import randomizer.dice as dice

expected_dice_faces = [
    (set(dice.d4.randomDraw()), set(range(1, 5))),
    (set(dice.d6.randomDraw()), set(range(1, 7))),
    (set(dice.d8.randomDraw()), set(range(1, 9))),
    (set(dice.d10.randomDraw()), set(range(1, 11))),
    (set(dice.d12.randomDraw()), set(range(1, 13))),
]


@pytest.mark.parametrize('dice,expected', expected_dice_faces)
def test_dice_has_proper_num_of_faces(dice, expected):
    assert dice == expected
