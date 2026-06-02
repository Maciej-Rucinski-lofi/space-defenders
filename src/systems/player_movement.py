import math

from pygame.math import Vector2

from entities.player import Player
from systems.player_input import PlayerInput


def _forward_direction(rotation: float) -> Vector2:
    return Vector2(math.sin(rotation), -math.cos(rotation))


def _apply_rotation(player: Player, player_input: PlayerInput, dt: float) -> None:
    if player_input.rotate_left:
        player.rotation -= player.rotation_speed * dt
    if player_input.rotate_right:
        player.rotation += player.rotation_speed * dt


def _apply_thrust(player: Player, player_input: PlayerInput, dt: float) -> None:
    if not player_input.thrust:
        return
    acceleration = _forward_direction(player.rotation) * player.thrust_force
    player.velocity += acceleration * dt


def _integrate_position(player: Player, dt: float) -> None:
    player.position += player.velocity * dt


def update_player_movement(
    player: Player, player_input: PlayerInput, dt: float
) -> None:
    _apply_rotation(player, player_input, dt)
    _apply_thrust(player, player_input, dt)
    _integrate_position(player, dt)
