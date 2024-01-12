"""Scoreboard module for the snake game."""
from turtle import Turtle

from snake_game.config import settings
from snake_game.typings import Color, Font


class Scoreboard(Turtle):
    """Scoreboard class for the snake game."""

    def __init__(self,
                 color: Color = settings.score_color,
                 font: Font = settings.score_font,
                 align: str = settings.score_align) -> None:
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
