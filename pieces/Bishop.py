from .consts import BLACK_PIECES, WHITE_PIECES
from .piece_base import PieceBase


class BishopBase(PieceBase):
    def __init__(self, symbol, position: list[int, int], is_white):
        self.score = 3
        super(BishopBase, self).__init__(symbol, position, is_white)

    def check(self, x, y, gm):
        stage_1 = self.check_stage_1(x, y)

        if not stage_1:
            return False

        return self.check_stage_2(x, y, gm)

    def check_stage_1(self, x, y):
        if abs(x - self.position[0]) == abs(y - self.position[1]):
            return True
        return False

    def check_stage_2(self, x, y, gm):
        steps = abs(self.position[0] - x)

        step_x = -1 if self.position[0] > x else 1
        step_y = -1 if self.position[1] > y else 1
        saw_chess_before = False

        for i in range(1, steps + 1):
            if saw_chess_before:
                return False
            cell = gm[self.position[1] + step_y * i][self.position[0] + step_x * i]
            if cell != " " and cell.symbol in (BLACK_PIECES if not self.is_white else WHITE_PIECES):
                return False
            if cell != " " and cell.symbol in (WHITE_PIECES if not self.is_white else BLACK_PIECES):
                saw_chess_before = True
        return True

    def compute_legal_moves(self, gm):
        legal_moves = [
            *self.compute_linear_moves(1, 1, gm),
            *self.compute_linear_moves(1, -1, gm),
            *self.compute_linear_moves(-1, -1, gm),
            *self.compute_linear_moves(-1, 1, gm)
        ]

        return legal_moves


class BlackBishop(BishopBase):
    def __init__(self, position: list[int, int]):
        super(BlackBishop, self).__init__("♝", position, False)


class WhiteBishop(BishopBase):
    def __init__(self, position: list[int, int]):
        super(WhiteBishop, self).__init__("♗", position, True)
