import pygame

from config.bullet import BULLET_RADIUS
from config.enemy import ENEMY_RADIUS
from entities.bullet import Bullet
from entities.enemy import Enemy

BULLET_HITBOX_COLOR = (255, 220, 80)
ENEMY_HITBOX_COLOR = (255, 100, 100)


def draw_collision_debug(
    surface: pygame.Surface,
    bullets: list[Bullet],
    enemies: list[Enemy],
) -> None:
    for bullet in bullets:
        center = (int(bullet.position.x), int(bullet.position.y))
        pygame.draw.circle(
            surface, BULLET_HITBOX_COLOR, center, int(BULLET_RADIUS), 1
        )
    for enemy in enemies:
        center = (int(enemy.position.x), int(enemy.position.y))
        pygame.draw.circle(
            surface, ENEMY_HITBOX_COLOR, center, int(ENEMY_RADIUS), 1
        )
