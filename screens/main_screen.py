from asciimatics.widgets import Frame, Layout, Label, Button


class MainScreen(Frame):
    def __init__(self, screen):
        super(MainScreen, self).__init__(screen, 12, screen.width - 20)

        layout = Layout([100])
        self.add_layout(layout)

        self.howto_label = Label("", height=2, align="^")
        layout.add_widget(Button('locally', self._play_locally))
        layout.add_widget(Button('with AI', self._play_ai))
        layout.add_widget(Button('over network', self._play_network))

        layout.add_widget(Label('\nOther', height=2, align='^'))
        layout.add_widget(Button('scoreboard', self._scoreboard))

        self.fix()

    def _play_locally(self):
        pass

    def _play_ai(self):
        pass

    def _play_network(self):
        pass

    def _scoreboard(self):
        pass
    
    def update(self, frame_no):
        super(MainScreen, self).update(frame_no)
