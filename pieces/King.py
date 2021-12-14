from .consts import WHITE_PIECES, BLACK_PIECES
from .piece_base import PieceBase


class BlackKing(PieceBase):
    def __init__(self, position: list[int, int]):
        super(BlackKing, self).__init__("♚", position)

    def check(self, x, y, gm):
        if abs(x - self.position[0]) == 1 or abs(y - self.position[1]):
            if gm[y][x] != " " and gm[y][x].symbol in BLACK_PIECES:
                return False
            return True

        return False


class WhiteKing(PieceBase):
    def __init__(self, position: list[int, int]):
        super(WhiteKing, self).__init__("♔", position)

    def check(self, x, y, gm):
        if abs(x - self.position[0]) <= 1 and abs(y - self.position[1]) <= 1:
            if gm[y][x] != " " and gm[y][x].symbol in WHITE_PIECES:
                return False
            return True

        return False
