from .consts import BLACK_PIECES, WHITE_PIECES
from .piece_base import PieceBase


class BlackKnight(PieceBase):
    def __init__(self, position: list[int, int]):
        super(BlackKnight, self).__init__("♞", position)

    def check(self, x, y, gm):
        if abs(x - self.position[0]) == 2 and abs(y - self.position[1]) == 1 or abs(x - self.position[0]) == 1 and abs(
                y - self.position[1]) == 2:
            if gm[y][x] != " " and gm[y][x].symbol in BLACK_PIECES:
                return False

        return True


class WhiteKnight(PieceBase):
    def __init__(self, position: list[int, int]):
        super(WhiteKnight, self).__init__("♘", position)

    def check(self, x, y, gm):
        if abs(x - self.position[0]) == 2 and abs(y - self.position[1]) == 1 or abs(x - self.position[0]) == 1 and abs(
                y - self.position[1]) == 2:
            if gm[y][x] != " " and gm[y][x].symbol in WHITE_PIECES:
                return False

        return True
