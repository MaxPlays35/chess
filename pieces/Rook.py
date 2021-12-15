from .consts import BLACK_PIECES, WHITE_PIECES
from .piece_base import PieceBase


class RookBase(PieceBase):
    def __init__(self, symbol: str, position: list[int, int], is_white):
        super(RookBase, self).__init__(symbol, position, is_white)

    def check(self, x, y, gm):
        stage_1 = self.check_stage_1(x, y)
        if not stage_1:
            return False
        return self.check_stage_2(x, y, gm)

    def check_stage_1(self, x, y):
        if x == self.position[0] or y == self.position[0]:
            return True
        return False

    def check_stage_2(self, x, y, gm):
        saw_chess_before = False
        if self.position[0] == x:
            ma = max(self.position[1], y)
            mi = min(self.position[1], y)
            for y_new in range(mi + 1, ma):
                if saw_chess_before:
                    return False
                if gm[y_new][x] != ' ' and gm[y_new][x].symbol in (BLACK_PIECES if not self.is_white else WHITE_PIECES):
                    return False
                if gm[y_new][x] != ' ' and gm[y_new][x].symbol in (WHITE_PIECES if not self.is_white else BLACK_PIECES):
                    saw_chess_before = True
            return True
        else:
            ma = max(self.position[0], x)
            mi = min(self.position[0], x)
            for x_new in range(mi + 1, ma):
                if saw_chess_before:
                    return False
                if gm[y][x_new] != ' ' and gm[y][x_new].symbol in (BLACK_PIECES if not self.is_white else WHITE_PIECES):
                    return False
                if gm[y][x_new] != ' ' and gm[y][x_new].symbol in (WHITE_PIECES if not self.is_white else BLACK_PIECES):
                    saw_chess_before = True
            return True


class BlackRook(RookBase):
    def __init__(self, position: list[int, int]):
        super(BlackRook, self).__init__("♜", position, False)


class WhiteRook(RookBase):
    def __init__(self, position: list[int, int]):
        super(WhiteRook, self).__init__("♖", position, True)
