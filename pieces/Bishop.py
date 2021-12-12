from .piece_base import PieceBase


class BlackBishop(PieceBase):
    def __init__(self, position: list[int, int]):
        super(BlackBishop, self).__init__("♝", position)

    def check(self, x, y):
        raise NotImplemented()


class WhiteBishop(PieceBase):
    def __init__(self, position: list[int, int]):
        super(WhiteBishop, self).__init__("♗", position)

    def check(self, x, y):
        raise NotImplemented()