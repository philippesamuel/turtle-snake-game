from turtle import Turtle
from typing import Callable

Color = tuple[float, float, float] | str
Font = tuple[str, int, str]
TurtleCallback = Callable[[Turtle], None]
