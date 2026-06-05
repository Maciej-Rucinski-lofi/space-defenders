import pygame
from pygame.math import Vector2

from entities.enemy import Enemy
from entities.player import Player
from game.player_setup import nearest_alive_player

TARGET_LINE_LENGTH = 60.0
VELOCITY_LINE_SCALE = 0.35
TARGET_LINE_COLOR = (100, 255, 100)
VELOCITY_LINE_COLOR = (100, 180, 255)


def _target_direction(enemy: Enemy, player_position: Vector2) -> Vector2 | None:
    delta = player_position - enemy.position
    if delta.length_squared() == 0:
        return None
    base = delta.normalize()
    combined = base + enemy.steering_offset
    if combined.length_squared() == 0:
        return base
    return combined.normalize()


def draw_enemy_debug(
    surface: pygame.Surface,
    enemies: list[Enemy],
    players: list[Player],
) -> None:
    for enemy in enemies:
        target = nearest_alive_player(players, enemy.position)
        if target is None:
            continue
        target_dir = _target_direction(enemy, target.position)
        if target_dir is not None:
            target_end = enemy.position + target_dir * TARGET_LINE_LENGTH
            pygame.draw.line(
                surface,
                TARGET_LINE_COLOR,
                enemy.position,
                target_end,
                1,
            )
        if enemy.velocity.length_squared() > 0:
            velocity_end = enemy.position + enemy.velocity * VELOCITY_LINE_SCALE
            pygame.draw.line(
                surface,
                VELOCITY_LINE_COLOR,
                enemy.position,
                velocity_end,
                2,
            )
