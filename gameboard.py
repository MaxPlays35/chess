from pieces import *


class GameBoard:
    def __init__(self):
        self.board = []
        self.board.append(
            [Rook.BlackRook([0, 7]), Knight.BlackKnight([1, 7]), Bishop.BlackBishop([2, 7]), King.BlackKing([3, 7]),
             Queen.BlackQueen([4, 7]),
             Bishop.BlackBishop([5, 7]), Knight.BlackKnight([6, 7]), Rook.BlackRook([7, 7])])
        self.board.append(
            [Pawn.BlackPawn([0, 6]), Pawn.BlackPawn([1, 6]), Pawn.BlackPawn([2, 6]), Pawn.BlackPawn([3, 6]),
             Pawn.BlackPawn([4, 6]), Pawn.BlackPawn([5, 6]),
             Pawn.BlackPawn([6, 6]), Pawn.BlackPawn([7, 6])])
        self.board.extend([[' ' for i in range(8)] for j in range(4)])
        self.board.append(
            [Pawn.WhitePawn([0, 1], ), Pawn.WhitePawn([1, 1]), Pawn.WhitePawn([2, 1]), Pawn.WhitePawn([3, 1]),
             Pawn.WhitePawn([4, 1]), Pawn.WhitePawn([5, 1]),
             Pawn.WhitePawn([6, 1]), Pawn.WhitePawn([7, 1])])
        self.board.append(
            [Rook.WhiteRook([0, 0]), Knight.WhiteKnight([1, 0]), Bishop.WhiteBishop([2, 0]), King.WhiteKing([3, 0]),
             Queen.WhiteQueen([4, 0]),
             Bishop.WhiteBishop([5, 0]), Knight.WhiteKnight([6, 0]), Rook.WhiteRook([7, 0])])

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
        print(chess_x, chess_y, move_x, move_y)
        print(self.board[chess_y][chess_x].check(move_x, move_y, self.board))
        if self.board[chess_y][chess_x].check(move_x, move_y, self.board):
            self.board[chess_x][chess_y], self.board[move_x][move_y] = self.board[move_x][move_y], self.board[chess_x][
                chess_y]
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

