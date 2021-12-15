from .consts import WHITE_PIECES, BLACK_PIECES
from .piece_base import PieceBase


class KingBase(PieceBase):
    def __init__(self, symbol, position: list[int, int], is_white):
        super(KingBase, self).__init__(symbol, position, is_white)

    def check(self, x, y, gm):
        if abs(x - self.position[0]) <= 1 and abs(y - self.position[1]) <= 1:
            if gm[y][x] != " " and gm[y][x].symbol in (BLACK_PIECES if not self.is_white else WHITE_PIECES):
                return False
            return True

        return False


class BlackKing(KingBase):
    def __init__(self, position: list[int, int]):
        super(BlackKing, self).__init__("♚", position, False)


class WhiteKing(KingBase):
    def __init__(self, position: list[int, int]):
        super(WhiteKing, self).__init__("♔", position, True)
