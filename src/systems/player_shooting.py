from pygame.math import Vector2

from config.bullet import BULLET_LIFESPAN_S, BULLET_SPEED
from config.player import SHOOT_COOLDOWN_S
from entities.bullet import Bullet
from entities.player import Player
from world.direction import forward_direction


def _spawn_bullet(player: Player, bullets: list[Bullet]) -> None:
    direction = forward_direction(player.rotation)
    bullets.append(
        Bullet(
            position=Vector2(player.position),
            velocity=direction * BULLET_SPEED,
            time_remaining=BULLET_LIFESPAN_S,
        )
    )


def _try_fire(player: Player, bullets: list[Bullet]) -> None:
    _spawn_bullet(player, bullets)
    player.shoot_cooldown_remaining = SHOOT_COOLDOWN_S


def update_player_shooting(
    player: Player, bullets: list[Bullet], dt: float
) -> None:
    player.shoot_cooldown_remaining -= dt
    if player.shoot_cooldown_remaining > 0:
        return
    _try_fire(player, bullets)
