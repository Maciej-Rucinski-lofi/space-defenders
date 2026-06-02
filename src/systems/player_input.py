from dataclasses import dataclass

import pygame


@dataclass(frozen=True)
class PlayerInput:
    rotate_left: bool
    rotate_right: bool
    thrust: bool


def read_player_one_input() -> PlayerInput:
    keys = pygame.key.get_pressed()
    return PlayerInput(
        rotate_left=keys[pygame.K_LEFT],
        rotate_right=keys[pygame.K_RIGHT],
        thrust=keys[pygame.K_UP],
    )
