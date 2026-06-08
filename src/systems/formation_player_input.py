from dataclasses import dataclass

import pygame


@dataclass(frozen=True)
class FormationPlayerInput:
    move_left: bool
    move_right: bool


def read_formation_player_one_input() -> FormationPlayerInput:
    keys = pygame.key.get_pressed()
    return FormationPlayerInput(
        move_left=keys[pygame.K_a],
        move_right=keys[pygame.K_d],
    )


def read_formation_player_two_input() -> FormationPlayerInput:
    keys = pygame.key.get_pressed()
    return FormationPlayerInput(
        move_left=keys[pygame.K_LEFT],
        move_right=keys[pygame.K_RIGHT],
    )
