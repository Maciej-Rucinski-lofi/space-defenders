from pygame.math import Vector2

from config.formation import (
    FORMATION_FACING_ROTATION,
    PLAYER_ZONE_BOTTOM_MARGIN,
    PLAYER_ZONE_HEIGHT_RATIO,
)
from config.player import (
    MAX_HEALTH,
    PLAYER_TWO_SHIP_COLOR,
    PLAYER_TWO_SHIP_OUTLINE_COLOR,
    ROTATION_SPEED,
    SHIP_COLOR,
    SHIP_OUTLINE_COLOR,
    SPAWN_HORIZONTAL_OFFSET,
    THRUST_FORCE,
)
from config.player_names import load_player_names
from entities.player import Player


def _create_formation_player_at(
    position: Vector2,
    name: str,
    ship_color: tuple[int, int, int],
    ship_outline_color: tuple[int, int, int],
) -> Player:
    return Player(
        position=position,
        velocity=Vector2(0, 0),
        rotation=FORMATION_FACING_ROTATION,
        rotation_speed=ROTATION_SPEED,
        thrust_force=THRUST_FORCE,
        shoot_cooldown_remaining=0.0,
        health=MAX_HEALTH,
        max_health=MAX_HEALTH,
        is_destroyed=False,
        name=name,
        ship_color=ship_color,
        ship_outline_color=ship_outline_color,
    )


def create_formation_players(window_width: int, window_height: int) -> list[Player]:
    names = load_player_names()
    zone_height = window_height * PLAYER_ZONE_HEIGHT_RATIO
    spawn_y = window_height - PLAYER_ZONE_BOTTOM_MARGIN
    center_x = window_width / 2
    return [
        _create_formation_player_at(
            Vector2(center_x - SPAWN_HORIZONTAL_OFFSET, spawn_y),
            names.player_one,
            SHIP_COLOR,
            SHIP_OUTLINE_COLOR,
        ),
        _create_formation_player_at(
            Vector2(center_x + SPAWN_HORIZONTAL_OFFSET, spawn_y),
            names.player_two,
            PLAYER_TWO_SHIP_COLOR,
            PLAYER_TWO_SHIP_OUTLINE_COLOR,
        ),
    ]
