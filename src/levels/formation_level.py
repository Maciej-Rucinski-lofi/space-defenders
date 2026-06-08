import pygame

from config.formation import FORMATION_LABEL_FONT_SIZE
from entities.bullet import Bullet
from entities.enemy import Enemy
from entities.player import Player
from game.formation_player_setup import create_formation_players
from levels.base_level import BaseLevel
from systems.bullet_system import update_bullets
from systems.bullet_render import draw_bullets
from systems.collision import process_bullet_enemy_collisions
from systems.enemy_render import draw_enemies
from systems.formation_background import (
    ScrollingStarfield,
    draw_formation_label,
    draw_player_zone_line,
)
from systems.formation_placeholder_enemies import create_placeholder_enemies
from systems.formation_player_input import (
    read_formation_player_one_input,
    read_formation_player_two_input,
)
from systems.formation_player_movement import (
    create_player_zone_bounds,
    update_formation_player_movement,
)
from systems.health_render import draw_health_hud
from systems.player_render import draw_player
from systems.player_shooting import update_player_shooting


class FormationLevel(BaseLevel):
    def __init__(self, window_width: int, window_height: int) -> None:
        self._window_width = window_width
        self._window_height = window_height
        self._players: list[Player] = []
        self._bullets: list[Bullet] = []
        self._enemies: list[Enemy] = []
        self._starfield = ScrollingStarfield(window_width, window_height)
        self._zone_bounds = create_player_zone_bounds(window_width, window_height)
        self._label_font: pygame.font.Font | None = None

    def initialize(self) -> None:
        self._players = create_formation_players(self._window_width, self._window_height)
        self._bullets = []
        self._enemies = create_placeholder_enemies(self._window_width)
        self._starfield = ScrollingStarfield(self._window_width, self._window_height)
        self._zone_bounds = create_player_zone_bounds(
            self._window_width, self._window_height
        )
        self._label_font = pygame.font.Font(None, FORMATION_LABEL_FONT_SIZE)

    def update(self, dt: float) -> None:
        self._starfield.update(dt)
        self._update_players(dt)
        update_bullets(self._bullets, dt)
        process_bullet_enemy_collisions(self._bullets, self._enemies)

    def render(self, screen: pygame.Surface) -> None:
        self._starfield.draw(screen)
        draw_player_zone_line(screen, self._zone_bounds.top)
        if self._label_font is not None:
            draw_formation_label(screen, self._label_font)
        draw_enemies(screen, self._enemies)
        for player in self._players:
            draw_player(screen, player)
        draw_bullets(screen, self._bullets)
        draw_health_hud(screen, self._players)

    def cleanup(self) -> None:
        self._players = []
        self._bullets = []
        self._enemies = []
        self._label_font = None

    def is_complete(self) -> bool:
        return False

    def _update_players(self, dt: float) -> None:
        player_inputs = [
            read_formation_player_one_input(),
            read_formation_player_two_input(),
        ]
        for player, player_input in zip(self._players, player_inputs):
            update_formation_player_movement(
                player, player_input, dt, self._zone_bounds
            )
            update_player_shooting(player, self._bullets, dt)
