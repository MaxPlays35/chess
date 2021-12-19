import copy

from .consts import BLACK_PIECES, WHITE_PIECES
from .piece_base import PieceBase


class KnightBase(PieceBase):
    def __init__(self, symbol, position: list[int, int], is_white):
        self.score = 3
        super(KnightBase, self).__init__(symbol, position, is_white)

    def check(self, x, y, gm):
        if (abs(x - self.position[0]) == 2 and abs(y - self.position[1]) == 1) or (
                abs(x - self.position[0]) == 1 and abs(
                y - self.position[1]) == 2):
            if gm[y][x] != " " and gm[y][x].symbol in (BLACK_PIECES if not self.is_white else WHITE_PIECES):
                return False

            return True

        return False

    def compute_legal_moves(self, gm):
        self.computing_position = copy.copy(self.position)

        legal_moves = []
        target_square = self.get_square(1, 2, gm)
        self.check_square(legal_moves, target_square, 1, 2)
        target_square = self.get_square(-1, 2, gm)
        self.check_square(legal_moves, target_square, -1, 2)
        target_square = self.get_square(1, -2, gm)
        self.check_square(legal_moves, target_square, 1, -2)
        target_square = self.get_square(-1, -2, gm)
        self.check_square(legal_moves, target_square, -1, -2)
        target_square = self.get_square(2, 1, gm)
        self.check_square(legal_moves, target_square, 2, 1)
        target_square = self.get_square(-2, 1, gm)
        self.check_square(legal_moves, target_square, -2, 1)
        target_square = self.get_square(2, -1, gm)
        self.check_square(legal_moves, target_square, 2, -1)
        target_square = self.get_square(-2, -1, gm)
        self.check_square(legal_moves, target_square, -2, -1)

        return legal_moves


class BlackKnight(KnightBase):
    def __init__(self, position: list[int, int]):
        super(BlackKnight, self).__init__("♞", position, False)


class WhiteKnight(KnightBase):
    def __init__(self, position: list[int, int]):
        super(WhiteKnight, self).__init__("♘", position, True)
