from dataclasses import dataclass

from pygame.math import Vector2


@dataclass
class Player:
    position: Vector2
    velocity: Vector2
    rotation: float
    rotation_speed: float
    thrust_force: float
