from pygame.math import Vector2

from config.player import MAX_PLAYER_SPEED
from entities.player import Player
from systems.player_input import PlayerInput
from world.direction import forward_direction


def _apply_rotation(player: Player, player_input: PlayerInput, dt: float) -> None:
    if player_input.rotate_left:
        player.rotation -= player.rotation_speed * dt
    if player_input.rotate_right:
        player.rotation += player.rotation_speed * dt


def _apply_thrust(player: Player, player_input: PlayerInput, dt: float) -> None:
    if not player_input.thrust:
        return
    acceleration = forward_direction(player.rotation) * player.thrust_force
    player.velocity += acceleration * dt


def _clamp_velocity(player: Player) -> None:
    speed = player.velocity.length()
    if speed <= MAX_PLAYER_SPEED:
        return
    player.velocity.scale_to_length(MAX_PLAYER_SPEED)


def _integrate_position(player: Player, dt: float) -> None:
    player.position += player.velocity * dt


def update_player_movement(
    player: Player, player_input: PlayerInput, dt: float
) -> None:
    _apply_rotation(player, player_input, dt)
    _apply_thrust(player, player_input, dt)
    _clamp_velocity(player)
    _integrate_position(player, dt)
