from .piece_base import PieceBase


class BlackQueen(PieceBase):
    def __init__(self, position: list[int, int]):
        super(BlackQueen, self).__init__("♛", position)

    def check(self, x, y):
        raise NotImplemented()


class WhiteQueen(PieceBase):
    def __init__(self, position: list[int, int]):
        super(WhiteQueen, self).__init__("♕", position)

    def check(self, x, y):
        raise NotImplemented()
