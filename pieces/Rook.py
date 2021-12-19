from .consts import BLACK_PIECES, WHITE_PIECES
from .piece_base import PieceBase


class RookBase(PieceBase):
    def __init__(self, symbol: str, position: list[int, int], is_white):
        self.score = 5
        super(RookBase, self).__init__(symbol, position, is_white)

    def check(self, x, y, gm):
        stage_1 = self.check_stage_1(x, y)
        if not stage_1:
            return False
        return self.check_stage_2(x, y, gm)

    def check_stage_1(self, x, y):
        if x == self.position[0] or y == self.position[1]:
            return True
        return False

    def check_stage_2(self, x, y, gm):
        saw_chess_before = False
        if self.position[0] == x:
            if y > self.position[1]:
                for y_new in range(self.position[1] + 1, y + 1):
                    if saw_chess_before:
                        return False
                    if gm[y_new][x] != ' ' and gm[y_new][x].symbol in (
                    BLACK_PIECES if not self.is_white else WHITE_PIECES):
                        return False
                    if gm[y_new][x] != ' ' and gm[y_new][x].symbol in (
                    WHITE_PIECES if not self.is_white else BLACK_PIECES):
                        saw_chess_before = True
                return True
            else:
                for y_new in range(self.position[1] - 1, y - 1, -1):
                    if saw_chess_before:
                        return False
                    if gm[y_new][x] != ' ' and gm[y_new][x].symbol in (
                    BLACK_PIECES if not self.is_white else WHITE_PIECES):
                        return False
                    if gm[y_new][x] != ' ' and gm[y_new][x].symbol in (
                    WHITE_PIECES if not self.is_white else BLACK_PIECES):
                        saw_chess_before = True
                return True
        else:
            if x > self.position[0]:
                for x_new in range(self.position[0] + 1, x + 1):
                    if saw_chess_before:
                        return False
                    if gm[y][x_new] != ' ' and gm[y][x_new].symbol in (
                    BLACK_PIECES if not self.is_white else WHITE_PIECES):
                        return False
                    if gm[y][x_new] != ' ' and gm[y][x_new].symbol in (
                    WHITE_PIECES if not self.is_white else BLACK_PIECES):
                        saw_chess_before = True
                return True
            else:
                for x_new in range(self.position[0] - 1, x - 1, -1):
                    if saw_chess_before:
                        return False
                    if gm[y][x_new] != ' ' and gm[y][x_new].symbol in (
                    BLACK_PIECES if not self.is_white else WHITE_PIECES):
                        return False
                    if gm[y][x_new] != ' ' and gm[y][x_new].symbol in (
                    WHITE_PIECES if not self.is_white else BLACK_PIECES):
                        saw_chess_before = True
                return True

    def compute_legal_moves(self, gm):
        legal_moves = [*self.compute_linear_moves(1, 0, gm), *self.compute_linear_moves(-1, 0, gm),
                       *self.compute_linear_moves(0, 1, gm), *self.compute_linear_moves(0, -1, gm)]
        return legal_moves


class BlackRook(RookBase):
    def __init__(self, position: list[int, int]):
        super(BlackRook, self).__init__("♜", position, False)


class WhiteRook(RookBase):
    def __init__(self, position: list[int, int]):
        super(WhiteRook, self).__init__("♖", position, True)
