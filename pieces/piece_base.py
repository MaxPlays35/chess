class PieceBase:
    def __init__(self, symbol: str, position: list[int, int]):
        self.symbol = symbol
        self.position = position

    def check(self, x, y, gm):
        raise NotImplemented()

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol
