from config.bullet import BULLET_OFFSCREEN_MARGIN
from config.settings import WINDOW_HEIGHT, WINDOW_WIDTH
from entities.bullet import Bullet


def _integrate_position(bullet: Bullet, dt: float) -> None:
    bullet.position += bullet.velocity * dt


def _tick_lifespan(bullet: Bullet, dt: float) -> None:
    bullet.time_remaining -= dt


def _is_lifetime_expired(bullet: Bullet) -> bool:
    return bullet.time_remaining <= 0


def _is_off_screen(
    bullet: Bullet, margin: float, width: float, height: float
) -> bool:
    x, y = bullet.position.x, bullet.position.y
    return (
        x < -margin
        or x > width + margin
        or y < -margin
        or y > height + margin
    )


def _should_remove(
    bullet: Bullet, margin: float, width: float, height: float
) -> bool:
    return _is_lifetime_expired(bullet) or _is_off_screen(
        bullet, margin, width, height
    )


def update_bullets(bullets: list[Bullet], dt: float) -> None:
    margin = BULLET_OFFSCREEN_MARGIN
    width = float(WINDOW_WIDTH)
    height = float(WINDOW_HEIGHT)
    write = 0
    for bullet in bullets:
        _integrate_position(bullet, dt)
        _tick_lifespan(bullet, dt)
        if not _should_remove(bullet, margin, width, height):
            bullets[write] = bullet
            write += 1
    del bullets[write:]
