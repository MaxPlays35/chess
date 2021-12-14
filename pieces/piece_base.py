class PieceBase:
    def __init__(self, symbol: str, position: list[int, int], is_white: bool):
        self.symbol = symbol
        self.position = position
        self.first = True
        self.is_white = is_white

    def check(self, x, y, gm):
        raise NotImplemented()

    def move(self, x, y):
        self.position = [x, y]
        self.first = False

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol
