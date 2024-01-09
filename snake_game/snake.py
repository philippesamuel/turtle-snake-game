from itertools import pairwise
from turtle import Turtle

from typings import Color, TurtleCallback
from config import settings

UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0


class Snake:
    _segments: list[Turtle]

    def __init__(self,
                 size: int = settings.snake_start_size,
                 color: Color = settings.snake_color,
                 segment_shape: str = settings.snake_segment_shape) -> None:
        x_positions = (0 - i * 20 for i in range(size))
        self._segments = [create_segment(shape=segment_shape, color=color, x=x, y=0) for x in x_positions]

    @property
    def head(self) -> Turtle:
        return self._segments[0]

    def move(self, move_func: TurtleCallback) -> None:
        reversed_segments = self._segments[::-1]
        for s0, s1 in pairwise(reversed_segments):
            s0.goto(s1.position())
        move_func(self.head)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


def create_segment(shape: str, color: Color, x: int, y: int = 0) -> Turtle:
    segment = Turtle(shape=shape)
    segment.penup()
    segment.color(color)
    segment.goto(x=x, y=y)
    return segment
