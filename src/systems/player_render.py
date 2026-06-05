import math

import pygame
from pygame.math import Vector2

from config.player import SHIP_COLOR, SHIP_LOCAL_VERTICES, SHIP_OUTLINE_COLOR
from entities.player import Player


def _rotate_vertex(vertex: Vector2, rotation: float) -> Vector2:
    sin_r = math.sin(rotation)
    cos_r = math.cos(rotation)
    return Vector2(
        vertex.x * cos_r - vertex.y * sin_r,
        vertex.x * sin_r + vertex.y * cos_r,
    )


def _ship_vertices(player: Player) -> list[tuple[int, int]]:
    world_vertices: list[tuple[int, int]] = []
    for local in SHIP_LOCAL_VERTICES:
        rotated = _rotate_vertex(local, player.rotation)
        world = player.position + rotated
        world_vertices.append((int(world.x), int(world.y)))
    return world_vertices


def draw_player(surface: pygame.Surface, player: Player) -> None:
    if player.is_destroyed:
        return
    vertices = _ship_vertices(player)
    pygame.draw.polygon(surface, SHIP_COLOR, vertices)
    pygame.draw.polygon(surface, SHIP_OUTLINE_COLOR, vertices, 1)
