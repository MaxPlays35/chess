from .piece_base import PieceBase


class BlackRook(PieceBase):
    def __init__(self, position: list[int, int]):
        super(BlackRook, self).__init__("♜", position)

    def check(self, x, y):
        raise NotImplemented()


class WhiteRook(PieceBase):
    def __init__(self, position: list[int, int]):
        super(WhiteRook, self).__init__("♖", position)

    def check(self, x, y):
        raise NotImplemented()