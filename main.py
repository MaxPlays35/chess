from asciimatics.scene import Scene
from asciimatics.screen import Screen

from screens import GameScreen, MainScreen, GameScreenWithAI, StartScreen


def main(screen: Screen):
    scenes = [
        Scene([StartScreen(screen)], 40, name="StartScreen"),
        Scene([MainScreen(screen)], -1, name="MainScreen"),
        Scene([GameScreen(screen)], -1, name="GameScreenLocally"),
        Scene([GameScreenWithAI(screen)], -1, name="GameScreenWithAI")
    ]
    try:
        screen.play(scenes)
    except KeyboardInterrupt:
        exit(0)


Screen.wrapper(main)
