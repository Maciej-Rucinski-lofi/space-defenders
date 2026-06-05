import pygame

from config.player import (
    HEALTH_HUD_COLOR,
    HEALTH_HUD_FONT_SIZE,
    HEALTH_HUD_LINE_GAP,
    HEALTH_HUD_MARGIN_X,
    HEALTH_HUD_MARGIN_Y,
)
from entities.player import Player

_FONT: pygame.font.Font | None = None


def _get_font() -> pygame.font.Font:
    global _FONT
    if _FONT is None:
        _FONT = pygame.font.Font(None, HEALTH_HUD_FONT_SIZE)
    return _FONT


def draw_health_hud(surface: pygame.Surface, players: list[Player]) -> None:
    font = _get_font()
    y = HEALTH_HUD_MARGIN_Y
    for index, player in enumerate(players, start=1):
        label = f"P{index} HP: {player.health}"
        text_surface = font.render(label, True, HEALTH_HUD_COLOR)
        surface.blit(text_surface, (HEALTH_HUD_MARGIN_X, y))
        y += text_surface.get_height() + HEALTH_HUD_LINE_GAP
