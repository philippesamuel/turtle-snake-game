"""Main module for the snake game."""
import time
from turtle import Screen
from typing import Callable

from snake_game.config import settings
from snake_game.scoreboard import Scoreboard
from snake_game.snake import Snake
from snake_game.food import Food
from snake_game.typings import Color

SCREEN_WIDTH: int = settings.screen_width
SCREEN_HEIGHT: int = settings.screen_height
SCREEN_BG_COLOR: Color = settings.screen_bg_color
SCREEN_TITLE: str = settings.screen_title


def main() -> None:
    """Main function. Entry point for the snake game."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_BG_COLOR)
    screen.title(SCREEN_TITLE)
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
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
            scoreboard.increase_score()

        # Detect collision with wall
        x_max = (SCREEN_WIDTH / 2) - 20
        y_max = (SCREEN_HEIGHT / 2) - 20
        if (snake.head.xcor() > x_max or snake.head.xcor() < -x_max
                or snake.head.ycor() > y_max or snake.head.ycor() < -y_max):
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()


if __name__ == '__main__':
    main()
