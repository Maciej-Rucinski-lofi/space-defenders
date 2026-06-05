import math
from dataclasses import dataclass
from enum import Enum, auto

from pygame.math import Vector2

from config.enemy import (
    ENEMY_HP,
    ENEMY_SPAWN_INTERVAL_S,
    ENEMY_SPAWN_OFFSET,
    ENEMY_SPEED,
)
from config.enemy_behaviour import ENEMY_TYPE_PROFILES
from config.settings import WINDOW_HEIGHT, WINDOW_WIDTH
from entities.enemy import Enemy
from entities.enemy_type import EnemyType
from entities.player import Player
from systems.enemy_movement import initial_steering_state
from world.enemy_rng import get_enemy_rng


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
    return get_enemy_rng().choice(list(ScreenEdge))


def _random_enemy_type() -> EnemyType:
    return get_enemy_rng().choice(list(EnemyType))


def _spawn_position(edge: ScreenEdge, offset: float) -> Vector2:
    rng = get_enemy_rng()
    width = float(WINDOW_WIDTH)
    height = float(WINDOW_HEIGHT)
    if edge is ScreenEdge.TOP:
        return Vector2(rng.uniform(0, width), -offset)
    if edge is ScreenEdge.BOTTOM:
        return Vector2(rng.uniform(0, width), height + offset)
    if edge is ScreenEdge.LEFT:
        return Vector2(-offset, rng.uniform(0, height))
    return Vector2(width + offset, rng.uniform(0, height))


def _direction_toward(target: Vector2, origin: Vector2) -> Vector2:
    delta = target - origin
    if delta.length_squared() == 0:
        return Vector2(1, 0)
    return delta.normalize()


def _rotation_from_velocity(velocity: Vector2) -> float:
    return math.atan2(velocity.x, -velocity.y)


def _create_enemy(position: Vector2, target: Vector2, enemy_type: EnemyType) -> Enemy:
    profile = ENEMY_TYPE_PROFILES[enemy_type]
    speed = ENEMY_SPEED * profile.speed_multiplier
    direction = _direction_toward(target, position)
    velocity = direction * speed
    steering_offset, behaviour_timer = initial_steering_state(enemy_type)
    return Enemy(
        position=position,
        velocity=velocity,
        rotation=_rotation_from_velocity(velocity),
        speed=speed,
        health=ENEMY_HP,
        enemy_type=enemy_type,
        steering_offset=steering_offset,
        behaviour_timer=behaviour_timer,
        can_shoot=profile.can_shoot,
    )


def _spawn_enemy(player: Player) -> Enemy:
    edge = _random_edge()
    position = _spawn_position(edge, ENEMY_SPAWN_OFFSET)
    enemy_type = _random_enemy_type()
    return _create_enemy(position, player.position, enemy_type)


def update_enemy_spawner(
    spawner: EnemySpawner,
    enemies: list[Enemy],
    player: Player,
    dt: float,
    spawn_allowed: bool,
) -> bool:
    if not spawn_allowed:
        return False
    spawner.spawn_timer_remaining -= dt
    if spawner.spawn_timer_remaining > 0:
        return False
    enemies.append(_spawn_enemy(player))
    spawner.spawn_timer_remaining = ENEMY_SPAWN_INTERVAL_S
    return True
