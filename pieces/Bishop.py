from .piece_base import PieceBase
from .consts import BLACK_PIECES, WHITE_PIECES


class BlackBishop(PieceBase):
    def __init__(self, position: list[int, int]):
        super(BlackBishop, self).__init__("♝", position)

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
            if cell != " " and cell.symbol in BLACK_PIECES:
                return False
            if cell != " " and cell.symbol in WHITE_PIECES:
                saw_chess_before = True
            print(saw_chess_before)
        return True


class WhiteBishop(PieceBase):
    def __init__(self, position: list[int, int]):
        super(WhiteBishop, self).__init__("♗", position)

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
            if cell != " " and cell.symbol in WHITE_PIECES:
                return False
            if cell != " " and cell.symbol in BLACK_PIECES:
                saw_chess_before = True

        return True
