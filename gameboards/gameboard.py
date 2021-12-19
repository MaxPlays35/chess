import pprint
from collections import deque

from gameboards.board import Board
from pieces import *


class GameBoard:
    def __init__(self):
        self.board = Board()
        self.history = deque()
        self.reset_time = True

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

        if figure != " " and figure.check(move_x, move_y, self.board) and figure.is_white == self.board.is_white_turn:

            figure.move(move_x, move_y)

            self.history.appendleft(f"- {chess_xy} ⇨ {move_xy} ({int(time)} s)")

            if self.board[move_y][move_x] != " ":
                if self.board.is_white_turn:
                    self.board.black_army.remove(self.board[move_y][move_x])
                else:
                    self.board.white_army.remove(self.board[move_y][move_x])
                self.board[move_y][move_x] = figure
                self.board[chess_y][chess_x] = " "
                self.board.is_white_turn = not self.board.is_white_turn
                return True
            self.board[chess_y][chess_x], self.board[move_y][move_x] = self.board[move_y][move_x], self.board[chess_y][
                chess_x]
            self.board.is_white_turn = not self.board.is_white_turn
            return True

        return False

    def anybody_wins(self):
        white_king = list(filter(lambda piece: isinstance(piece, King.WhiteKing), self.board.white_army))
        black_king = list(filter(lambda piece: isinstance(piece, King.BlackKing), self.board.black_army))

        if not len(black_king):
            return "White"
        if not len(white_king):
            return "Black"

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
