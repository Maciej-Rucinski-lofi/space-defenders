import random

from config.enemy_behaviour import ENEMY_AI_SEED

_enemy_rng = random.Random(ENEMY_AI_SEED) if ENEMY_AI_SEED is not None else random.Random()


def get_enemy_rng() -> random.Random:
    return _enemy_rng
