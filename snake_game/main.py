"""Main module for the snake game."""
import time
from turtle import Screen
from typing import Callable

from snake_game.config import settings
from snake_game.snake import Snake
from snake_game.food import Food


def main() -> None:
    """Main function. Entry point for the snake game."""
    screen = Screen()
    screen.setup(width=settings.screen_width, height=settings.screen_height)
    screen.bgcolor(settings.screen_bg_color)
    screen.title(settings.screen_title)
    screen.tracer(0)

    snake = Snake()
    food = Food()
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

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()

    screen.exitonclick()


if __name__ == '__main__':
    main()
