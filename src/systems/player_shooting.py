from pygame.math import Vector2

from config.bullet import BULLET_LIFETIME_SECONDS, BULLET_SPEED
from config.player import BULLET_SIDE_ANGLE, SHOOT_COOLDOWN_S
from entities.bullet import Bullet
from entities.player import Player
from world.direction import forward_direction

BULLET_LINE_ANGLE_OFFSETS = (-BULLET_SIDE_ANGLE, 0.0, BULLET_SIDE_ANGLE)


def _spawn_bullets(player: Player, bullets: list[Bullet]) -> None:
    for angle_offset in BULLET_LINE_ANGLE_OFFSETS:
        direction = forward_direction(player.rotation + angle_offset)
        bullets.append(
            Bullet(
                position=Vector2(player.position),
                velocity=direction * BULLET_SPEED,
                direction=direction,
                time_remaining=BULLET_LIFETIME_SECONDS,
            )
        )


def _try_fire(player: Player, bullets: list[Bullet]) -> None:
    _spawn_bullets(player, bullets)
    player.shoot_cooldown_remaining = SHOOT_COOLDOWN_S


def update_player_shooting(
    player: Player, bullets: list[Bullet], dt: float
) -> None:
    player.shoot_cooldown_remaining -= dt
    if player.shoot_cooldown_remaining > 0:
        return
    _try_fire(player, bullets)
