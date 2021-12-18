import copy


class PieceBase:
    def __init__(self, symbol: str, position: list[int, int], is_white: bool = False):
        self.symbol = symbol
        self.position = position
        self.moves = 0
        self.is_white = is_white
        self.computing_position = []

    def check(self, x, y, gm):
        raise NotImplemented()

    def move(self, x, y):
        self.position = [x, y]
        self.moves += 1

    def compute_linear_moves(self, horizontal: int, vertical: int, gm):
        self.computing_position = copy.deepcopy(self.position)
        legal_moves = []

        target_square = self.get_square(horizontal, vertical, gm)

        while target_square is not None:
            self.computing_position[1] += vertical
            self.computing_position[0] += horizontal

            if target_square == " ":
                legal_moves.append([self.position, [self.computing_position[0], self.computing_position[1]]])
            elif target_square.is_white == self.is_white:
                break
            else:
                legal_moves.append([self.position, [self.computing_position[0], self.computing_position[1]]])
                break
            target_square = self.get_square(horizontal, vertical, gm)

        return legal_moves

    def get_square(self, horizontal: int, vertical: int, gm):
        if 8 > horizontal + self.computing_position[0] >= 0 and 8 > vertical + self.computing_position[1] >= 0:
            return gm[vertical + self.computing_position[1]][horizontal + self.computing_position[0]]
        else:
            return None

    def check_square(self, legal_moves: list, square, horizontal, vertical):
        if square is not None:
            if square == " ":
                legal_moves.append([self.position, [self.computing_position[0] + horizontal, self.computing_position[1] + vertical]])
            elif square.is_white != self.is_white:
                legal_moves.append([self.position, [self.computing_position[0] + horizontal, self.computing_position[1] + vertical]])

    def __repr__(self):
        return self.symbol + str(self.position)

    def __str__(self):
        return self.symbol
