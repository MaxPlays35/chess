from asciimatics.exceptions import NextScene
from asciimatics.widgets import Frame, Layout, Label, Button, PopUpDialog


class MainScreen(Frame):
    def __init__(self, screen):
        super(MainScreen, self).__init__(screen, 12, screen.width - 20)

        layout = Layout([100])
        self.add_layout(layout)

        self.howto_label = Label("", height=2, align="^")
        layout.add_widget(Button("locally", self._play_locally))
        layout.add_widget(Button("with AI", self._play_ai))
        layout.add_widget(Button("over network", self._play_network))

        self.fix()

    def _play_locally(self):
        raise NextScene("GameScreenLocally")

    def _play_ai(self):
        raise NextScene("GameScreenWithAI")

    def _play_network(self):
        self.scene.add_effect(PopUpDialog(self.screen, "This feature will be implemented in future", ["Accept"]))

    def update(self, frame_no):
        super(MainScreen, self).update(frame_no)
