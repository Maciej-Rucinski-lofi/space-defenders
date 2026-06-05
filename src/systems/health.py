from config.player import ENEMY_COLLISION_DAMAGE
from entities.player import Player


def apply_enemy_collision_damage(player: Player) -> None:
    if player.is_destroyed:
        return
    player.health -= ENEMY_COLLISION_DAMAGE
    if player.health <= 0:
        player.health = 0
        player.is_destroyed = True


def any_player_alive(players: list[Player]) -> bool:
    return any(not player.is_destroyed for player in players)
