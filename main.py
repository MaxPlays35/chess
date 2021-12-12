from asciimatics.scene import Scene
from asciimatics.screen import Screen

from screens import GameScreen


def main(screen: Screen):
    # screen.play([Scene([MainScreen(screen)], -1, "MainScreen")])
    # screen.play([Scene([GameScreen(screen)], -1, name="GameScreen")])
    try:
        screen.play([Scene([GameScreen(screen)], -1, "GameScreen")])
    except KeyboardInterrupt:
        exit(0)


Screen.wrapper(main)
