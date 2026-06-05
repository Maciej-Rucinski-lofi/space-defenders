import pygame

from config.settings import WINDOW_HEIGHT, WINDOW_WIDTH
from config.wave import (
    WAVE_ANNOUNCEMENT_COLOR,
    WAVE_ANNOUNCEMENT_FONT_SIZE,
    WAVE_HUD_COLOR,
    WAVE_HUD_ENEMIES_COLOR,
    WAVE_HUD_FONT_SIZE,
    WAVE_HUD_GAP,
    WAVE_HUD_MARGIN_X,
    WAVE_HUD_MARGIN_Y,
)
from systems.wave_manager import WaveManager, WavePhase, enemies_remaining_in_wave

_HUD_FONT: pygame.font.Font | None = None
_ANNOUNCEMENT_FONT: pygame.font.Font | None = None


def _get_hud_font() -> pygame.font.Font:
    global _HUD_FONT
    if _HUD_FONT is None:
        _HUD_FONT = pygame.font.Font(None, WAVE_HUD_FONT_SIZE)
    return _HUD_FONT


def _get_announcement_font() -> pygame.font.Font:
    global _ANNOUNCEMENT_FONT
    if _ANNOUNCEMENT_FONT is None:
        _ANNOUNCEMENT_FONT = pygame.font.Font(None, WAVE_ANNOUNCEMENT_FONT_SIZE)
    return _ANNOUNCEMENT_FONT


def draw_wave_hud(
    surface: pygame.Surface,
    wave_manager: WaveManager,
    active_enemy_count: int,
) -> None:
    font = _get_hud_font()
    wave_label = f"Wave {wave_manager.wave_number}"
    wave_surface = font.render(wave_label, True, WAVE_HUD_COLOR)
    surface.blit(wave_surface, (WAVE_HUD_MARGIN_X, WAVE_HUD_MARGIN_Y))

    enemies_left = enemies_remaining_in_wave(wave_manager, active_enemy_count)
    enemies_label = f"Enemies: {enemies_left}"
    enemies_surface = font.render(enemies_label, True, WAVE_HUD_ENEMIES_COLOR)
    enemies_x = WAVE_HUD_MARGIN_X + wave_surface.get_width() + WAVE_HUD_GAP
    surface.blit(enemies_surface, (enemies_x, WAVE_HUD_MARGIN_Y))


def draw_wave_announcement(
    surface: pygame.Surface, wave_manager: WaveManager
) -> None:
    if wave_manager.phase is not WavePhase.ANNOUNCING:
        return

    label = f"Wave: {wave_manager.wave_number}"
    text_surface = _get_announcement_font().render(label, True, WAVE_ANNOUNCEMENT_COLOR)
    text_rect = text_surface.get_rect(
        center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    )
    surface.blit(text_surface, text_rect)
