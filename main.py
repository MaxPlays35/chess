from asciimatics.scene import Scene
from asciimatics.screen import Screen

from screens import GameScreen, MainScreen, GameScreenWithAI


def main(screen: Screen):
    scenes = [
        Scene([MainScreen(screen)], -1, name="MainScreen"),
        Scene([GameScreen(screen)], -1, name="GameScreenLocally"),
        Scene([GameScreenWithAI(screen)], -1, name="GameScreenWithAI")
    ]
    try:
        screen.play(scenes)
    except KeyboardInterrupt:
        exit(0)


Screen.wrapper(main)
