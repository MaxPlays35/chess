from .consts import BLACK_PIECES, WHITE_PIECES
from .piece_base import PieceBase


class KnightBase(PieceBase):
    def __init__(self, symbol, position: list[int, int], is_white):
        super(KnightBase, self).__init__(symbol, position, is_white)

    def check(self, x, y, gm):
        if abs(x - self.position[0]) == 2 and abs(y - self.position[1]) == 1 or abs(x - self.position[0]) == 1 and abs(
                y - self.position[1]) == 2:
            if gm[y][x] != " " and gm[y][x].symbol in (BLACK_PIECES if not self.is_white else WHITE_PIECES):
                return False

        return True


class BlackKnight(KnightBase):
    def __init__(self, position: list[int, int]):
        super(BlackKnight, self).__init__("♞", position, False)


class WhiteKnight(KnightBase):
    def __init__(self, position: list[int, int]):
        super(WhiteKnight, self).__init__("♘", position, True)
