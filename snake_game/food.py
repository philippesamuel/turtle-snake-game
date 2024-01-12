"""Food class for snake game."""
from random import randint
from turtle import Turtle

from snake_game.config import settings
from snake_game.typings import Color


class Food(Turtle):
    """Food class for snake game.

    Food is a turtle that moves to a random position on the screen.
    This currently relies on inheritance from Turtle, but could be
    refactored to composition.

    """
    def __init__(self, color: Color = settings.food_color, shape: str = settings.food_shape) -> None:
        super().__init__(shape=shape)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(color)
        self.speed("fastest")
        self.refresh()

    def refresh(self) -> None:
        """Refresh food position."""
        window_width = self.screen.window_width() * 0.92
        window_height = self.screen.window_height() * 0.92

        x_max = int(window_width // 2)
        y_max = int(window_height // 2)

        self.goto(x=randint(-x_max, x_max), y=randint(-y_max, y_max))
