from abc import ABC, abstractmethod

import pygame


class BaseLevel(ABC):
    @abstractmethod
    def initialize(self) -> None:
        pass

    @abstractmethod
    def update(self, dt: float) -> None:
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        pass

    @abstractmethod
    def cleanup(self) -> None:
        pass

    @abstractmethod
    def is_complete(self) -> bool:
        pass

    def toggle_debug(self) -> None:
        pass
