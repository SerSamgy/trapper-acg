import pytestimport src.dice as diceexpected_dice_faces = [    (dice.d4, tuple(range(1, 5))),    (dice.d6, tuple(range(1, 7))),    (dice.d8, tuple(range(1, 9))),    (dice.d10, tuple(range(1, 11))),    (dice.d12, tuple(range(1, 13))),]@pytest.mark.parametrize('dice,expected', expected_dice_faces)def test_dice_has_proper_num_of_faces(dice, expected):    assert dice == expected