import re
import time

from asciimatics.event import KeyboardEvent
from asciimatics.widgets import Frame, Layout, Label, Text, PopUpDialog
from itertools import islice

from gameboard import GameBoard


class GameScreen(Frame):
    def __init__(self, screen):
        super(GameScreen, self).__init__(screen, screen.height - 20, screen.width - 20)
        self.game = GameBoard()

        self.layout = Layout([1, 1])

        self.time = time.time()

        self.add_layout(self.layout)

        self.matrix = Label("", 20, name="GameMatrix", align="^")

        self.layout.add_widget(Label("Black", 1, "^"), 0)
        self.layout.add_widget(self.matrix, 0)
        self.layout.add_widget(Label("White", 1, "^"), 0)

        self.move_text = Text(">", name="move", validator=self.__check, max_length=5)
        self.layout.add_widget(self.move_text, 1)

        self.time_label = Label("Turn ", 1)
        self.layout.add_widget(self.time_label, 1)

        self.turn_text = Label("", 1)
        self.layout.add_widget(self.turn_text, 1)

        self.history = Label('- ', 8)
        self.layout.add_widget(self.history, 1)

        self.fix()

    def __check(self, value: str):
        value = value.upper()

        if re.match(r'[A-H][1-8] [A-H][1-8]', value) is None or len(value) < 5:
            if len(value) == 5:
                self.scene.add_effect(PopUpDialog(self.screen, "Invalid move", ["Accept"]))
                self.move_text.value = ''
            return False

        return True

    def __make_move(self):
        if len(self.move_text.value) == 5:
            chess_xy, move_xy = self.move_text.value.upper().split()
        else:
            self.scene.add_effect(PopUpDialog(self.screen, "Invalid move", ["Accept"]))
            self.move_text.value = ''
            return

        if self.game.move(chess_xy, move_xy, time.time() - self.time):
            self.time = time.time()
        self.move_text.value = ""

    def process_event(self, event):
        if event is not None and isinstance(event, KeyboardEvent) and event.key_code == 13:
            self.__make_move()
            event = None

        return super(GameScreen, self).process_event(event)

    def update(self, frame_no):
        self.matrix.text = str(self.game)
        self.time_label.text = f'Turn duration: {int(time.time() - self.time)} s'
        self.turn_text.text = f'{ "Black" if not self.game.is_white_turn else "White" } turn'
        self.history.text = '\n'.join(islice(self.game.history, 8))
        super(GameScreen, self).update(frame_no)
