import math

import pygame
from pygame.math import Vector2

from config.enemy import ENEMY_COLOR, ENEMY_LOCAL_VERTICES, ENEMY_OUTLINE_COLOR
from entities.enemy import Enemy


def _rotate_vertex(vertex: Vector2, rotation: float) -> Vector2:
    sin_r = math.sin(rotation)
    cos_r = math.cos(rotation)
    return Vector2(
        vertex.x * cos_r - vertex.y * sin_r,
        vertex.x * sin_r + vertex.y * cos_r,
    )


def _enemy_vertices(enemy: Enemy) -> list[tuple[int, int]]:
    world_vertices: list[tuple[int, int]] = []
    for local in ENEMY_LOCAL_VERTICES:
        rotated = _rotate_vertex(local, enemy.rotation)
        world = enemy.position - rotated
        world_vertices.append((int(world.x), int(world.y)))
    return world_vertices


def draw_enemies(surface: pygame.Surface, enemies: list[Enemy]) -> None:
    for enemy in enemies:
        vertices = _enemy_vertices(enemy)
        pygame.draw.polygon(surface, ENEMY_COLOR, vertices)
        pygame.draw.polygon(surface, ENEMY_OUTLINE_COLOR, vertices, 1)
