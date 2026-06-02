from dataclasses import dataclass

from pygame.math import Vector2


@dataclass
class Enemy:
    position: Vector2
    velocity: Vector2
    rotation: float
    speed: float
    health: int
