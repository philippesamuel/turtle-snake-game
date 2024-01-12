"""Snake class and helper functions."""
from itertools import pairwise
from turtle import Turtle

from typings import Color, TurtleCallback
from config import settings

UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0

START_SIZE: int = settings.snake_start_size
COLOR: Color = settings.snake_color
SEGMENT_SHAPE: str = settings.snake_segment_shape


class Snake:
    """Snake class for snake game."""

    _segments: list[Turtle]
    """List of turtle segments that make up the snake."""

    def __init__(self,
                 size: int = START_SIZE,
                 color: Color = COLOR,
                 segment_shape: str = SEGMENT_SHAPE) -> None:
        """Initialize snake."""
        x_positions = (0 - i * 20 for i in range(size))
        self._segments = [create_segment(shape=segment_shape, color=color, x=x, y=0) for x in x_positions]

    @property
    def head(self) -> Turtle:
        """Head of the snake."""
        return self._segments[0]

    @property
    def tail(self) -> Turtle:
        """Tail of the snake."""
        return self._segments[-1]

    def move(self, move_func: TurtleCallback) -> None:
        """Move snake according to `move_func`.

        Args:
            move_func: Function that moves the snake head.

        """
        reversed_segments = self._segments[::-1]
        for s0, s1 in pairwise(reversed_segments):
            s0.goto(s1.position())
        move_func(self.head)

    def up(self) -> None:
        """Turn snake upwards."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        """Turn snake downwards."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        """Turn snake to the left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        """Turn snake to the right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self) -> None:
        """Extend snake's body by one segment."""
        segment = self.create_segment(x=self.tail.xcor(), y=self.tail.ycor())
        self._segments.append(segment)

    def create_segment(self, x: float, y: float = 0) -> Turtle:
        """Create a new segment at position (x, y).

        Args:
            x: x-coordinate of new segment.
            y: y-coordinate of new segment.

        Returns:
            New segment (Turtle object).

        """
        segment = Turtle(shape=self.head.shape())
        segment.penup()
        segment.color(self.head.pencolor())
        segment.goto(x=x, y=y)
        return segment


def create_segment(shape: str, color: Color, x: float, y: float = 0) -> Turtle:
    """Create a new segment at position (x, y).

    Args:
        shape: Shape of new segment.
        color: Color of new segment.
        x: x-coordinate of new segment.
        y: y-coordinate of new segment.

    Returns:
        New segment (Turtle object).

    """
    segment = Turtle(shape=shape)
    segment.penup()
    segment.color(color)
    segment.goto(x=x, y=y)
    return segment
