from dataclasses import dataclass

from entities.enemy_type import EnemyType

ENEMY_AI_SEED: int | None = None
ENEMY_AI_DEBUG = False


@dataclass(frozen=True)
class EnemyTypeProfile:
    speed_multiplier: float
    steering_offset_strength: float
    behaviour_interval_min_s: float
    behaviour_interval_max_s: float
    can_shoot: bool
    color: tuple[int, int, int]
    outline_color: tuple[int, int, int]


ENEMY_TYPE_PROFILES: dict[EnemyType, EnemyTypeProfile] = {
    EnemyType.CHASER: EnemyTypeProfile(
        speed_multiplier=1.0,
        steering_offset_strength=0.2,
        behaviour_interval_min_s=1.0,
        behaviour_interval_max_s=2.0,
        can_shoot=True,
        color=(255, 70, 70),
        outline_color=(255, 180, 180),
    ),
    EnemyType.DRIFTER: EnemyTypeProfile(
        speed_multiplier=0.75,
        steering_offset_strength=0.55,
        behaviour_interval_min_s=0.5,
        behaviour_interval_max_s=1.5,
        can_shoot=True,
        color=(255, 140, 50),
        outline_color=(255, 200, 140),
    ),
    EnemyType.KAMIKAZE: EnemyTypeProfile(
        speed_multiplier=1.45,
        steering_offset_strength=0.45,
        behaviour_interval_min_s=0.5,
        behaviour_interval_max_s=1.0,
        can_shoot=False,
        color=(255, 230, 60),
        outline_color=(255, 255, 160),
    ),
}
