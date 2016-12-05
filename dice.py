class Dice:
    """Base dice class."""
    _sides = 0

    def __init__(self):
        self._faces = self.__retrieve_faces(self._sides)

    @property
    def faces(self):
        """Get all faces of dice."""
        return self._faces

    @staticmethod
    def __retrieve_faces(amount):
        return tuple(range(1, amount + 1))


class Tetrahedron(Dice):
    """4-sided dice."""
    _sides = 4


class Cube(Dice):
    """6-sided dice."""
    _sides = 6


class Octahedron(Dice):
    """8-sided dice."""
    _sides = 8


class Decahedron(Dice):
    """10-sided dice."""
    _sides = 10

    def __init__(self):
        super(Decahedron, self).__init__()
        self._faces = tuple(range(0, self._sides))


class Dodecahedron(Dice):
    """12-sided dice."""
    _sides = 12


def get_dice(num_of_faces):
    """Factory method that retrieves dice with number of sides provided."""
    dices = {4: Tetrahedron, 6: Cube, 8: Octahedron, 10: Decahedron,
             12: Dodecahedron}
    return dices[num_of_faces]()
