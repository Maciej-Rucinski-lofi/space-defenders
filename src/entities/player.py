from dataclasses import dataclass

from pygame.math import Vector2


@dataclass
class Player:
    position: Vector2
    velocity: Vector2
    rotation: float
    rotation_speed: float
    thrust_force: float
    shoot_cooldown_remaining: float
    health: int
    max_health: int
    is_destroyed: bool
