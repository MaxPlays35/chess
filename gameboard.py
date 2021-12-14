from pieces import *


class GameBoard:
    def __init__(self):
        self.board = []
        self.board.append(
            [Rook.BlackRook([0, 0]), Knight.BlackKnight([1, 0]), Bishop.BlackBishop([2, 0]), Queen.BlackQueen([3, 0]),
             King.BlackKing([4, 0]),
             Bishop.BlackBishop([5, 0]), Knight.BlackKnight([6, 0]), Rook.BlackRook([7, 0])])
        self.board.append(
            [Pawn.BlackPawn([0, 1]), Pawn.BlackPawn([1, 1]), Pawn.BlackPawn([2, 1]), Pawn.BlackPawn([3, 1]),
             Pawn.BlackPawn([4, 1]), Pawn.BlackPawn([5, 1]),
             Pawn.BlackPawn([6, 1]), Pawn.BlackPawn([7, 1])])
        self.board.extend([[' ' for i in range(8)] for j in range(4)])
        self.board.append(
            [Pawn.WhitePawn([0, 6], ), Pawn.WhitePawn([1, 6]), Pawn.WhitePawn([2, 6]), Pawn.WhitePawn([3, 6]),
             Pawn.WhitePawn([4, 6]), Pawn.WhitePawn([5, 6]),
             Pawn.WhitePawn([6, 6]), Pawn.WhitePawn([7, 6])])
        self.board.append(
            [Rook.WhiteRook([0, 7]), Knight.WhiteKnight([1, 7]), Bishop.WhiteBishop([2, 7]), Queen.WhiteQueen([3, 7]),
             King.WhiteKing([4, 7]),
             Bishop.WhiteBishop([5, 7]), Knight.WhiteKnight([6, 7]), Rook.WhiteRook([7, 7])])
        self.is_white_turn = True

    def __repr__(self):
        unpacked = [item for sublist in self.board for item in sublist]
        return """
  ┌───┬───┬───┬───┬───┬───┬───┬───┐
8 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
7 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
6 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
5 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
4 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
3 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
2 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
1 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │
  └───┴───┴───┴───┴───┴───┴───┴───┘
 A   B   C   D   E   F   G   H""" % tuple(unpacked)

    def move(self, chess_x, chess_y, move_x, move_y):
        # print(type(self.board[chess_y][chess_x]))
        # print(self.board[chess_y][chess_x].check.__code__.co_varnames)
        if self.board[chess_y][chess_x].check(move_x, move_y, self.board):
            self.board[chess_y][chess_x].move(move_x, move_y)
            if self.board[move_y][move_x] != " ":
                self.board[move_y][move_x] = self.board[chess_y][chess_x]
                self.board[chess_y][chess_x] = " "
                return True
            self.board[chess_y][chess_x], self.board[move_y][move_x] = self.board[move_y][move_x], self.board[chess_y][
                chess_x]
            return True

        return False

    def __iter__(self):
        self.idx = -1
        return self

    def __next__(self):
        self.idx += 1
        if self.idx < 8:
            return self.board[self.idx]
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.board[item]
