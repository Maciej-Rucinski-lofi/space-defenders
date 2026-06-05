import pygame

from config.game_state import (
    GAME_OVER_SUBTITLE_COLOR,
    GAME_OVER_SUBTITLE_FONT_SIZE,
    GAME_OVER_SUBTITLE_GAP,
    GAME_OVER_TITLE_COLOR,
    GAME_OVER_TITLE_FONT_SIZE,
)
from config.settings import WINDOW_HEIGHT, WINDOW_WIDTH
from systems.game_state import GamePhase, GameState

_TITLE_FONT: pygame.font.Font | None = None
_SUBTITLE_FONT: pygame.font.Font | None = None


def _get_title_font() -> pygame.font.Font:
    global _TITLE_FONT
    if _TITLE_FONT is None:
        _TITLE_FONT = pygame.font.Font(None, GAME_OVER_TITLE_FONT_SIZE)
    return _TITLE_FONT


def _get_subtitle_font() -> pygame.font.Font:
    global _SUBTITLE_FONT
    if _SUBTITLE_FONT is None:
        _SUBTITLE_FONT = pygame.font.Font(None, GAME_OVER_SUBTITLE_FONT_SIZE)
    return _SUBTITLE_FONT


def draw_game_over(
    surface: pygame.Surface, game_state: GameState, wave_reached: int
) -> None:
    if game_state.phase is not GamePhase.GAME_OVER:
        return

    title_surface = _get_title_font().render("GAME OVER", True, GAME_OVER_TITLE_COLOR)
    subtitle_surface = _get_subtitle_font().render(
        f"Wave Reached: {wave_reached}", True, GAME_OVER_SUBTITLE_COLOR
    )
    title_rect = title_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    subtitle_y = title_rect.bottom + GAME_OVER_SUBTITLE_GAP
    subtitle_rect = subtitle_surface.get_rect(
        center=(WINDOW_WIDTH // 2, subtitle_y + subtitle_surface.get_height() // 2)
    )
    surface.blit(title_surface, title_rect)
    surface.blit(subtitle_surface, subtitle_rect)
