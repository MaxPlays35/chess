import copy

from .Queen import QueenBase
from .consts import BLACK_PIECES, WHITE_PIECES
from .piece_base import PieceBase


class BlackPawn(QueenBase):
    def __init__(self, position: list[int, int]):
        self.first = True
        self.Queen = False
        self.score = 1
        super(BlackPawn, self).__init__("♟", position, False)

    def move(self, x, y):
        if y == 7:
            self.Queen = True
            self.symbol = "♛"
        self.position = [x, y]
        self.moves += 1

    def check(self, x, y, gm):
        if not self.Queen:
            stage_1 = self.check_stage_1(x, y, gm)
            if not stage_1:
                return False
            return self.check_stage_2(x, y, gm)
        stage_1, figure = super(BlackPawn, self).check_stage_1(x, y)
        if not stage_1:
            return False

        return super(BlackPawn, self).check_stage_2(x, y, gm, figure)

    def check_stage_1(self, x, y, gm):
        if not self.Queen:
            if y - self.position[1] == 1 or (y - self.position[1] == 2 and not self.moves):
                if gm[y][x] != ' ' and gm[y][x].symbol in WHITE_PIECES:
                    if x == self.position[0]:
                        return False
                    return True

                if gm[y][x] != " " and gm[y][x].symbol in BLACK_PIECES:
                    return False

                if x == self.position[0]:
                    return True

            return False
        return super(BlackPawn, self).check_stage_1(x, y)

    def check_stage_2(self, x, y, gm):
        if not self.Queen:
            if x == self.position[0]:
                for y_new in range(self.position[1] + 1, y):
                    if gm[y_new][x] != ' ':
                        return False
            return True

    def compute_legal_moves(self, gm):
        if not self.Queen:
            self.computing_position = copy.copy(self.position)
            legal_moves = []
            target_square = self.get_square(0, 1, gm)
            if target_square is not None and target_square == " ":
                legal_moves.append([self.position, [self.computing_position[0], self.computing_position[1] + 1]])
                target_square = self.get_square(0, 2, gm)
    
                if not self.moves and target_square == " ":
                    legal_moves.append([self.position, [self.computing_position[0], self.computing_position[1] + 2]])
    
            target_square = self.get_square(-1, 1, gm)
    
            if target_square is not None and target_square != " " and target_square.symbol in WHITE_PIECES:
                legal_moves.append([self.position, [self.computing_position[0] - 1, self.computing_position[1] + 1]])
    
            target_square = self.get_square(1, 1, gm)
    
            if target_square is not None and target_square != " " and target_square.symbol in WHITE_PIECES:
                legal_moves.append([self.position, [self.computing_position[0] + 1, self.computing_position[1] + 1]])
    
            return legal_moves
        return super(BlackPawn, self).compute_legal_moves(gm)


class WhitePawn(QueenBase):
    def __init__(self, position: list[int, int]):
        self.first = True
        self.score = 1
        self.Queen = False
        super(WhitePawn, self).__init__("♙", position, True)

    def check(self, x, y, gm):
        if not self.Queen:
            stage_1 = self.check_stage_1(x, y, gm)
            if not stage_1:
                return False
            return self.check_stage_2(x, y, gm)
        stage_1, figure = super(WhitePawn, self).check_stage_1(x, y)
        if not stage_1:
            return False

        return super(WhitePawn, self).check_stage_2(x, y, gm, figure)

    def check_stage_1(self, x, y, gm):
        if y - self.position[1] == -1 or (y - self.position[1] == -2 and not self.moves):
            if gm[y][x] != ' ' and gm[y][x].symbol in BLACK_PIECES:
                if x == self.position[0]:
                    return False
                return True

            if gm[y][x] != " " and gm[y][x].symbol in WHITE_PIECES:
                return False
    
            if x == self.position[0]:
                return True
    
        return False

    def check_stage_2(self, x, y, gm):
        if x == self.position[0]:
            for y_new in range(self.position[1] - 1, y - 1, -1):
                if gm[y_new][x] != ' ':
                    return False
        return True


    def compute_legal_moves(self, gm):
        if not self.Queen:
            self.computing_position = copy.copy(self.position)
            legal_moves = []
            target_square = self.get_square(0, -1, gm)
            if target_square is not None and target_square == " ":
                legal_moves.append([self.position, [self.computing_position[0], self.computing_position[1] - 1]])
                target_square = self.get_square(0, -2, gm)

                if not self.moves and target_square == " ":
                    legal_moves.append([self.position, [self.computing_position[0], self.computing_position[1] - 2]])

            target_square = self.get_square(1, -1, gm)

            if target_square is not None and target_square != " " and target_square.symbol in BLACK_PIECES:
                legal_moves.append([self.position, [self.computing_position[0] - 1, self.computing_position[1] - 1]])

            target_square = self.get_square(-1, -1, gm)

            if target_square is not None and target_square != " " and target_square.symbol in BLACK_PIECES:
                legal_moves.append([self.position, [self.computing_position[0] - 1, self.computing_position[1] - 1]])

            return legal_moves
        return super(WhitePawn, self).compute_legal_moves(gm)

    def move(self, x, y):
        if y == 0:
            self.Queen = True
            self.symbol = "♛"
        self.position = [x, y]
        self.moves += 1
