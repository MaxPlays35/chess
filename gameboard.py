from collections import deque

from pieces import *


class GameBoard:
    def __init__(self):
        self.black_army = [Rook.BlackRook([0, 0]), Knight.BlackKnight([1, 0]), Bishop.BlackBishop([2, 0]),
                           Queen.BlackQueen([3, 0]),
                           King.BlackKing([4, 0]),
                           Bishop.BlackBishop([5, 0]), Knight.BlackKnight([6, 0]), Rook.BlackRook([7, 0]),
                           Pawn.BlackPawn([0, 1]), Pawn.BlackPawn([1, 1]), Pawn.BlackPawn([2, 1]),
                           Pawn.BlackPawn([3, 1]),
                           Pawn.BlackPawn([4, 1]), Pawn.BlackPawn([5, 1]),
                           Pawn.BlackPawn([6, 1]), Pawn.BlackPawn([7, 1])]
        self.white_army = [Pawn.WhitePawn([0, 6], ), Pawn.WhitePawn([1, 6]), Pawn.WhitePawn([2, 6]),
                           Pawn.WhitePawn([3, 6]),
                           Pawn.WhitePawn([4, 6]), Pawn.WhitePawn([5, 6]),
                           Pawn.WhitePawn([6, 6]), Pawn.WhitePawn([7, 6]), Rook.WhiteRook([0, 7]),
                           Knight.WhiteKnight([1, 7]), Bishop.WhiteBishop([2, 7]), Queen.WhiteQueen([3, 7]),
                           King.WhiteKing([4, 7]),
                           Bishop.WhiteBishop([5, 7]), Knight.WhiteKnight([6, 7]), Rook.WhiteRook([7, 7])]
        self.board = []
        self.board.append([*self.black_army[:8]])
        self.board.append(
            [*self.black_army[8:]])
        self.board.extend([[' ' for i in range(8)] for j in range(4)])
        self.board.append(
            [*self.white_army[:8]])
        self.board.append(
            [*self.white_army[8:]])
        self.is_white_turn = True
        self.history = deque()

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

    def move(self, chess_xy: str, move_xy: str, time: float):
        chess_x, chess_y = ord(chess_xy[0]) - 65, 8 - int(chess_xy[1])
        move_x, move_y = ord(move_xy[0]) - 65, 8 - int(move_xy[1])
        figure = self.board[chess_y][chess_x]
        if figure != " " and figure.check(move_x, move_y, self.board) and figure.is_white == self.is_white_turn:

            figure.move(move_x, move_y)

            self.history.appendleft(f"- {chess_xy} ⇨ {move_xy} ({int(time)} s)")

            if self.board[move_y][move_x] != " ":
                if self.is_white_turn:
                    self.black_army.remove(self.board[move_y][move_x])
                else:
                    self.white_army.remove(self.board[move_y][move_x])
                self.board[move_y][move_x] = figure
                self.board[chess_y][chess_x] = " "
                self.is_white_turn = not self.is_white_turn
                return True
            self.board[chess_y][chess_x], self.board[move_y][move_x] = self.board[move_y][move_x], self.board[chess_y][
                chess_x]
            self.is_white_turn = not self.is_white_turn
            if isinstance(figure, Rook.WhiteRook):
                print(figure.compute_legal_moves(self.board))
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
