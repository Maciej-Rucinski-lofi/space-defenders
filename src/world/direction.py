import math

from pygame.math import Vector2


def forward_direction(rotation: float) -> Vector2:
    return Vector2(math.sin(rotation), -math.cos(rotation))
