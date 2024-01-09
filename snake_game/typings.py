from turtle import Turtle
from typing import Callable

Color = tuple[float, float, float] | str
TurtleCallback = Callable[[Turtle], None]
