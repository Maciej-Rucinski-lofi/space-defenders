import pygame

from config.settings import WINDOW_HEIGHT, WINDOW_WIDTH
from levels.base_level import BaseLevel


class FormationLevel(BaseLevel):
    def __init__(self) -> None:
        self._font: pygame.font.Font | None = None

    def initialize(self) -> None:
        self._font = pygame.font.Font(None, 48)

    def update(self, dt: float) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        if self._font is None:
            return
        title = self._font.render("Formation Level", True, (200, 200, 255))
        subtitle = self._font.render("(placeholder)", True, (150, 150, 180))
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30))
        subtitle_rect = subtitle.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 30)
        )
        screen.blit(title, title_rect)
        screen.blit(subtitle, subtitle_rect)

    def cleanup(self) -> None:
        self._font = None

    def is_complete(self) -> bool:
        return False
