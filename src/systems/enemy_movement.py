import math
import random

from pygame.math import Vector2

from config.enemy import ENEMY_STEER_STRENGTH
from config.enemy_behaviour import ENEMY_TYPE_PROFILES, EnemyTypeProfile
from entities.enemy import Enemy
from entities.enemy_type import EnemyType
from entities.player import Player
from world.enemy_rng import get_enemy_rng


def _rotation_from_velocity(velocity: Vector2) -> float:
    return math.atan2(velocity.x, -velocity.y)


def _profile(enemy: Enemy) -> EnemyTypeProfile:
    return ENEMY_TYPE_PROFILES[enemy.enemy_type]


def _random_behaviour_interval(profile: EnemyTypeProfile, rng: random.Random) -> float:
    return rng.uniform(
        profile.behaviour_interval_min_s,
        profile.behaviour_interval_max_s,
    )


def _random_steering_offset(
    profile: EnemyTypeProfile, rng: random.Random
) -> Vector2:
    angle = rng.uniform(0.0, 2.0 * math.pi)
    magnitude = rng.uniform(0.0, profile.steering_offset_strength)
    return Vector2(math.cos(angle), math.sin(angle)) * magnitude


def _refresh_steering(enemy: Enemy, profile: EnemyTypeProfile, rng: random.Random) -> None:
    enemy.steering_offset = _random_steering_offset(profile, rng)
    enemy.behaviour_timer = _random_behaviour_interval(profile, rng)


def _tick_behaviour_timer(enemy: Enemy, profile: EnemyTypeProfile, rng: random.Random, dt: float) -> None:
    enemy.behaviour_timer -= dt
    if enemy.behaviour_timer <= 0.0:
        _refresh_steering(enemy, profile, rng)


def _steered_direction(enemy: Enemy, player: Player) -> Vector2 | None:
    delta = player.position - enemy.position
    if delta.length_squared() == 0:
        return None
    base = delta.normalize()
    combined = base + enemy.steering_offset
    if combined.length_squared() == 0:
        return base
    return combined.normalize()


def _steer_toward_player(enemy: Enemy, player: Player, dt: float) -> None:
    direction = _steered_direction(enemy, player)
    if direction is None:
        return
    desired_velocity = direction * enemy.speed
    blend = min(1.0, ENEMY_STEER_STRENGTH * dt)
    enemy.velocity = enemy.velocity.lerp(desired_velocity, blend)
    enemy.rotation = _rotation_from_velocity(enemy.velocity)


def _integrate_position(enemy: Enemy, dt: float) -> None:
    enemy.position += enemy.velocity * dt


def update_enemies(
    enemies: list[Enemy], target: Player | None, dt: float
) -> None:
    rng = get_enemy_rng()
    for enemy in enemies:
        profile = _profile(enemy)
        _tick_behaviour_timer(enemy, profile, rng, dt)
        if target is not None:
            _steer_toward_player(enemy, target, dt)
        _integrate_position(enemy, dt)


def initial_steering_state(
    enemy_type: EnemyType, rng: random.Random | None = None
) -> tuple[Vector2, float]:
    source = rng if rng is not None else get_enemy_rng()
    profile = ENEMY_TYPE_PROFILES[enemy_type]
    offset = _random_steering_offset(profile, source)
    timer = _random_behaviour_interval(profile, source)
    return offset, timer
