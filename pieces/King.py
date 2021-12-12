from .piece_base import PieceBase


class BlackKing(PieceBase):
    def __init__(self, position: list[int, int]):
        super(BlackKing, self).__init__("♚", position)

    def check(self, x, y):
        raise NotImplemented()


class WhiteKing(PieceBase):
    def __init__(self, position: list[int, int]):
        super(WhiteKing, self).__init__("♔", position)

    def check(self, x, y):
        raise NotImplemented()
