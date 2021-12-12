from .piece_base import PieceBase


class BlackKnight(PieceBase):
    def __init__(self, position: list[int, int]):
        super(BlackKnight, self).__init__("♞", position)

    def check(self, x, y):
        raise NotImplemented()


class WhiteKnight(PieceBase):
    def __init__(self, position: list[int, int]):
        super(WhiteKnight, self).__init__("♘", position)

    def check(self, x, y):
        raise NotImplemented()