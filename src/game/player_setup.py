from pygame.math import Vector2

from config.player import (
    FACING_LEFT_ROTATION,
    MAX_HEALTH,
    PLAYER_TWO_SHIP_COLOR,
    PLAYER_TWO_SHIP_OUTLINE_COLOR,
    ROTATION_SPEED,
    SHIP_COLOR,
    SHIP_OUTLINE_COLOR,
    SPAWN_HORIZONTAL_OFFSET,
    THRUST_FORCE,
)
from entities.player import Player


def _create_player_at(
    position: Vector2,
    ship_color: tuple[int, int, int],
    ship_outline_color: tuple[int, int, int],
) -> Player:
    return Player(
        position=position,
        velocity=Vector2(0, 0),
        rotation=FACING_LEFT_ROTATION,
        rotation_speed=ROTATION_SPEED,
        thrust_force=THRUST_FORCE,
        shoot_cooldown_remaining=0.0,
        health=MAX_HEALTH,
        max_health=MAX_HEALTH,
        is_destroyed=False,
        ship_color=ship_color,
        ship_outline_color=ship_outline_color,
    )


def create_players(window_width: int, window_height: int) -> list[Player]:
    center = Vector2(window_width / 2, window_height / 2)
    return [
        _create_player_at(
            center + Vector2(-SPAWN_HORIZONTAL_OFFSET, 0),
            SHIP_COLOR,
            SHIP_OUTLINE_COLOR,
        ),
        _create_player_at(
            center + Vector2(SPAWN_HORIZONTAL_OFFSET, 0),
            PLAYER_TWO_SHIP_COLOR,
            PLAYER_TWO_SHIP_OUTLINE_COLOR,
        ),
    ]


def nearest_alive_player(
    players: list[Player], from_position: Vector2
) -> Player | None:
    nearest: Player | None = None
    nearest_distance_sq = float("inf")
    for player in players:
        if player.is_destroyed:
            continue
        distance_sq = (player.position - from_position).length_squared()
        if distance_sq < nearest_distance_sq:
            nearest_distance_sq = distance_sq
            nearest = player
    return nearest
