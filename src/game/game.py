import pygame

from config.settings import (
    BACKGROUND_COLOR,
    TARGET_FPS,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)
from game.starfield import Starfield
from levels.level_manager import LevelManager
from levels.level_type import LevelType


class Game:
    def __init__(self) -> None:
        pygame.init()
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self._running = True
        self._starfield = Starfield(WINDOW_WIDTH, WINDOW_HEIGHT)
        self._level_manager = LevelManager(WINDOW_WIDTH, WINDOW_HEIGHT)
        self._level_manager.switch_to(LevelType.SURVIVAL)

    def run(self) -> None:
        while self._running:
            dt = self._clock.tick(TARGET_FPS) / 1000.0
            self._handle_events()
            self._update(dt)
            self._render()
        if self._level_manager.active_level is not None:
            self._level_manager.active_level.cleanup()
        pygame.quit()

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._running = False
                elif event.key == pygame.K_F3:
                    self._level_manager.toggle_debug()
                elif event.key == pygame.K_F5:
                    self._level_manager.switch_to(LevelType.FORMATION)
                elif event.key == pygame.K_F6:
                    self._level_manager.switch_to(LevelType.SURVIVAL)

    def _update(self, dt: float) -> None:
        self._level_manager.update(dt)

    def _render(self) -> None:
        self._screen.fill(BACKGROUND_COLOR)
        self._starfield.draw(self._screen)
        self._level_manager.render(self._screen)
        pygame.display.flip()
