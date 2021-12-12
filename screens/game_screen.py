import re

from asciimatics.event import KeyboardEvent
from asciimatics.widgets import Frame, Layout, Label, Text, PopUpDialog

from gameboard import GameBoard


class GameScreen(Frame):
    def __init__(self, screen):
        super(GameScreen, self).__init__(screen, screen.height - 20, screen.width - 20)
        self.game = GameBoard()

        self.layout = Layout([1, 1])

        self.add_layout(self.layout)
        self.matrix = Label("", 20, name="GameMatrix", align="^")
        self.layout.add_widget(Label("Black", 1, "^"), 0)
        self.layout.add_widget(self.matrix, 0)
        self.layout.add_widget(Label("White", 1, "^"), 0)
        self.move_text = Text(">", name="move", validator=self.__check, max_length=5)
        self.layout.add_widget(self.move_text, 1)
        self.fix()

    def __check(self, value: str):
        value = value.upper()

        if re.match(r'[A-H][1-8] [A-H][1-8]', value) is None:
            if len(value) == 5:
                self.scene.add_effect(PopUpDialog(self.screen, "Invalid move", ["Accept"]))
                self.move_text.value = ''
            return False

        return True

    def __make_move(self):
        chess_xy, move_xy = self.move_text.value.split()
        chess_x, chess_y = ord(chess_xy[0]) - 65, int(chess_xy[1]) - 1
        move_x, move_y = ord(move_xy[0]) - 65, int(move_xy[1]) - 1

        if self.game[chess_y][chess_x] != ' ':
            # self.game[chess_x][chess_y], self.game[move_x][move_y] = self.game[move_x][move_y], self.game[chess_x][
            #     chess_y]
            if self.game.move(chess_x, chess_y, move_x, move_y):
                pass
            self.move_text.value = ""

    def process_event(self, event):
        if event is not None and isinstance(event, KeyboardEvent) and event.key_code == 13:
            self.__make_move()
            event = None

        return super(GameScreen, self).process_event(event)

    def update(self, frame_no):
        self.matrix.text = str(self.game)
        super(GameScreen, self).update(frame_no)
