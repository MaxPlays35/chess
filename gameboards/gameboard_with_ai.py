import copy
from collections import deque
from typing import Union

from .board import Board
from .gameboard import GameBoard
from pieces import Pawn


class GameBoardWithAI(GameBoard):
    def __init__(self):
        super().__init__()
        self.search_depth = 2
        self.best_move = None
        self.is_white_turn = True
        self.history = deque()
        self.reset_time = True
        self.shadow_board = Board()
        self.backup = deque()


    def move(self, chess_xy: str, move_xy: str, time: float):
        chess_x, chess_y = ord(chess_xy[0]) - 65, 8 - int(chess_xy[1])
        move_x, move_y = ord(move_xy[0]) - 65, 8 - int(move_xy[1])
        if super(GameBoardWithAI, self).move(chess_xy, move_xy, time):
            self.shadow_board = copy.deepcopy(self.board)
            print(self.shadow_board)
            move_res = self.correct_ai(self.ai_move())

            res = super(GameBoardWithAI, self).move(*move_res, 0)
            print(move_res)
            assert res
            # self.shadow_board.set_board(self.board)
            self.reset_time = True
            return True
        return False

    def make_move(self, x1, y1, x2, y2):
        self.backup.append(copy.deepcopy(self.shadow_board))
        figure = self.shadow_board[y1][x1]

        # print(figure)


        if figure != " " and figure.check(x2, y2,
                                          self.shadow_board) and figure.is_white == self.shadow_board.is_white_turn:

            figure.move(x2, y2)

            if self.shadow_board[y2][x2] != " ":
                if self.shadow_board.is_white_turn:
                    self.shadow_board.black_army.remove(self.shadow_board[y2][x2])
                else:
                    self.shadow_board.white_army.remove(self.shadow_board[y2][x2])
                self.shadow_board[y2][x2] = self.shadow_board[y1][x1]
                self.shadow_board[y1][x1] = " "
            else:
                self.shadow_board[y1][x1], self.shadow_board[y2][x2] = self.shadow_board[y2][x2], self.shadow_board[y1][
                    x1]

            self.shadow_board.is_white_turn = not self.shadow_board.is_white_turn

    def undo_move(self):
        self.shadow_board = self.backup.pop()

    def ai_move(self):
        for i in range(2):
            self.maximizer(self.search_depth, -10000, 10000)
        return self.best_move

    def maximizer(self, depth: int, alpha: Union[int, float], beta: Union[int, float]):
        if depth == 0:
            return self.shadow_board.compute_rating("BLACK")

        legal_moves = self.shadow_board.compute_all_legal_moves()

        for move in legal_moves:
            # print(self.shadow_board[move[0][1]][move[0][0]])
            self.make_move(*move[0], *move[1])
            rating = self.minimizer(depth - 1, alpha, beta)
            print(rating)
            self.undo_move()

            if rating > alpha:
                alpha = rating

                if depth == self.search_depth:
                    self.best_move = move

            if alpha >= beta:
                return alpha

        return alpha

    def minimizer(self, depth: int, alpha: Union[int, float], beta: Union[int, float]):
        if depth == 0:
            return self.shadow_board.compute_rating("BLACK")

        legal_moves = self.shadow_board.compute_all_legal_moves()

        for move in legal_moves:
            self.make_move(*move[0], *move[1])
            rating = self.maximizer(depth - 1, alpha, beta)

            print(rating)
            self.undo_move()

            if rating <= beta:
                beta = rating

            if alpha >= beta:
                return beta

        return beta

    def correct_ai(self, move):
        print(move)
        x1 = chr(move[0][0] + 65)
        y1 = str(8 - move[0][1])
        x2 = chr(move[1][0] + 65)
        y2 = str(8 - move[1][1])
        return x1 + y1, x2 + y2
