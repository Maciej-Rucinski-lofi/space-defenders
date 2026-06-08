import math

from pygame.math import Vector2

from config.enemy import ENEMY_HP
from config.formation import (
    PLACEHOLDER_ENEMY_COUNT,
    PLACEHOLDER_ENEMY_SPACING,
    PLACEHOLDER_ENEMY_Y,
)
from entities.enemy import Enemy
from entities.enemy_type import EnemyType
from systems.enemy_movement import initial_steering_state


def _rotation_facing_down() -> float:
    return math.pi


def create_placeholder_enemies(window_width: int) -> list[Enemy]:
    center_x = window_width / 2
    total_width = (PLACEHOLDER_ENEMY_COUNT - 1) * PLACEHOLDER_ENEMY_SPACING
    start_x = center_x - total_width / 2
    enemies: list[Enemy] = []
    for index in range(PLACEHOLDER_ENEMY_COUNT):
        steering_offset, behaviour_timer = initial_steering_state(EnemyType.CHASER)
        enemies.append(
            Enemy(
                position=Vector2(start_x + index * PLACEHOLDER_ENEMY_SPACING, PLACEHOLDER_ENEMY_Y),
                velocity=Vector2(0, 0),
                rotation=_rotation_facing_down(),
                speed=0.0,
                health=ENEMY_HP,
                enemy_type=EnemyType.CHASER,
                steering_offset=steering_offset,
                behaviour_timer=behaviour_timer,
                can_shoot=False,
            )
        )
    return enemies
