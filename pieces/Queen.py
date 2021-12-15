from .consts import BLACK_PIECES, WHITE_PIECES
from .piece_base import PieceBase


class QueenBase(PieceBase):
    def __init__(self, symbol, position: list[int, int], is_white):
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
                ma = max(self.position[1], y)
                mi = min(self.position[1], y)
                for y_new in range(mi + 1, ma):
                    if saw_chess_before:
                        return False
                    if gm[y_new][x] != ' ' and gm[y_new][x].symbol in (
                            WHITE_PIECES if not self.is_white else BLACK_PIECES):
                        return False
                    if gm[y_new][x] != ' ' and gm[y_new][x].symbol in (
                            BLACK_PIECES if not self.is_white else WHITE_PIECES):
                        saw_chess_before = True
                return True
            else:
                ma = max(self.position[0], x)
                mi = min(self.position[0], x)
                for x_new in range(mi + 1, ma):
                    if saw_chess_before:
                        return False
                    if gm[y][x_new] != ' ' and gm[y][x_new].symbol in (
                            WHITE_PIECES if not self.is_white else BLACK_PIECES):
                        return False
                    if gm[y][x_new] != ' ' and gm[y][x_new].symbol in (
                            BLACK_PIECES if not self.is_white else WHITE_PIECES):
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
                if cell != " " and cell.symbol in WHITE_PIECES:
                    return False
                if cell != " " and cell.symbol in BLACK_PIECES:
                    saw_chess_before = True

            return True


class BlackQueen(QueenBase):
    def __init__(self, position: list[int, int]):
        super(BlackQueen, self).__init__("♛", position, False)


class WhiteQueen(QueenBase):
    def __init__(self, position: list[int, int]):
        super(WhiteQueen, self).__init__("♕", position, True)
