"""Food class for snake game."""
from random import randint
from turtle import Turtle

from snake_game.config import settings
from snake_game.typings import Color


class Food(Turtle):
    """Food class for snake game."""
    def __init__(self, color: Color = settings.food_color, shape: str = settings.food_shape) -> None:
        super().__init__(shape=shape)
        self.penup()
        self.color(color)
        self.speed("fastest")
        self.refresh()

    def refresh(self) -> None:
        """Refresh food position."""
        x_max = self.screen.window_width() // 2
        y_max = self.screen.window_height() // 2
        self.goto(x=randint(-x_max, x_max), y=randint(-y_max, y_max))
