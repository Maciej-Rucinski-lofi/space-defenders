import pygame

from levels.base_level import BaseLevel
from levels.formation_level import FormationLevel
from levels.level_type import LevelType
from levels.survival_level import SurvivalLevel


class LevelManager:
    def __init__(self, window_width: int, window_height: int) -> None:
        self._window_width = window_width
        self._window_height = window_height
        self._active_level: BaseLevel | None = None
        self._active_level_type: LevelType | None = None

    @property
    def active_level(self) -> BaseLevel | None:
        return self._active_level

    @property
    def active_level_type(self) -> LevelType | None:
        return self._active_level_type

    def switch_to(self, level_type: LevelType) -> None:
        if self._active_level_type is level_type:
            return

        if self._active_level is not None:
            self._active_level.cleanup()

        self._active_level = self._create_level(level_type)
        self._active_level_type = level_type
        self._active_level.initialize()

    def update(self, dt: float) -> None:
        if self._active_level is not None:
            self._active_level.update(dt)

    def render(self, screen: pygame.Surface) -> None:
        if self._active_level is not None:
            self._active_level.render(screen)

    def toggle_debug(self) -> None:
        if self._active_level is not None:
            self._active_level.toggle_debug()

    def _create_level(self, level_type: LevelType) -> BaseLevel:
        if level_type is LevelType.SURVIVAL:
            return SurvivalLevel(self._window_width, self._window_height)
        if level_type is LevelType.FORMATION:
            return FormationLevel()
        raise ValueError(f"Unknown level type: {level_type}")
