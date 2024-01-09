import time
from turtle import Screen
from typing import Callable

from snake import Snake

from config import settings


def main() -> None:
    screen = Screen()
    screen.setup(width=settings.screen_width, height=settings.screen_height)
    screen.bgcolor(settings.screen_bg_color)
    screen.title(settings.screen_title)
    screen.tracer(0)

    snake = Snake()
    screen.listen()

    key_bindings: dict[str, Callable[[None], None]] = {
        "Up": snake.up,
        "Down": snake.down,
        "Left": snake.left,
        "Right": snake.right
    }

    for key, callback in key_bindings.items():
        screen.onkey(key=key, fun=callback)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move(lambda t: t.forward(20))

    screen.exitonclick()


if __name__ == '__main__':
    main()
