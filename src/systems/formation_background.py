import random

import pygame

from config.formation import (
    FORMATION_LABEL_COLOR,
    FORMATION_LABEL_FONT_SIZE,
    FORMATION_LABEL_MARGIN_Y,
    FORMATION_STAR_COLOR,
    FORMATION_STAR_COUNT,
    FORMATION_STAR_SCROLL_SPEED,
    PLAYER_ZONE_LINE_COLOR,
)


class ScrollingStarfield:
    def __init__(self, width: int, height: int, star_count: int = FORMATION_STAR_COUNT) -> None:
        self._width = width
        self._height = height
        self._stars = [
            (random.randint(0, width - 1), random.randint(0, height - 1))
            for _ in range(star_count)
        ]

    def update(self, dt: float) -> None:
        scroll = FORMATION_STAR_SCROLL_SPEED * dt
        updated: list[tuple[int, int]] = []
        for x, y in self._stars:
            new_y = y + scroll
            while new_y >= self._height:
                new_y -= self._height
            updated.append((x, int(new_y)))
        self._stars = updated

    def draw(self, surface: pygame.Surface) -> None:
        for x, y in self._stars:
            surface.set_at((x, y), FORMATION_STAR_COLOR)


def draw_formation_label(screen: pygame.Surface, font: pygame.font.Font) -> None:
    label = font.render("Formation Mode", True, FORMATION_LABEL_COLOR)
    screen.blit(label, (FORMATION_LABEL_MARGIN_Y, FORMATION_LABEL_MARGIN_Y))


def draw_player_zone_line(screen: pygame.Surface, zone_top_y: float) -> None:
    width = screen.get_width()
    pygame.draw.line(
        screen,
        PLAYER_ZONE_LINE_COLOR,
        (0, int(zone_top_y)),
        (width, int(zone_top_y)),
        1,
    )
