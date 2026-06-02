import pygame

from config.bullet import BULLET_COLOR, BULLET_OUTLINE_COLOR, BULLET_RADIUS
from entities.bullet import Bullet


def draw_bullets(surface: pygame.Surface, bullets: list[Bullet]) -> None:
    for bullet in bullets:
        center = (int(bullet.position.x), int(bullet.position.y))
        pygame.draw.circle(surface, BULLET_COLOR, center, BULLET_RADIUS)
        pygame.draw.circle(surface, BULLET_OUTLINE_COLOR, center, BULLET_RADIUS, 1)
