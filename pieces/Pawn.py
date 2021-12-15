from .consts import BLACK_PIECES, WHITE_PIECES
from .piece_base import PieceBase


class BlackPawn(PieceBase):
    def __init__(self, position: list[int, int]):
        self.first = True
        super(BlackPawn, self).__init__("♟", position, False)

    def check(self, x, y, gm):
        stage_1 = self.check_stage_1(x, y, gm)
        if not stage_1:
            return False
        return self.check_stage_2(x, y, gm)

    def check_stage_1(self, x, y, gm):
        if y - self.position[1] == 1 or (y - self.position[1] == 2 and not self.moves):
            if gm[y][x] != ' ' and gm[y][x].symbol in WHITE_PIECES:
                if x == self.position[0]:
                    return False
                return True

            if x == self.position[0]:
                return True

        return False

    def check_stage_2(self, x, y, gm):
        if x == self.position[0]:
            for y_new in range(self.position[1] + 1, y):
                if gm[y_new][x] != ' ':
                    return False
        return True


class WhitePawn(PieceBase):
    def __init__(self, position: list[int, int]):
        self.first = True
        super(WhitePawn, self).__init__("♙", position, True)

    def check(self, x, y, gm):
        stage_1 = self.check_stage_1(x, y, gm)
        if not stage_1:
            return False
        return self.check_stage_2(x, y, gm)

    def check_stage_1(self, x, y, gm):
        if y - self.position[1] == -1 or (y - self.position[1] == -2 and not self.moves):
            if gm[y][x] != ' ' and gm[y][x].symbol in BLACK_PIECES:
                if x == self.position[0]:
                    return False
                return True

            if x == self.position[0]:
                return True

        return False

    def check_stage_2(self, x, y, gm):
        if x == self.position[0]:
            for y_new in range(self.position[1] - 1, y - 1, -1):
                if gm[y_new][x] != ' ':
                    return False
        return True
