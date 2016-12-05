class Dice:
    def __init__(self, edges):
        self.edges = self.__retrieve_edges(edges)

    @staticmethod
    def __retrieve_edges(amount):
        return list(range(1, amount + 1))
