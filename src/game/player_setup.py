from pygame.math import Vector2

from config.player import FACING_LEFT_ROTATION, ROTATION_SPEED, THRUST_FORCE
from entities.player import Player


def create_center_player(window_width: int, window_height: int) -> Player:
    return Player(
        position=Vector2(window_width / 2, window_height / 2),
        velocity=Vector2(0, 0),
        rotation=FACING_LEFT_ROTATION,
        rotation_speed=ROTATION_SPEED,
        thrust_force=THRUST_FORCE,
        shoot_cooldown_remaining=0.0,
    )
