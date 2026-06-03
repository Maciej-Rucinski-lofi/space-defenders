from pygame.math import Vector2

from config.bullet import BULLET_RADIUS
from config.enemy import ENEMY_RADIUS
from entities.bullet import Bullet
from entities.enemy import Enemy


def _circles_overlap(
    pos_a: Vector2,
    radius_a: float,
    pos_b: Vector2,
    radius_b: float,
) -> bool:
    combined = radius_a + radius_b
    return (pos_a - pos_b).length_squared() < combined * combined


def _remove_indices[T](items: list[T], indices: set[int]) -> None:
    if not indices:
        return
    write = 0
    for index, item in enumerate(items):
        if index not in indices:
            items[write] = item
            write += 1
    del items[write:]


def process_bullet_enemy_collisions(
    bullets: list[Bullet],
    enemies: list[Enemy],
) -> None:
    bullets_to_remove: set[int] = set()
    enemies_to_remove: set[int] = set()

    for bullet_index, bullet in enumerate(bullets):
        if bullet_index in bullets_to_remove:
            continue
        for enemy_index, enemy in enumerate(enemies):
            if enemy_index in enemies_to_remove:
                continue
            if _circles_overlap(
                bullet.position,
                BULLET_RADIUS,
                enemy.position,
                ENEMY_RADIUS,
            ):
                bullets_to_remove.add(bullet_index)
                enemies_to_remove.add(enemy_index)
                break

    _remove_indices(bullets, bullets_to_remove)
    _remove_indices(enemies, enemies_to_remove)
