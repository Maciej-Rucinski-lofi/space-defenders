import math

from pygame.math import Vector2

from config.enemy import ENEMY_STEER_STRENGTH
from entities.enemy import Enemy
from entities.player import Player


def _rotation_from_velocity(velocity: Vector2) -> float:
    return math.atan2(velocity.x, -velocity.y)


def _steer_toward_player(enemy: Enemy, player: Player, dt: float) -> None:
    delta = player.position - enemy.position
    if delta.length_squared() == 0:
        return
    desired_velocity = delta.normalize() * enemy.speed
    blend = min(1.0, ENEMY_STEER_STRENGTH * dt)
    enemy.velocity = enemy.velocity.lerp(desired_velocity, blend)
    enemy.rotation = _rotation_from_velocity(enemy.velocity)


def _integrate_position(enemy: Enemy, dt: float) -> None:
    enemy.position += enemy.velocity * dt


def update_enemies(enemies: list[Enemy], player: Player, dt: float) -> None:
    for enemy in enemies:
        _steer_toward_player(enemy, player, dt)
        _integrate_position(enemy, dt)
