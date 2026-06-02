from dataclasses import dataclass

from pygame.math import Vector2


@dataclass
class Bullet:
    position: Vector2
    velocity: Vector2
    direction: Vector2
    time_remaining: float
