import math
import random
from dataclasses import dataclass
from enum import Enum, auto

from pygame.math import Vector2

from config.enemy import (
    ENEMY_HP,
    ENEMY_SPAWN_INTERVAL_S,
    ENEMY_SPAWN_OFFSET,
    ENEMY_SPEED,
)
from config.settings import WINDOW_HEIGHT, WINDOW_WIDTH
from entities.enemy import Enemy
from entities.player import Player


class ScreenEdge(Enum):
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()


@dataclass
class EnemySpawner:
    spawn_timer_remaining: float


def create_enemy_spawner() -> EnemySpawner:
    return EnemySpawner(spawn_timer_remaining=ENEMY_SPAWN_INTERVAL_S)


def _random_edge() -> ScreenEdge:
    return random.choice(list(ScreenEdge))


def _spawn_position(edge: ScreenEdge, offset: float) -> Vector2:
    width = float(WINDOW_WIDTH)
    height = float(WINDOW_HEIGHT)
    if edge is ScreenEdge.TOP:
        return Vector2(random.uniform(0, width), -offset)
    if edge is ScreenEdge.BOTTOM:
        return Vector2(random.uniform(0, width), height + offset)
    if edge is ScreenEdge.LEFT:
        return Vector2(-offset, random.uniform(0, height))
    return Vector2(width + offset, random.uniform(0, height))


def _direction_toward(target: Vector2, origin: Vector2) -> Vector2:
    delta = target - origin
    if delta.length_squared() == 0:
        return Vector2(1, 0)
    return delta.normalize()


def _rotation_from_velocity(velocity: Vector2) -> float:
    return math.atan2(velocity.x, -velocity.y)


def _create_enemy(position: Vector2, target: Vector2) -> Enemy:
    direction = _direction_toward(target, position)
    velocity = direction * ENEMY_SPEED
    return Enemy(
        position=position,
        velocity=velocity,
        rotation=_rotation_from_velocity(velocity),
        speed=ENEMY_SPEED,
        health=ENEMY_HP,
    )


def _spawn_enemy(player: Player) -> Enemy:
    edge = _random_edge()
    position = _spawn_position(edge, ENEMY_SPAWN_OFFSET)
    return _create_enemy(position, player.position)


def update_enemy_spawner(
    spawner: EnemySpawner,
    enemies: list[Enemy],
    player: Player,
    dt: float,
) -> None:
    spawner.spawn_timer_remaining -= dt
    if spawner.spawn_timer_remaining > 0:
        return
    enemies.append(_spawn_enemy(player))
    spawner.spawn_timer_remaining = ENEMY_SPAWN_INTERVAL_S
