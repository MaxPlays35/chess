from .piece_base import PieceBase
from .consts import BLACK_PIECES, WHITE_PIECES


class BlackPawn(PieceBase):
    def __init__(self, position: list[int, int]):
        super(BlackPawn, self).__init__("♟", position)

    def check(self, x, y, gm):
        if y - self.position[1] == 1:
            if gm[x][y] != ' ' and gm[x][y].symbol in WHITE_PIECES:
                return True

            if x == self.position[0]:
                return True

        return False


class WhitePawn(PieceBase):
    def __init__(self, position: list[int, int]):
        super(WhitePawn, self).__init__("♙", position)

    def check(self, x, y, gm):
        print(x, y, self.position)
        if y - self.position[1] == 1:
            if gm[y][x] != ' ' and gm[y][x].symbol in BLACK_PIECES:
                return True

            if x == self.position[0]:
                return True

        return False
