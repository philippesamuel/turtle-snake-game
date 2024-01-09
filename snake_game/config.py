from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from snake_game.typings import Color


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")

    # Screen settings
    screen_width: int = Field(default=800)
    screen_height: int = Field(default=600)
    screen_bg_color: Color = Field(default=(0, 0, 0), description="Screen backgroud color as RGB tuple or color name")
    screen_title: str = Field(default="My Snake Game")

    # Snake settings
    snake_start_size: int = Field(default=3, description="Number of blocks in the snake")
    snake_color: Color = Field(default=(1, 1, 1), description="Snake color as RGB tuple or color name")
    snake_segment_shape: str = Field(default="square")


settings = Settings()
