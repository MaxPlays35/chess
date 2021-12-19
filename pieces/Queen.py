from .consts import BLACK_PIECES, WHITE_PIECES
from .piece_base import PieceBase


class QueenBase(PieceBase):
    def __init__(self, symbol, position: list[int, int], is_white):
        self.score = 9
        super(QueenBase, self).__init__(symbol, position, is_white)

    def check(self, x, y, gm):
        stage_1, figure = self.check_stage_1(x, y)

        if not stage_1:
            return False

        return self.check_stage_2(x, y, gm, figure)

    def check_stage_1(self, x, y):
        if x == self.position[0] or y == self.position[1]:
            return True, "Rook"
        if abs(x - self.position[0]) == abs(y - self.position[1]):
            return True, "Bishop"
        return False, ""

    def check_stage_2(self, x, y, gm, figure):
        saw_chess_before = False
        if figure == "Rook":
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
        else:
            steps = abs(self.position[0] - x)

            step_x = -1 if self.position[0] > x else 1
            step_y = -1 if self.position[1] > y else 1

            for i in range(1, steps + 1):
                if saw_chess_before:
                    return False
                cell = gm[self.position[1] + step_y * i][self.position[0] + step_x * i]
                if cell != " " and cell.symbol in (
                        WHITE_PIECES if self.is_white else BLACK_PIECES):
                    return False
                if cell != " " and cell.symbol in (
                        BLACK_PIECES if self.is_white else WHITE_PIECES):
                    saw_chess_before = True

            return True

    def compute_legal_moves(self, gm):
        legal_moves = [
            *self.compute_linear_moves(1, 0, gm),
            *self.compute_linear_moves(-1, 0, gm),
            *self.compute_linear_moves(0, 1, gm),
            *self.compute_linear_moves(0, -1, gm),
            *self.compute_linear_moves(1, 1, gm),
            *self.compute_linear_moves(1, -1, gm),
            *self.compute_linear_moves(-1, -1, gm),
            *self.compute_linear_moves(-1, 1, gm)

        ]

        return legal_moves


class BlackQueen(QueenBase):
    def __init__(self, position: list[int, int]):
        super(BlackQueen, self).__init__("♛", position, False)


class WhiteQueen(QueenBase):
    def __init__(self, position: list[int, int]):
        super(WhiteQueen, self).__init__("♕", position, True)
