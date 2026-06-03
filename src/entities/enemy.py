from dataclasses import dataclass

from pygame.math import Vector2

from entities.enemy_type import EnemyType


@dataclass
class Enemy:
    position: Vector2
    velocity: Vector2
    rotation: float
    speed: float
    health: int
    enemy_type: EnemyType
    steering_offset: Vector2
    behaviour_timer: float
    can_shoot: bool
