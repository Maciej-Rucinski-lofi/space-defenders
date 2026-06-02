import math

from pygame.math import Vector2

from entities.player import Player

ROTATION_SPEED = 3.0
THRUST_FORCE = 280.0
FACING_LEFT_ROTATION = -math.pi / 2

SHIP_LOCAL_VERTICES: tuple[Vector2, ...] = (
    Vector2(0, -18),
    Vector2(-12, 12),
    Vector2(12, 12),
)

SHIP_COLOR = (0, 220, 255)
SHIP_OUTLINE_COLOR = (200, 240, 255)


def create_center_player(window_width: int, window_height: int) -> Player:
    return Player(
        position=Vector2(window_width / 2, window_height / 2),
        velocity=Vector2(0, 0),
        rotation=FACING_LEFT_ROTATION,
        rotation_speed=ROTATION_SPEED,
        thrust_force=THRUST_FORCE,
    )
