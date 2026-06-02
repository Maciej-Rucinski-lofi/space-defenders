import random

import pygame

STAR_COUNT = 800
STAR_COLOR = (255, 255, 255)


class Starfield:
    def __init__(self, width: int, height: int, star_count: int = STAR_COUNT) -> None:
        self._stars = [
            (random.randint(0, width - 1), random.randint(0, height - 1))
            for _ in range(star_count)
        ]

    def draw(self, surface: pygame.Surface) -> None:
        for x, y in self._stars:
            surface.set_at((x, y), STAR_COLOR)
