from pieces import *


class Board:
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

    def __getitem__(self, item: int):
        return self.board[item]

    def compute_rating(self, side):
        white_score = 0
        black_score = 0

        for piece in self.black_army:
            black_score += piece.score
        for piece in self.white_army:
            white_score += piece.score
        return black_score - white_score if side == "BLACK" else white_score - black_score

    def compute_all_legal_moves(self):
        legal_moves = []
        if not self.is_white_turn:
            for piece in self.black_army:
                legal_moves.extend(piece.compute_legal_moves(self.board))
        else:
            for piece in self.white_army:
                legal_moves.extend(piece.compute_legal_moves(self.board))

        return legal_moves

    def set_board(self, board):
        self.board = board

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
