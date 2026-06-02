from entities.bullet import Bullet


def _integrate_position(bullet: Bullet, dt: float) -> None:
    bullet.position += bullet.velocity * dt


def _tick_lifespan(bullet: Bullet, dt: float) -> None:
    bullet.time_remaining -= dt


def _is_expired(bullet: Bullet) -> bool:
    return bullet.time_remaining <= 0


def update_bullets(bullets: list[Bullet], dt: float) -> None:
    for bullet in bullets:
        _integrate_position(bullet, dt)
        _tick_lifespan(bullet, dt)
    bullets[:] = [bullet for bullet in bullets if not _is_expired(bullet)]
