import pygame

from config.enemy_behaviour import ENEMY_AI_DEBUG
from entities.bullet import Bullet
from entities.enemy import Enemy
from entities.player import Player
from game.player_setup import create_players
from levels.base_level import BaseLevel
from systems.bullet_system import update_bullets
from systems.bullet_render import draw_bullets
from systems.collision import (
    process_bullet_enemy_collisions,
    process_enemy_player_collisions,
)
from systems.collision_debug_render import draw_collision_debug
from systems.enemy_debug_render import draw_enemy_debug
from systems.enemy_movement import update_enemies
from systems.enemy_render import draw_enemies
from systems.enemy_spawner import create_enemy_spawner, update_enemy_spawner
from systems.game_over_render import draw_game_over
from systems.game_state import (
    create_game_state,
    is_gameplay_active,
    update_game_state,
)
from systems.health_render import draw_health_hud
from systems.player_input import read_player_one_input, read_player_two_input
from systems.player_movement import update_player_movement
from systems.player_render import draw_player
from systems.player_screen_wrap import update_player_screen_wrap
from systems.player_shooting import update_player_shooting
from systems.wave_manager import (
    create_wave_manager,
    is_spawn_allowed,
    record_enemy_spawned,
    update_wave_manager,
)
from systems.wave_render import draw_wave_announcement, draw_wave_hud


class SurvivalLevel(BaseLevel):
    def __init__(self, window_width: int, window_height: int) -> None:
        self._window_width = window_width
        self._window_height = window_height
        self._players: list[Player] = []
        self._bullets: list[Bullet] = []
        self._enemies: list[Enemy] = []
        self._enemy_spawner = create_enemy_spawner()
        self._wave_manager = create_wave_manager()
        self._game_state = create_game_state()
        self._enemy_ai_debug = ENEMY_AI_DEBUG

    def initialize(self) -> None:
        self._players = create_players(self._window_width, self._window_height)
        self._bullets = []
        self._enemies = []
        self._enemy_spawner = create_enemy_spawner()
        self._wave_manager = create_wave_manager()
        self._game_state = create_game_state()
        self._enemy_ai_debug = ENEMY_AI_DEBUG

    def update(self, dt: float) -> None:
        if not is_gameplay_active(self._game_state):
            return

        self._update_players(dt)
        update_bullets(self._bullets, dt)
        spawned = update_enemy_spawner(
            self._enemy_spawner,
            self._enemies,
            self._players,
            dt,
            is_spawn_allowed(self._wave_manager),
        )
        if spawned:
            record_enemy_spawned(self._wave_manager)
        update_enemies(self._enemies, self._players, dt)
        process_bullet_enemy_collisions(self._bullets, self._enemies)
        process_enemy_player_collisions(self._enemies, self._players)
        update_wave_manager(self._wave_manager, len(self._enemies), dt)
        update_game_state(self._game_state, self._players)

    def render(self, screen: pygame.Surface) -> None:
        for player in self._players:
            draw_player(screen, player)
        draw_bullets(screen, self._bullets)
        draw_enemies(screen, self._enemies)
        draw_wave_announcement(screen, self._wave_manager)
        draw_wave_hud(screen, self._wave_manager, len(self._enemies))
        draw_health_hud(screen, self._players)
        draw_game_over(
            screen,
            self._game_state,
            self._wave_manager.wave_number,
        )
        if self._enemy_ai_debug:
            draw_collision_debug(screen, self._bullets, self._enemies)
            draw_enemy_debug(screen, self._enemies, self._players)

    def cleanup(self) -> None:
        self._players = []
        self._bullets = []
        self._enemies = []

    def is_complete(self) -> bool:
        return False

    def toggle_debug(self) -> None:
        self._enemy_ai_debug = not self._enemy_ai_debug

    def _update_players(self, dt: float) -> None:
        player_inputs = [read_player_one_input(), read_player_two_input()]
        for player, player_input in zip(self._players, player_inputs):
            update_player_movement(player, player_input, dt)
            update_player_screen_wrap(player)
            update_player_shooting(player, self._bullets, dt)
