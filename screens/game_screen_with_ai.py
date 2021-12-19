from gameboards import GameBoardWithAI
from .game_screen import GameScreen


class GameScreenWithAI(GameScreen):
    def __init__(self, screen):
        super(GameScreenWithAI, self).__init__(screen, GameBoardWithAI())
