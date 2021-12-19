from asciimatics.effects import Print
from asciimatics.particles import Explosion, Rain
from asciimatics.renderers import FigletText
from asciimatics.widgets import Frame


class StartScreen(Frame):
    def __init__(self, screen):
        super(StartScreen, self).__init__(screen, screen.height, screen.width)

    def update(self, frame_no):
        if frame_no == 1:
            author = FigletText("By MaxPlays35")
            new_year = FigletText("Happy New Year!", "banner3")
            rain = Rain(self.screen, 40)
            explosion1 = Explosion(self.screen, self.screen.width // 2 - 35, self.screen.height // 2 - 5, 40)
            explosion2 = Explosion(self.screen, self.screen.width // 2 + 35, self.screen.height // 2 - 5, 40)
            explosion3 = Explosion(self.screen, self.screen.width // 2 - 45, self.screen.height // 2 + 5, 40)
            explosion4 = Explosion(self.screen, self.screen.width // 2 + 45, self.screen.height // 2 + 5, 40)

            effects = [
                rain,
                explosion1, explosion2, explosion3, explosion4,
                Print(self.screen, author, (self.screen.height - 4) // 2, speed=1),
                Print(self.screen, new_year, (self.screen.height + 20) // 2, speed=1)
            ]

            for effect in effects:
                self.scene.add_effect(effect)
