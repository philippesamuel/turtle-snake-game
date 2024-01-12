"""Scoreboard module for the snake game."""
from turtle import Turtle

from snake_game.config import settings
from snake_game.typings import Color, Font

COLOR: Color = settings.score_color
FONT: Font = settings.score_font
ALIGNMENT: str = settings.score_align


class Scoreboard(Turtle):
    """Scoreboard class for the snake game."""

    def __init__(self,
                 color: Color = COLOR,
                 font: Font = FONT,
                 align: str = ALIGNMENT) -> None:
        """Initialize the scoreboard."""
        super().__init__()
        self.score = 0
        self.color(color)
        self.font = font
        self.align = align
        self.penup()
        self.hideturtle()
        font_size = font[1]
        y = (self.screen.window_height()) // 2 - (font_size * 2)
        self.goto(x=0, y=y)
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """Update the scoreboard."""
        self.clear()
        self.write(arg=f"Score: {self.score}", align=self.align, font=self.font)

    def increase_score(self) -> None:
        """Increase the score."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self) -> None:
        """Display game over message."""
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER!", align="center", font=self.font)
