from dataclasses import dataclass

from config.formation import (
    FORMATION_MOVE_SPEED,
    PLAYER_ZONE_BOTTOM_MARGIN,
    PLAYER_ZONE_HEIGHT_RATIO,
    PLAYER_ZONE_TOP_MARGIN,
)
from config.player import PLAYER_RADIUS
from entities.player import Player
from systems.formation_player_input import FormationPlayerInput


@dataclass(frozen=True)
class PlayerZoneBounds:
    left: float
    right: float
    top: float
    bottom: float


def create_player_zone_bounds(window_width: int, window_height: int) -> PlayerZoneBounds:
    zone_height = window_height * PLAYER_ZONE_HEIGHT_RATIO
    top = window_height - zone_height - PLAYER_ZONE_TOP_MARGIN
    return PlayerZoneBounds(
        left=PLAYER_RADIUS,
        right=float(window_width) - PLAYER_RADIUS,
        top=top,
        bottom=float(window_height) - PLAYER_ZONE_BOTTOM_MARGIN,
    )


def _horizontal_velocity(player_input: FormationPlayerInput) -> float:
    if player_input.move_left and player_input.move_right:
        return 0.0
    if player_input.move_left:
        return -FORMATION_MOVE_SPEED
    if player_input.move_right:
        return FORMATION_MOVE_SPEED
    return 0.0


def _clamp_horizontal(player: Player, bounds: PlayerZoneBounds) -> None:
    player.position.x = max(bounds.left, min(bounds.right, player.position.x))


def update_formation_player_movement(
    player: Player,
    player_input: FormationPlayerInput,
    dt: float,
    bounds: PlayerZoneBounds,
) -> None:
    if player.is_destroyed:
        return
    player.velocity.x = _horizontal_velocity(player_input)
    player.velocity.y = 0.0
    player.position.x += player.velocity.x * dt
    _clamp_horizontal(player, bounds)
